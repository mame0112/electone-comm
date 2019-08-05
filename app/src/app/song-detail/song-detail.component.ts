import { Component, OnInit } from '@angular/core';

import { ActivatedRoute } from '@angular/router';
import { Location } from '@angular/common';

import { ContentData } from '../contentdata';

import { ApiService } from '../api.service';
import { DataProcessorService } from '../data-processor.service';

@Component({
  selector: 'app-song-detail',
  templateUrl: './song-detail.component.html',
  styleUrls: ['./song-detail.component.css']
})
export class SongDetailComponent implements OnInit {

    item: ContentData;

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
              this.item = this.dataProcessorService.parseJson2ContentData(param)
            }
          );

    }


    goBack(): void {
        this.location.back();
    }

}
