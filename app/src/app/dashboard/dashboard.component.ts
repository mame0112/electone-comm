import { Component, OnInit } from '@angular/core';

import { Constants } from '../constants';

import { ContentData } from '../contentdata';

import { ApiService } from '../api.service';
import { DataProcessorService } from '../data-processor.service';

import { GaService } from '../ga.service';


import { NgbModule } from '@ng-bootstrap/ng-bootstrap' ; 

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {

  contents: ContentData[];

  constructor(
      private apiService: ApiService,
      private dataProcessorServie: DataProcessorService,
      private gaService: GaService) {}

  ngOnInit() {
      console.log('Dashboard onInit');

      this.gaService.sendPageView(Constants.GA_VIEW_DASHBOARD);


      this.apiService.getRecommendContents()
      .subscribe(params => this.contents = this.dataProcessorServie.parseJson2ContentsData(params));


      // TODO
      // this.apiService.getYoutubeData()
      // .subscribe(param => {
      //         this.contents = this.dataProcessorServie.parseJson2ContentsData(param)}

              // TEMPORARY


          // );

      // TEMPORARY
      // this.apiService.savePropertyData()
      // .subscribe(param => console.log(param));

  }


}
