export class ContentData {

    constructor(){
        // Nothing to do
    }


    song_id: string;
    title: string;
    description: string;
    publish_date: number;
    thumb_url: string;
    channel_title: string;
    video_id: string;
    difficulty: number;
    famous: number;
    concert: number;
    contents: string;

    get_song_id(): string{
        return this.song_id;
    }

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

    getVideoId(): string{
        return this.video_id;
    }

    getDifficulty(): number{
        return this.difficulty;
    }

    getFamous(): number{
        return this.famous;
    }

    getConcert(): number{
        return this.concert;
    }

    setSongId(song_id: string): void{
        this.song_id = song_id;
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

    setVideoId(video_id: string): void{
        this.video_id = video_id;
    }

    setDifficulty(difficulty: number): void{
        this.difficulty = difficulty;
    }

    setFamous(famous: number): void{
        this.famous = famous;
    }

    setConcert(concert: number): void{
        this.concert = concert;
    }

    setContents(contents: string): void{
        this.contents = contents;
    }


}
