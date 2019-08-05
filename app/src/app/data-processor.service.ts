import { Injectable } from '@angular/core';

import { ContentData } from './contentdata';
import { ContentDataBuilder } from './contentdata-builder';

import { MiniContentData } from './minicontentdata';


@Injectable({
  providedIn: 'root'
})
export class DataProcessorService {

  constructor() { }

  // contentsData: ContentsData;

  parseJson2ContentsData(jsonobj: any): ContentData[] {
      console.log('parseJson2ContentsData')

      var contents: ContentData[] = [];

      // this.contentsData = jsonobj.contents;

      if(jsonobj.contents !== undefined) {
          for (var i=0; i<Object.keys(jsonobj.contents).length; i++){

              var content: ContentData = jsonobj.contents[i];
              console.log(content.thumb_url);
              contents.push(content);
           }
      }

       return contents;
 
  }

  parseJson2ContentData(jsonObj: any): ContentData {
      console.log('parseJson2ContentData')      
      console.log(jsonObj)

      var builder = new ContentDataBuilder();
      builder.setSongId(jsonObj['song_id']).setTitle(jsonObj['title']).setDescription(jsonObj['description']).setPublishDate(jsonObj['publish_date']).setThumbnailUrl(jsonObj['thumb_url']).setChannelTitle(jsonObj['channel_title']).setVideoId(jsonObj['video_id']).setDifficulty(jsonObj['diff']).setConcert(jsonObj['concert']).setFamous(jsonObj['famous']).setContents(jsonObj['contents']);

      return builder.getResult()
  }


  parseJson2MiniContentsData(jsonobj: any): MiniContentData[] {
      console.log('parseJson2MiniContentsData')
      console.log(jsonobj)
      console.log(jsonobj.contents)

      var contents: MiniContentData[] = [];

      // this.contentsData = jsonobj.contents;

      if(jsonobj.contents !== undefined) {
          for (var i=0; i<Object.keys(jsonobj.contents).length; i++){

              var content: MiniContentData = jsonobj.contents[i];
              console.log(content.title);
              contents.push(content);
           }
      }

       return contents;
 
  }


  stringifyContentData2Json(): void {

  }

}

