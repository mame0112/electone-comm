import { Component, OnInit } from '@angular/core';

import { ActivatedRoute } from '@angular/router';
import { Location } from '@angular/common';

import { ContentData } from '../contentdata';
import { MiniContentData } from '../minicontentdata';

import { ApiService } from '../api.service';
import { DataProcessorService } from '../data-processor.service';

@Component({
  selector: 'app-song-detail',
  templateUrl: './song-detail.component.html',
  styleUrls: ['./song-detail.component.css']
})
export class SongDetailComponent implements OnInit {

    item: ContentData;
    subItems: MiniContentData[];

    constructor(
        private route: ActivatedRoute,
        private location: Location,
        private apiService: ApiService,
        private dataProcessorService: DataProcessorService
    ) { }

    ngOnInit() {
        this.getSong();
    }

    getSong(): void {
        console.log("getSong");

        const id = this.route.snapshot.paramMap.get('song_id');

        this.apiService.getSongContents(id).subscribe(param => {
              this.item = this.dataProcessorService.parseJson2ContentData(param);
              this.subItems = this.item.contents;
              // console.log("item");
              // console.log(this.item.title);
              // console.log(this.item.contents[0].title);
              // console.log(this.item.contents);
              // this.subItems = JSON.parse(this.item.contents);
              // this.createSubItemContents(JSON.parse(this.item.contents));
            }
          );

    }


    // createSubItemContents(jsonArray: any): void{
    //   console.log("createSubItemContents");

    //   for(let i in jsonArray){
    //     console.log(jsonArray[i]);
    //     var item = jsonArray[i];

    //     // this.subItems[i] = builder.getResult();
    //     this.subItems.push(builder.getResult());
    //   }

    //  }


    goBack(): void {
        this.location.back();
    }

}
