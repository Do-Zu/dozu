const fs = require('fs');
const path = require('path');
const { execFileSync } = require('child_process');

// Define paths
const distDir = path.join(__dirname, '../dist-lambda');
const finalZipPath = path.join(distDir, 'function.zip');

// Make sure the bundle exists
if (!fs.existsSync(path.join(distDir, 'index.js'))) {
  console.error('Lambda bundle not found. Run npm run lambda:build first.');
  process.exit(1);
}

// Create zip file
console.log('Creating ZIP file...');
if (fs.existsSync(finalZipPath)) {
  fs.unlinkSync(finalZipPath);
}

try {
  if (process.platform === 'win32') {
    execFileSync('powershell.exe', ['-NoProfile', '-NonInteractive', '-Command',
      'Compress-Archive -LiteralPath (Get-ChildItem -LiteralPath $env:DOZU_LAMBDA_DIST).FullName -DestinationPath $env:DOZU_LAMBDA_ZIP -Force'],
    { stdio: 'inherit', windowsHide: true, env: { ...process.env,
      DOZU_LAMBDA_DIST: distDir, DOZU_LAMBDA_ZIP: finalZipPath } });
  } else {
    execFileSync('zip', ['-r', 'function.zip', '.', '-x', 'function.zip'],
      { cwd: distDir, stdio: 'inherit' });
  }
  console.log(`Lambda package created at ${finalZipPath}`);
} catch (error) {
  console.error('Error creating ZIP file:', error);
  process.exit(1);
}
