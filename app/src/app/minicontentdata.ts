export class MiniContentData {

    constructor(){
        // Nothing to do
    }

    title: string;
    description: string;
    thumb_url: string;
    video_id: number;


    getTitle(): string{
        return this.title;
    }

    getDescription(): string{
        return this.description;
    }

    getThumbnailUri(): string{
        return this.thumb_url;
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

    setThumbnailUri(thumb_url: string): void{
        this.thumb_url = thumb_url;
    }

    setVideoId(video_id: number): void{
        this.video_id = video_id;
    }

}
