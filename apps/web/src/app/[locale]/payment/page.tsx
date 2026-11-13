'use client';

import Link from 'next/link';
import { useTranslations } from 'next-intl';
import { withAuth } from '@/hoc/withAuth';
import { Button } from '@/components/ui/button';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { ROUTES } from '@/utils/constants/routes';
import { USER_ROLES } from '@/utils/constants/roles';

const PaymentPage = () => {
    const t = useTranslations('PaymentAvailability');

    return (
        <div className="mx-auto max-w-xl p-6">
            <Card>
                <CardHeader>
                    <CardTitle>{t('title')}</CardTitle>
                </CardHeader>
                <CardContent className="space-y-4">
                    <p role="status">{t('description')}</p>
                    <p>{t('history')}</p>
                    <Button asChild>
                        <Link href={ROUTES.HOME}>{t('home')}</Link>
                    </Button>
                </CardContent>
            </Card>
        </div>
    );
};

export default withAuth(PaymentPage, {
    requiredRole: USER_ROLES.USER,
    redirectTo: ROUTES.LANDING,
});
