import { defineConfig } from 'drizzle-kit';
import * as dotenv from 'dotenv';
import path from 'node:path';
import fs from 'fs';

const env = process.env.NODE_ENV || 'development';
const envPath = path.resolve(__dirname, `.env${env !== 'development' ? '.' + env : ''}`);

if (fs.existsSync(envPath)) {
    dotenv.config({ path: envPath });
}

const databaseUrl = process.env.DATABASE_URL_DRIZZLE_MIGRATE!;

export default defineConfig({
    out: path.resolve(__dirname, 'drizzle'),
    schema: path.resolve(__dirname, 'src/models'),
    dialect: 'postgresql',
    dbCredentials: {
        url: databaseUrl,
    },
});
