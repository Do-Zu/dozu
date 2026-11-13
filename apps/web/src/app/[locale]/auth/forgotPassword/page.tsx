'use client';

import Link from 'next/link';
import { useTranslations } from 'next-intl';
import CentralCard from '@/components/auth/CentralCard';
import { Button } from '@/components/ui/button';
import { CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card';
import { ROUTES } from '@/utils/constants/routes';

const ForgotPasswordPage = () => {
    const t = useTranslations('ForgotPasswordPage');
    const availability = useTranslations('EmailAvailability');

    return (
        <CentralCard>
            <CardHeader className="space-y-2 text-center">
                <CardTitle className="text-3xl font-bold">{t('title')}</CardTitle>
                <CardDescription className="text-base text-muted-foreground" role="status">
                    {availability('recoveryUnavailable')}
                </CardDescription>
            </CardHeader>
            <CardContent className="space-y-6 p-6">
                <Button asChild className="w-full">
                    <Link href={ROUTES.LOGIN}>{availability('login')}</Link>
                </Button>
            </CardContent>
        </CentralCard>
    );
};

export default ForgotPasswordPage;
