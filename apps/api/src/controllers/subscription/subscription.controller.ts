import { Request, Response } from 'express';
import { BadRequest, InternalServerError, NotFoundError, PaymentRequire } from '@/core/error';
import { SuccessResponse } from '@/core/success';

import { assertPaymentsAvailable } from '@/services/payment/paymentAvailability.service';
import subscriptionService from '@/services/subscription/subscription.service';
import { getCurrentDateInTimeZone, getTimezoneClient } from '@/utils/date';
import {
    checkFeatureUsageSchema,
    recordFeatureUsageSchema,
    updateSubscriptionSchema,
} from '@/dtos/subscription/subscription.dto';
import { getUserIdFromRequest } from '@/utils/auth/authHelpers.utils';
import { toNumber } from '@/utils/common';

export class SubscriptionController {
    /**
     * Get all available plans with features
     */
    public async getAllPlans(_req: Request, res: Response) {
        const plans = await subscriptionService.getAvailablePlans();

        SuccessResponse.ok(res, plans, 'Plans retrieved successfully');
    }

    public async getAllAvailablePlansUpgrade(req: Request, res: Response) {
        const userId = getUserIdFromRequest(req);
        const timezone = getTimezoneClient(req);

        const plans = await subscriptionService.getAvailablePlanForUserUpgrade({
            userId,
            timezone,
        });

        SuccessResponse.ok(res, plans, 'Plans retrieved successfully');
    }

    /**
     * Get current user's subscription
     */
    public getCurrentSubscription = async (req: Request, res: Response) => {
        const userId = req.currentUser?.userId;
        const timezone = getTimezoneClient(req);

        const subscription = await subscriptionService.getUserSubscriptionWithPlan({ userId, timezone });

        SuccessResponse.ok(res, subscription, 'Subscription retrieved successfully');
    };

    public getAllFeaturesOfPlan = async (req: Request, res: Response) => {
        const { planId } = req.body;

        if (!planId) {
            throw new BadRequest('Plan ID is required');
        }

        const features = await subscriptionService.getAllFeaturesOfPlan({ planId });

        if (!features || features.length === 0) {
            throw new NotFoundError('No features found for this plan');
        }

        SuccessResponse.ok(res, features, 'Plan features retrieved successfully');
    };

    /**
     * Create a new subscription
     */
    public async createSubscription(_req: Request, _res: Response): Promise<never> {
        void _req;
        void _res;
        return assertPaymentsAvailable();
    }

    /**
     * Update subscription
     */
    updateSubscription = async (req: Request, res: Response) => {
        const userId = req.currentUser?.userId;

        const validatedData = updateSubscriptionSchema.parse(req.body);
        const subscriptionId = toNumber(validatedData.subscriptionId as string);

        const timeZone = getTimezoneClient(req);
        const date = getCurrentDateInTimeZone(timeZone);

        // Verify subscription belongs to user
        const subscription = await subscriptionService.getUserActiveSubscription(userId);

        if (!subscription || subscription.subscriptionId !== subscriptionId) {
            throw new NotFoundError('Subscription not found');
        }

        // Handle cancellation
        if (validatedData.status === 'cancelled') {
            const success = await subscriptionService.cancelSubscription(
                subscriptionId,
                validatedData.cancellationReason,
                date
            );

            if (!success) {
                throw new InternalServerError('Failed to cancel subscription');
            }
        }

        SuccessResponse.created(res, {}, 'Subscription updated successfully');
    };

    /**
     * Upgrade subscription to a new plan
     * This method allows users to upgrade their subscription plan.
     */
    async upgradeSubscription(_req: Request, _res: Response): Promise<never> {
        void _req;
        void _res;
        return assertPaymentsAvailable();
    }

    /**
     * Check feature usage limit
     */
    checkFeatureUsage = async (req: Request, res: Response) => {
        const userId = req?.currentUser?.userId;

        const validatedData = checkFeatureUsageSchema.parse(req.body);

        const result = await subscriptionService.canUseFeature(
            userId,
            validatedData.featureName,
            validatedData.requestedAmount
        );

        SuccessResponse.ok(res, result);
    };

    /**
     * Record feature usage
     */
    recordFeatureUsage = async (req: Request, res: Response) => {
        const userId = req.currentUser?.userId;

        const validatedData = recordFeatureUsageSchema.parse(req.body);

        // Check if user can use the feature
        const canUse = await subscriptionService.canUseFeature(
            userId,
            validatedData.featureName,
            validatedData.usageAmount
        );

        if (!canUse.canUse) {
            throw new PaymentRequire('Feature usage limit exceeded.');
        }

        const success = await subscriptionService.recordFeatureUsage(
            userId,
            validatedData.featureName,
            validatedData.usageAmount
        );

        if (!success) {
            throw new InternalServerError('Failed to record feature usage');
        }

        SuccessResponse.ok(res, {}, 'Feature usage recorded successfully');
    };

    /**
     * Get user's feature usage summary
     */
    getFeatureUsage = async (req: Request, res: Response) => {
        const userId = req.currentUser?.userId;

        const usage = await subscriptionService.getUserFeatureUsage(userId);

        SuccessResponse.ok(res, usage, 'Feature usage retrieved successfully');
    };

    /**
     * Cancel subscription
     */
    public async cancelSubscription(req: Request, res: Response) {
        const userId = req.currentUser?.userId;

        const validatedData = updateSubscriptionSchema.parse(req.body);

        const date = getCurrentDateInTimeZone(getTimezoneClient(req));

        // Verify user has an active subscription
        const subscription = await subscriptionService.getUserActiveSubscription(userId);
        if (!subscription) {
            throw new NotFoundError('No active subscription found');
        }

        // Cancel the subscription
        const success = await subscriptionService.cancelSubscription(
            subscription.subscriptionId,
            validatedData.cancellationReason,
            date
        );

        if (!success) {
            throw new InternalServerError('Failed to cancel subscription');
        }

        SuccessResponse.accepted(res, {}, 'Subscription cancelled successfully');
    }
}

export default new SubscriptionController();
