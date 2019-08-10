import { MiniContentData } from './minicontentdata';

export class MiniContentDataBuilder {

    content: MiniContentData = new MiniContentData();

    constructor(){
        // Nothing to do
    }


    setVideoId(video_id: string): MiniContentDataBuilder{
        this.content.setVideoId(video_id);
        return this;
    }

    setTitle(title: string): MiniContentDataBuilder{
        this.content.setTitle(title);
        return this;
    }

    setDescription(description: string): MiniContentDataBuilder{
        this.content.setDescription(description);
        return this;
    }

    setPublishDate(publish_date: string): MiniContentDataBuilder{
        this.content.setPublishDate(publish_date);
        return this;
    }

    setThumbnailUrl(thumb_url: string): MiniContentDataBuilder{
        this.content.setThumbnailUrl(thumb_url);
        return this;
    }

    setChannelTitle(channel_title: string): MiniContentDataBuilder{
        this.content.setChannelTitle(channel_title);
        return this;
    }

    getResult(): MiniContentData {
        return this.content;
    }

}