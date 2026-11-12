import { YouTubePlayer } from 'react-youtube';
import MediaPlayerController from '../MediaPlayerController';

export class YoutubePlayerAdapter implements MediaPlayerController {
    private readonly player: YouTubePlayer;
    constructor(player: YouTubePlayer) {
        this.player = player;
    }

    seekTo(seconds: number): void {
        this.player.seekTo(seconds, true);
        this.player.playVideo();
    }

    play(): void {
        this.player.playVideo();
    }

    getCurrentTime(): number {
        // The ready event supplies the raw synchronous IFrame player. The
        // library's facade type instead describes an asynchronous wrapper.
        const currentTime: unknown = this.player.getCurrentTime();
        if (typeof currentTime !== 'number') {
            throw new TypeError('YoutubePlayerAdapter requires the ready IFrame player');
        }
        return currentTime || 0;
    }
}
