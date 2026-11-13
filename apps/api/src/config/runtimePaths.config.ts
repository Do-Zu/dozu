import path from 'node:path';

// Desktop supervision supplies an absolute per-user directory before startup.
// Retain cwd-based storage for existing website deployments.
const configuredDataDir = process.env.DOZU_DATA_DIR;
if (configuredDataDir && !path.isAbsolute(configuredDataDir)) {
    throw new Error('DOZU_DATA_DIR must be an absolute writable directory');
}

export const dataDir = configuredDataDir || process.cwd();
export const resolveDataPath = (configuredPath: string | undefined, fallback: string): string =>
    path.resolve(dataDir, configuredPath || fallback);

export const runtimePaths = {
    logs: resolveDataPath(process.env.LOG_DIR, 'logs'),
    uploads: resolveDataPath(process.env.UPLOAD_DIR, 'uploads'),
    convertUploads: resolveDataPath(process.env.UPLOAD_CONVERT_FILE_DIR, 'uploads/convert'),
    convertOutputs: resolveDataPath(process.env.OUTPUT_CONVERT_FILE_DIR, 'outputs/convert'),
};
