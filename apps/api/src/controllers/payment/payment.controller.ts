import { BadRequest } from '@/core/error';
import { SuccessResponse } from '@/core/success';
import { paymentService } from '@/services/payment/payment.service';
import { assertPaymentsAvailable } from '@/services/payment/paymentAvailability.service';
import { getUserIdFromRequest } from '@/utils/auth/authHelpers.utils';
import { Request, Response } from 'express';

const paymentUnavailable = async (_req: Request, _res: Response): Promise<never> => {
    void _req;
    void _res;
    return assertPaymentsAvailable();
};

export const paymentController = {
    createLinkPaymentWithPayOS: paymentUnavailable,
    handleWebhookPayOS: paymentUnavailable,
    handleWebhookSepay: paymentUnavailable,
    connectPaymentSSE: paymentUnavailable,
    updateTransactionStatus: paymentUnavailable,
    async getTransactionHistory(req: Request, res: Response) {
        const userId = getUserIdFromRequest(req);

        const DEFAULT_LIMIT = 50;
        const MAX_LIMIT = 100; // adjust as appropriate
        const rawLimit = req.query.limit;

        let limit = DEFAULT_LIMIT;

        if (rawLimit !== undefined) {
            const parsed = Number(rawLimit);

            if (!Number.isInteger(parsed) || parsed <= 0) {
                throw new BadRequest('limit must be a positive integer');
            }

            limit = Math.min(parsed, MAX_LIMIT);
        }

        const transactions = await paymentService.getUserTransactionHistory(userId, limit);

        SuccessResponse.ok(res, transactions, 'Transaction history retrieved successfully');
    }
};
