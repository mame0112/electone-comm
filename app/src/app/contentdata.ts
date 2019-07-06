export class ContentData {

    constructor(){
        // Nothing to do
    }

    title: string;
    description: string;
    publish_date: number;
    thumbnail_uri: string;
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

    getThumbnailUri(): string{
        return this.thumbnail_uri;
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

    setThumbnailUri(thumbnail_uri: string): void{
        this.thumbnail_uri = thumbnail_uri;
    }

    setChannelTitle(channel_title: string): void{
        this.channel_title = channel_title;
    }

    setVideoId(video_id: number): void{
        this.video_id = video_id;
    }

}
