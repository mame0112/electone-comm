import { Injectable } from '@angular/core';

import { HttpClientModule }    from '@angular/common/http';
import { HttpClient, HttpHeaders } from '@angular/common/http';

import { Observable, of } from 'rxjs';
import { catchError, map, tap } from 'rxjs/operators';

import { ContentData } from './contentdata';

import { Constants } from './constants'

@Injectable({
  providedIn: 'root'
})

export class ApiService {

    // private url = 'youtube';
    // private props_url = 'props';

    constructor(private http: HttpClient) { }

    // getYoutubeData(): Observable<ContentData> {
    //     console.log("getYoutubeData")
    //     // return this.http.get(this.url)
    //     return this.http.get<ContentData>(this.url)
    //     .pipe(
    //         tap(datas => console.log("YouTube data fetched")),
    //         catchError(this.handleError<ContentData>('Error occured'))
    //         );
    // }

    // getYoutubeData(): void {
    //     console.log("getYoutubeData")
    //     // return this.http.get<ContentData[]>(this.url)
    //     this.http.get(this.url).subscribe(response => {
    //         console.log(response);
    //         // console.log(response['foo']);
    //     });
    // }

    getYoutubeData(): Observable<string> {
        return this.http.get<string>(Constants.url_contents)
        .pipe(
            tap(heroes => console.log('fetched heroes')),
            catchError(this.handleError<string>('getYoutubeData', 'Error'))
            );

    }

    getSongContents(song_id: string): Observable<string> {
        const url = `${Constants.url_contents}/${song_id}`;
        return this.http.get<string>(url)
        .pipe(
            tap(heroes => console.log('getSongContents')),
            catchError(this.handleError<string>('getSongContents', 'Error'))
            );

    }

    savePropertyData(): Observable<string> {
        return this.http.get<string>(Constants.props_url_tmp)
        .pipe(
            tap(props => console.log('savePropertyData')),
            catchError(this.handleError<string>('savePropertyData', 'Error'))
            );
    }

    searchContentByProperties(properties: string): Observable<string> {
        console.log('searchContentByProperties')
        const url = `${Constants.props_url}/${properties}`;
        return this.http.get<string>(url)
        .pipe(
            tap(props => console.log('searchContentByProperties fetched')),
            catchError(this.handleError<string>('savePropertyData', 'Error'))
            );
    }

    // Recommend
    getRecommendContents(): Observable<string> {
        console.log('getRecommendContents')
        return this.http.get<string>(Constants.url_recommends)
        .pipe(
            tap(props => console.log('getRecommendContents fetched')),
            catchError(this.handleError<string>('savePropertyData', 'Error'))
            );
    }


    private handleError<T> (operation = 'operation', result?: T) {
        // console.error('Error ocurred');
        return (error: any): Observable<T> => {

        console.error(error);
        console.log(`${operation} failed: ${error.message}`);
        return of(result as T);
        };
    }

}
