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
        return this.http.get<string>(Constants.url)
        .pipe(
            tap(heroes => console.log('fetched heroes')),
            catchError(this.handleError<string>('getYoutubeData', 'Error'))
            );

    }

    getCategoryContents(category_id: string): Observable<string> {
        const url = `${Constants.url}/${category_id}`;
        return this.http.get<string>(Constants.url)
        .pipe(
            tap(heroes => console.log('getCategoryContents')),
            catchError(this.handleError<string>('getCategoryContents', 'Error'))
            );

    }

    savePropertyData(): Observable<string> {
        return this.http.get<string>(Constants.props_url)
        .pipe(
            tap(props => console.log('savePropertyData')),
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
