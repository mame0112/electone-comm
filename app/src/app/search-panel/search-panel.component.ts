import { Component, OnInit } from '@angular/core';

import { FormsModule } from '@angular/forms';

import { ApiService } from '../api.service';
import { DataProcessorService } from '../data-processor.service';

import { MiniContentData } from '../minicontentdata';

import { SearchPropertyProcessor } from './search-commandprocessor';

import { Difficulties } from './search-commandprocessor';
import { Concert } from './search-commandprocessor';
import { Famous } from './search-commandprocessor';

@Component({
  selector: 'app-search-panel',
  templateUrl: './search-panel.component.html',
  styleUrls: ['./search-panel.component.css']
})
export class SearchPanelComponent implements OnInit {

    public isCollapsed = false;

    // For 
    difficulty = 1;
    concert = 1;
    famous = 1;

    // For Default value of rank
    difficulty_rank = Difficulties.Easy;
    concert_rank = Concert.Best;
    famous_rank = Famous.Famous;

    // For rank UI
    difficulty_ranks = Difficulties;
    concert_ranks = Concert;
    famous_ranks = Famous;

    processor = new SearchPropertyProcessor();


    properties = {
        'difficulty': this.difficulty,
        'concert': this.concert,
        'famous': this.famous
    }

    contents: MiniContentData[];


    constructor(private apiService: ApiService,
        private dataProcessorService: DataProcessorService) { }

    ngOnInit() {
    }

    onSearchClicked(): void {
        console.log('onSearchClicked')

        // this.properties.difficulty = this.difficulty;
        // this.properties.concert = this.concert;
        // this.properties.famous = this.famous;


        //TODO 
        this.properties = this.processor.transcodePropertyRanksToValues(this.difficulty_rank, this.concert_rank, this.famous_rank);

        console.log(this.properties);

        this.apiService.searchContentByProperties(JSON.stringify(this.properties))
        .subscribe(results => this.contents = this.dataProcessorService.parseJson2MiniContentsData(results));

    }

    difficulty_values() : Array<string> {
        var values = Object.values(this.difficulty_ranks);
        return values;
    }

    concert_values() : Array<string> {
        var values = Object.values(this.concert_ranks);
        return values;
    }

    famous_values() : Array<string> {
        var values = Object.values(this.famous_ranks);
        return values;
    }

}
