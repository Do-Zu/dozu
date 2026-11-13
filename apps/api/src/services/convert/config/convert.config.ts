import { runtimePaths } from '@/config/runtimePaths.config';
import { LaunchOptions } from 'puppeteer';

const convertToMB = (byte: number): number => byte * 1024 * 1024;

/**
 * Configuration constants for file conversion
 */
export const CONVERT_CONFIG = {
    UPLOAD_DIR: runtimePaths.convertUploads,
    OUTPUT_DIR: runtimePaths.convertOutputs,
    MAX_FILE_SIZE: convertToMB(15), // 15MB
    GOTENBERG_URL: process.env.GOTENBERG_URL,
    SUPPORTED_EXTENSIONS: ['.txt', '.docx', '.doc'],
    PDF_OPTIONS: {
        format: 'A4' as const,
        printBackground: true,
        margin: {
            top: '1cm',
            right: '1cm',
            bottom: '1cm',
            left: '1cm',
        },
    },
    PUPPETEER_OPTIONS: {
        headless: 'shell',
        args: ['--no-sandbox', '--disable-setuid-sandbox'],
    } as LaunchOptions,
    NETWORK_TIMEOUT: 60000,
    DEFAULT_FORMAT_CONVERT: '.pdf',
    DEFAULT_FORMAT_MIMETYPE_CONVERT: 'application/pdf',
};

export type SupportedExtension = (typeof CONVERT_CONFIG.SUPPORTED_EXTENSIONS)[number];
