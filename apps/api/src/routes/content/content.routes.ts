import express from 'express';
import { registerRoute } from '../register.routes';
import { globalAsyncHandler } from '@/middleware/handler/handler.v2';
import { authMiddleware } from '@/middleware/auth.middleware';
import { youtubeContentController } from '@/controllers/content/youtube/youtube.controller';

const router = express.Router();

// Apply global async handler
globalAsyncHandler(router);

router.use(authMiddleware);

// Define routes
router.get('/youtube/transcript', youtubeContentController.getTranscript);

// Register the router
registerRoute('/content', router, {
    description: 'Content API endpoints',
    version: 'v1',
    isEnabled: true,
});

export default router;
