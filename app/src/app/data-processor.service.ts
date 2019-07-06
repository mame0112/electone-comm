import { Injectable } from '@angular/core';

import { ContentData } from './contentdata';
import { ContentDataBuilder } from './contentdata-builder';

@Injectable({
  providedIn: 'root'
})
export class DataProcessorService {

  constructor() { }

  // contentsData: ContentsData;

  parseJson2ContentData(jsonobj: any): ContentData[] {
      console.log('parseJson2ContentData')

      var contents: ContentData[] = [];

      // this.contentsData = jsonobj.contents;

      for (var i=0; i<Object.keys(jsonobj.contents).length; i++){

          var content: ContentData = jsonobj.contents[i];
          console.log(content.title);
          contents.push(content);
       }

       return contents;
 
  }

  stringifyContentData2Json(): void {

  }

}

