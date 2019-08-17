import { Component, OnInit } from '@angular/core';

import { ActivatedRoute } from '@angular/router';
import { Location } from '@angular/common';

import { ContentData } from '../contentdata';
import { MiniContentData } from '../minicontentdata';

import { ApiService } from '../api.service';
import { DataProcessorService } from '../data-processor.service';
import { GaService } from '../ga.service';

import { Constants } from '../constants';

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
        private dataProcessorService: DataProcessorService,
        private gaService: GaService
    ) { }

    ngOnInit() {
        this.getSong();
        this.gaService.sendPageView(Constants.GA_VIEW_DETAIL);
    }

    getSong(): void {
        console.log("getSong");

        const id = this.route.snapshot.paramMap.get('song_id');

        this.apiService.getSongContents(id).subscribe(param => {
              this.item = this.dataProcessorService.parseJson2ContentData(param);
              this.subItems = this.item.contents;

            }
          );
    }

    goBack(): void {
        this.location.back();
    }

    simplifyTimeformat(time: string): string {
      if (time != null){
        return time.substr(0, Constants.TIME_FORMAT_LENGTH);
      }

    }

}
