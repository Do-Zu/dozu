import { ServiceUnavailable } from '@/core/error';

// Email delivery is excluded from this version; never report a message as sent.
export const assertEmailSendingAvailable = (): never => {
    throw new ServiceUnavailable('Email delivery is unavailable in this version.');
};
