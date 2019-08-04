import { ContentData } from './contentdata';

export class ContentDataBuilder {

    content: ContentData = new ContentData();

    constructor(){
        // Nothing to do
    }


    setSongId(song_id: string): ContentDataBuilder{
        this.content.setSongId(song_id);
        return this;
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

    setThumbnailUrl(thumb_url: string): ContentDataBuilder{
        this.content.setThumbnailUrl(thumb_url);
        return this;
    }

    setChannelTitle(channel_title: string): ContentDataBuilder{
        this.content.setChannelTitle(channel_title);
        return this;
    }

    setVideoId(video_id: string): ContentDataBuilder{
        this.content.setVideoId(video_id);
        return this;
    }

    getResult(): ContentData {
        return this.content;
    }

    setDifficulty(difficulty: number): ContentDataBuilder{
        this.content.setDifficulty(difficulty);
        return this;
    }

    setFamous(famous: number): ContentDataBuilder{
        this.content.setFamous(famous);
        return this;
    }

    setConcert(concert: number): ContentDataBuilder{
        this.content.setConcert(concert);
        return this;
    }


}