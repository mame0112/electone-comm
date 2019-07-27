import { Component, OnInit } from '@angular/core';

import { ApiService } from '../api.service';

@Component({
  selector: 'app-search-panel',
  templateUrl: './search-panel.component.html',
  styleUrls: ['./search-panel.component.css']
})
export class SearchPanelComponent implements OnInit {

    difficulty = 1;
    concert = 1;
    famous = 1;

    properties = {
        'difficulty': this.difficulty,
        'concert': this.concert,
        'famous': this.famous
    }


    constructor(private apiService: ApiService) { }

    ngOnInit() {
    }

    onSearchClicked(): void {
        console.log('onSearchClicked')

        this.properties.difficulty = this.difficulty;
        this.properties.concert = this.concert;
        this.properties.famous = this.famous;

        console.log(this.properties)

        this.apiService.searchContentByProperties(JSON.stringify(this.properties))
        .subscribe(param => console.log(param));


    }

}