import { Component, OnInit } from '@angular/core';

import { ContentData } from '../contentdata';

import { ApiService } from '../api.service';

import { DataProcessorService } from '../data-processor.service'

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {

  contents: ContentData[];

  constructor(
      private apiService: ApiService,
      private dataProcessorServie: DataProcessorService) {}

  ngOnInit() {
      console.log('Dashboard onInit');
      // this.apiService.getYoutubeData().subscribe(contents => this.contents = contents);
      // this.apiService.getYoutubeData().subscribe(contents => this.contents = contents);
      // this.apiService.getYoutubeData()
      // .subscribe(
      //     function(contents) {
      //         console.log('contents fetched');
      //         // console.log(contents);
      //         this.contents = contents
      //         this.dataProcessorServie.parseJson2ContentData(contents);
      //     });
      this.apiService.getYoutubeData()
      .subscribe(param => {
              this.contents = this.dataProcessorServie.parseJson2ContentData(param)}
          );
  }

}
