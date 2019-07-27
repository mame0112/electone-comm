import { Component, OnInit } from '@angular/core';

import { ApiService } from '../api.service';

@Component({
  selector: 'app-search-panel',
  templateUrl: './search-panel.component.html',
  styleUrls: ['./search-panel.component.css']
})
export class SearchPanelComponent implements OnInit {

    difficulty = 0;
    concert = 0;
    famous = 0;


    constructor(private apiService: ApiService) { }

    ngOnInit() {
    }

    onSearchClicked(): void {
        console.log('onSearchClicked')
        console.log(this.difficulty)
        console.log(this.concert)
        console.log(this.famous)
    }

}
