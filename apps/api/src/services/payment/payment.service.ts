import db from '@/libs/drizzleClient.lib';
import { transactionsModel } from '@/models/payment/transaction.model';
import { DatabaseError } from '@/core/error';
import logger from '@/utils/logger';
import { assertPaymentsAvailable } from '@/services/payment/paymentAvailability.service';
import { PaymentLinkRequest, TransactionStatusUpdate } from './type';
import { and, eq, desc } from 'drizzle-orm';

// Legacy transaction records remain queryable; executing a payment is excluded.
class PaymentService {
    public async createPaymentLinkWithPayOS(_request: PaymentLinkRequest): Promise<never> {
        void _request;
        return assertPaymentsAvailable();
    }

    public async updateTransactionStatus(_payment: TransactionStatusUpdate): Promise<never> {
        void _payment;
        return assertPaymentsAvailable();
    }

    public async getTransactionOfGateway({ orderCode, paymentId }: { orderCode: number; paymentId: string }) {
        const [existing] = await db
            .select({
                userId: transactionsModel.userId,
                transactionId: transactionsModel.transactionId,
                status: transactionsModel.status,
                metadata: transactionsModel.metadata,
            })
            .from(transactionsModel)
            .where(and(eq(transactionsModel.code, orderCode.toString()), eq(transactionsModel.paymentId, paymentId)))
            .limit(1);

        return existing;
    }
    public async getUserTransactionHistory(userId: number, limit: number = 50) {
        try {
            const transactions = await db
                .select({
                    transactionId: transactionsModel.transactionId,
                    gateway: transactionsModel.gateway,
                    transactionDate: transactionsModel.transactionDate,
                    accountNumber: transactionsModel.accountNumber,
                    amount: transactionsModel.amount,
                    currency: transactionsModel.currency,
                    code: transactionsModel.code,
                    paymentId: transactionsModel.paymentId,
                    description: transactionsModel.description,
                    status: transactionsModel.status,
                    metadata: transactionsModel.metadata,
                    createdAt: transactionsModel.createdAt,
                    updatedAt: transactionsModel.updatedAt,
                })
                .from(transactionsModel)
                .where(eq(transactionsModel.userId, userId))
                .orderBy(desc(transactionsModel.createdAt))
                .limit(limit);

            return transactions;
        } catch (error) {
            logger.error(`Error getting user transaction history: ${error}`);
            throw new DatabaseError('Failed to get transaction history');
        }
    }
}

export const paymentService = new PaymentService();
