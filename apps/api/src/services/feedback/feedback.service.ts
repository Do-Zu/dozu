import feedbackRepository from '@/repositories/feedback/feedback.repo';
import {
    evaluateFeedback,
    type FeedbackEvaluationResult,
    type FeedbackInput,
} from '@/services/feedback/feedback.evaluator';

/**
 * Service class for Feedback functionality
 */
class FeedbackService {
    constructor() {}

    public async submitFeedback(input: FeedbackInput): Promise<{
        success: boolean;
        feedbackId: number;
        notified: boolean;
        score: number;
        reasons: string[];
    }> {
        const message = input.message?.trim() || '';
        if (!message) {
            // Controller should validate, but keep service safe
            throw new Error('Feedback message is required');
        }

        const evaluation = this.evaluateFeedback({ ...input, message });

        const saved = await this.saveFeedback({ ...input, message }, evaluation);

        const notified = false; // Feedback is saved locally; email delivery is excluded.

        return {
            success: true,
            feedbackId: saved.feedbackId,
            notified,
            score: evaluation.score,
            reasons: evaluation.reasons,
        };
    }

    private evaluateFeedback(input: FeedbackInput): FeedbackEvaluationResult {
        return evaluateFeedback(input);
    }

    private async saveFeedback(input: FeedbackInput, evaluation: FeedbackEvaluationResult): Promise<{ feedbackId: number }> {
        return feedbackRepository.create({
            message: input.message,
            userId: input.userId,
            userEmail: input.userEmail,
            userName: input.userName,
            imageUrl: input.imageUrl,
            hasImage: Boolean(input.imageUrl),
            isImportant: evaluation.score >= 3,
            status: 'new',
            category: undefined,
            score: evaluation.score,
            shouldSendEmail: 0,
            reasons: JSON.stringify(evaluation.reasons),
        });
    }

    /** Email delivery is excluded; do not claim a local feedback record was emailed. */
    public async sendFeedbackMail(_feedbackData: FeedbackInput): Promise<boolean> {
        void _feedbackData;
        return false;
    }

    /**
     * Backward compatibility: old API name.
     * Prefer using submitFeedback() which always saves to DB and filters spam.
     */
    public async sendFeedback(feedbackData: FeedbackInput): Promise<boolean> {
        const result = await this.submitFeedback(feedbackData);
        return result.success;
    }
}

export default new FeedbackService();
