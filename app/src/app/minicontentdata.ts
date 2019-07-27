export class MiniContentData {

    constructor(){
        // Nothing to do
    }

    title: string;
    description: string;
    thumbnail_uri: string;
    video_id: number;


    getTitle(): string{
        return this.title;
    }

    getDescription(): string{
        return this.description;
    }

    getThumbnailUri(): string{
        return this.thumbnail_uri;
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

    setThumbnailUri(thumbnail_uri: string): void{
        this.thumbnail_uri = thumbnail_uri;
    }

    setVideoId(video_id: number): void{
        this.video_id = video_id;
    }

}
