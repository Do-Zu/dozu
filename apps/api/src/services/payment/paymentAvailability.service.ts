import { ServiceUnavailable } from '@/core/error';

// Desktop payment execution is excluded. Never fabricate a paid transaction or entitlement.
export const assertPaymentsAvailable = (): never => {
    throw new ServiceUnavailable('Payments are unavailable in this desktop version.');
};
