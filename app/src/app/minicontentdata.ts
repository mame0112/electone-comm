export class MiniContentData {

    constructor(){
        // Nothing to do
    }

    title: string;
    description: string;
    thumb_url: string;
    video_id: string;
    publish_date: string;
    channel_title: string;


    getTitle(): string{
        return this.title;
    }

    getDescription(): string{
        return this.description;
    }

    getThumbnailUri(): string{
        return this.thumb_url;
    }

    getVideoId(): string{
        return this.video_id;
    }

    getPublishDate(): string{
        return this.publish_date;
    }

    getChannelTitle(): string{
        return this.channel_title;
    }

    setTitle(title: string): void{
        this.title = title;
    }

    setDescription(description: string): void{
        this.description = description;
    }

    setThumbnailUrl(thumb_url: string): void{
        this.thumb_url = thumb_url;
    }

    setVideoId(video_id: string): void{
        this.video_id = video_id;
    }

    setPublishDate(publish_date: string): void{
        this.publish_date = publish_date;
    }

    setChannelTitle(channel_title: string): void{
        this.channel_title = channel_title;
    }

}
