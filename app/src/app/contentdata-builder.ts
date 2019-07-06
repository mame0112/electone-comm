import { ContentData } from './contentdata';

export class ContentDataBuilder {

    content: ContentData = new ContentData();

    constructor(){
        // Nothing to do
    }

    setTitle(title: string): ContentDataBuilder{
        this.content.setTitle(title);
        return this;
    }

    setDescription(description: string): ContentDataBuilder{
        this.content.setDescription(description);
        return this;
    }

    setPublishDate(publish_date: number): ContentDataBuilder{
        this.content.setPublishDate(publish_date);
        return this;
    }

    setThumbnailUri(thumbnail_uri: string): ContentDataBuilder{
        this.content.setThumbnailUri(thumbnail_uri);
        return this;
    }

    setChannelTitle(channel_title: string): ContentDataBuilder{
        this.content.setChannelTitle(channel_title);
        return this;
    }

    setVideoId(video_id: number): ContentDataBuilder{
        this.content.setVideoId(video_id);
        return this;
    }

    getResult(): ContentData {
        return this.content;
    }


}