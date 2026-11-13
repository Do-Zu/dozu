import dotenv from 'dotenv';
import path from 'node:path';
import * as fs from 'fs';

const isDevelopment = process.env.NODE_ENV !== 'production';
const environment = process.env.NODE_ENV || 'development';

const rootPath = path.resolve(__dirname, '../../');

const envFile = isDevelopment ? '.env.development' : '.env.production';
const envPath = path.resolve(rootPath, envFile);

try {
    if (fs.existsSync(envPath)) {
        const result = dotenv.config({
            path: envPath,
        });

        if (result.error) {
            throw result.error;
        }

        process.stdout.write(`Loaded environment from ${envFile}\n`);
    } else {
        process.stderr.write(`Environment file ${envFile} not found, using default values\n`);
    }
} catch (error) {
    process.stderr.write(`Error loading environment: ${(error as Error).message}\n`);
}

function getEnv(name: string): string | undefined {
    const v = process.env[name];
    const trimmed = typeof v === 'string' ? v.trim() : v;
    if (!trimmed || trimmed.length === 0) return undefined;
    return trimmed;
}

// Validate required environment variables
const requiredEnvVars: string[] = ['PORT', 'HOST'];

const missingEnvVars = requiredEnvVars.filter(name => !process.env[name]);

if (missingEnvVars.length > 0) {
    process.stderr.write(`Missing required environment variables: ${missingEnvVars.join(', ')}\n`);
}

interface ServerConfig {
    port: number;
    host: string;
}

interface AppConfig {
    env: string;
    server: ServerConfig;
    allowedOrigins: string[];
    isProduction: boolean;
    isDevelopment: boolean;
    trustProxy: boolean | number;
    backendBaseUrl: string;
}

const allowedOrigins =
    getEnv('ALLOWED_ORIGINS')
        ?.split(',')
        ?.map(origin => origin.trim())
        .filter(Boolean) ?? [];

if (allowedOrigins.length === 0) {
    process.stderr.write('ALLOWED_ORIGINS is empty. CORS may block all cross-origin requests.\n');
}

export const config: AppConfig = {
    env: environment,
    isProduction: environment === 'production',
    isDevelopment: environment === 'development',
    server: {
        port: parseInt(process.env.PORT || '3333', 10),
        host: process.env.HOST || 'localhost',
    },
    allowedOrigins,
    // LAN/deployed URLs must be supplied explicitly; wildcard bind hosts are not public URLs.
    backendBaseUrl: (
        getEnv('BACKEND_BASE_URL') || getEnv('BACK_END_URL') || `http://localhost:${getEnv('PORT') || '3333'}`
    ).replace(/\/+$/, ''),
    // Trust proxy configuration for rate limiting and IP detection
    // Can be configured via TRUST_PROXY environment variable
    // Values: 'true', 'false', or a number (e.g., '1' to trust first proxy)
    trustProxy: process.env.TRUST_PROXY
        ? process.env.TRUST_PROXY === 'true'
            ? true
            : process.env.TRUST_PROXY === 'false'
              ? false
              : parseInt(process.env.TRUST_PROXY, 10)
        : environment === 'production'
          ? 1
          : true,
};

export { getEnv };
