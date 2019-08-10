import { Injectable } from '@angular/core';

import { ContentData } from './contentdata';
import { ContentDataBuilder } from './contentdata-builder';
import { MiniContentDataBuilder } from './minicontentdata-builder';

import { MiniContentData } from './minicontentdata';

import { FieldConstants } from './field-constants';

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
      console.log('parseJson2ContentData');
      console.log(jsonObj);

      // Get sub item
      var subItemsJsonArray = JSON.parse(jsonObj.contents);
      console.log("subItemsJsonArray: ");
      console.log(subItemsJsonArray);

        // var item = jsonObj['contents'];

      //Create MiniContentsData array
      var miniContentsData: MiniContentData[];
      miniContentsData = [];

      for(let i in subItemsJsonArray){
        var item = subItemsJsonArray[i];
        var miniBuilder = new MiniContentDataBuilder();
        miniBuilder.setVideoId(item[FieldConstants.CONTENTS_VIDEO_ID]).setTitle(item[FieldConstants.CONTENTS_TITLE]).setDescription(item[FieldConstants.CONTENTS_DESCRIPTION]).setPublishDate(item[FieldConstants.CONTENTS_PUBLISH_DATE]).setThumbnailUrl(item[FieldConstants.CONTENTS_THUMB_URL]).setChannelTitle(item[FieldConstants.CONTENTS_CHANNEL_TITLE]);
        miniContentsData.push(miniBuilder.getResult());
      }

      var builder = new ContentDataBuilder();
      builder.setSongId(jsonObj['song_id']).setTitle(jsonObj['title']).setDescription(jsonObj['description']).setPublishDate(jsonObj['publish_date']).setThumbnailUrl(jsonObj['thumb_url']).setChannelTitle(jsonObj['channel_title']).setVideoId(jsonObj['video_id']).setDifficulty(jsonObj['diff']).setConcert(jsonObj['concert']).setFamous(jsonObj['famous']).setContents(miniContentsData);

      return builder.getResult()
  }


  parseJson2MiniContentsData(jsonobj: any): MiniContentData[] {
      console.log('parseJson2MiniContentsData')
      console.log(jsonobj)
      console.log(jsonobj.contents)

      var contents: MiniContentData[] = [];

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

