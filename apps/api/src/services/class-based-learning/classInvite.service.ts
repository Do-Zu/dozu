import { BadRequest, NotFoundError } from '@/core/error';
import classInviteRepo from '@/repositories/class-based-learning/classInvite.repo';
import userSearchService from '@/services/user/userSearch.service';
import classEnrollmentService from '@/services/class-based-learning/classEnrollment.service';
import { assertEmailSendingAvailable } from '@/libs/email.lib';
import { 
    IClassInvite, 
    IInviteByEmailBody, 
    IGenerateInviteLinkBody, 
    IJoinViaInviteBody,
    IInviteResponse,
    IInviteEmailBatchResponse,
    IUserSearchResult,
    IClassInviteWithDetails
} from '@/types/class-based-learning/classInvite.type';
import { customAlphabet } from 'nanoid';

class ClassInviteService {
    private readonly tokenAlphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    private readonly tokenLength = 32;

    /**
     * Generate unique token for invite
     */
    private generateToken(): string {
        const nanoid = customAlphabet(this.tokenAlphabet, this.tokenLength);
        return nanoid();
    }

    /**
     * Generate invite link
     */
    public async generateInviteLink(
        classId: number, 
        invitedBy: number, 
        data: IGenerateInviteLinkBody
    ): Promise<IInviteResponse> {
        const { expiresInDays = 7, useLimit } = data;
        const expiresAt = new Date();
        expiresAt.setDate(expiresAt.getDate() + expiresInDays);

        // Check if there's already an active invite for this class
        const existingInvite = await classInviteRepo.getActiveInviteForClass(classId);
        if (existingInvite) {
            return {
                inviteId: existingInvite.inviteId,
                classId: existingInvite.classId,
                token: existingInvite.token,
                inviteLink: `${process.env.FRONTEND_BASE_URL}/join/${existingInvite.token}`,
                expiresAt: existingInvite.expiresAt,
                useLimit: existingInvite.useLimit,
                usedCount: existingInvite.usedCount,
                status: existingInvite.status,
                createdAt: existingInvite.createdAt,
            };
        }

        // Generate new token
        let token: string;
        let isUnique = false;
        let attempts = 0;
        const maxAttempts = 10;

        do {
            token = this.generateToken();
            const existingToken = await classInviteRepo.getInviteByToken(token);
            isUnique = !existingToken;
            attempts++;
        } while (!isUnique && attempts < maxAttempts);

        if (!isUnique) {
            throw new Error('Unable to generate unique token after multiple attempts');
        }

        // Create invite
        const invite = await classInviteRepo.createInvite({
            classId,
            invitedBy,
            token,
            expiresAt,
            useLimit,
        });

        return {
            inviteId: invite.inviteId,
            classId: invite.classId,
            token: invite.token,
            inviteLink: `${process.env.FRONTEND_BASE_URL}/join/${invite.token}`,
            expiresAt: invite.expiresAt,
            useLimit: invite.useLimit,
            usedCount: invite.usedCount,
            status: invite.status,
            createdAt: invite.createdAt,
        };
    }

    /**
     * Invite users by email
     */
    public async inviteByEmail(
        _classId: number,
        _invitedBy: number,
        _data: IInviteByEmailBody
    ): Promise<IInviteEmailBatchResponse> {
        void _classId;
        void _invitedBy;
        void _data;
        return assertEmailSendingAvailable();
    }

    /**
     * Search users to invite
     */
    public async searchUsersToInvite(query: string, classId: number): Promise<IUserSearchResult[]> {
        if (!query || query.trim().length < 2) {
            return [];
        }

        const users = await userSearchService.searchUsers(query, classId);
        return users;
    }

    /**
     * Accept invite
     */
    public async acceptInvite(userId: number, data: IJoinViaInviteBody): Promise<void> {
        const { token } = data;

        const invite = await classInviteRepo.getInviteByToken(token);
        if (!invite) {
            throw new NotFoundError('Invalid invite token');
        }

        // Validate invite
        const isValid = await this.validateInvite(invite);
        if (!isValid) {
            throw new BadRequest('Invite has expired or reached usage limit');
        }

        // Check if user is already in class
        const isAlreadyInClass = await classEnrollmentService.isStudentInClass(invite.classId, userId);
        if (isAlreadyInClass) {
            throw new BadRequest('You are already in this class');
        }

        // Add user to class
        await classEnrollmentService.addStudentToClass(invite.classId, userId);

        // Update invite status and increment use count
        await classInviteRepo.updateInviteStatus(invite.inviteId, 'accepted');
        await classInviteRepo.incrementUseCount(invite.inviteId);
    }

    /**
     * Reject invite
     */
    public async rejectInvite(userId: number, data: IJoinViaInviteBody): Promise<void> {
        const { token } = data;

        const invite = await classInviteRepo.getInviteByToken(token);
        if (!invite) {
            throw new NotFoundError('Invalid invite token');
        }

        await classInviteRepo.updateInviteStatus(invite.inviteId, 'rejected');
    }

    /**
     * Regenerate invite link
     */
    public async regenerateInviteLink(
        classId: number,
        invitedBy: number,
        data: IGenerateInviteLinkBody
    ): Promise<IInviteResponse> {
        const { expiresInDays = 7, useLimit } = data;
        const expiresAt = new Date();
        expiresAt.setDate(expiresAt.getDate() + expiresInDays);

        // Generate new token
        let token: string;
        let isUnique = false;
        let attempts = 0;
        const maxAttempts = 10;

        do {
            token = this.generateToken();
            const existingToken = await classInviteRepo.getInviteByToken(token);
            isUnique = !existingToken;
            attempts++;
        } while (!isUnique && attempts < maxAttempts);

        if (!isUnique) {
            throw new Error('Unable to generate unique token after multiple attempts');
        }

        // Regenerate invite
        const invite = await classInviteRepo.regenerateInviteToken(classId, token, expiresAt, useLimit);

        return {
            inviteId: invite.inviteId,
            classId: invite.classId,
            token: invite.token,
            inviteLink: `${process.env.FRONTEND_BASE_URL}/join/${invite.token}`,
            expiresAt: invite.expiresAt,
            useLimit: invite.useLimit,
            usedCount: invite.usedCount,
            status: invite.status,
            createdAt: invite.createdAt,
        };
    }

    /**
     * Validate invite
     */
    public async validateInvite(invite: IClassInvite): Promise<boolean> {
        // Check if invite is still pending
        if (invite.status !== 'pending') {
            return false;
        }

        // Check if invite has expired
        if (invite.expiresAt <= new Date()) {
            return false;
        }

        // Check if invite has reached use limit
        if (invite.useLimit && invite.usedCount >= invite.useLimit) {
            return false;
        }

        return true;
    }

    /**
     * Cleanup expired invites
     */
    public async cleanupExpiredInvites(): Promise<{ deleted: number; updated: number }> {
        const deleted = await classInviteRepo.deleteExpiredInvites();
        const updated = await classInviteRepo.updateExpiredInvitesStatus();
        
        return { deleted, updated };
    }

    /**
     * Get invite statistics for a class
     */
    public async getInviteStats(classId: number) {
        return await classInviteRepo.getInviteStats(classId);
    }
}

export default new ClassInviteService();
