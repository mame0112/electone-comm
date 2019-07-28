export class ContentData {

    constructor(){
        // Nothing to do
    }

    title: string;
    description: string;
    publish_date: number;
    thumb_url: string;
    channel_title: string;
    video_id: number;


    getTitle(): string{
        return this.title;
    }

    getDescription(): string{
        return this.description;
    }

    getPublishDate(): number{
        return this.publish_date;
    }

    getThumbnailUrl(): string{
        return this.thumb_url;
    }

    getChannelTitle(): string{
        return this.channel_title;
    }

    getVideoId(): number{
        return this.video_id;
    }

    setTitle(title: string): void{
        this.title = title;
    }

    setDescription(description: string): void{
        this.description = description;
    }

    setPublishDate(publish_date: number): void{
        this.publish_date = publish_date;
    }

    setThumbnailUrl(thumb_url: string): void{
        this.thumb_url = thumb_url;
    }

    setChannelTitle(channel_title: string): void{
        this.channel_title = channel_title;
    }

    setVideoId(video_id: number): void{
        this.video_id = video_id;
    }

}
