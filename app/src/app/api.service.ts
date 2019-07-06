import { Injectable } from '@angular/core';

import { HttpClientModule }    from '@angular/common/http';
import { HttpClient, HttpHeaders } from '@angular/common/http';

import { Observable, of } from 'rxjs';
import { catchError, map, tap } from 'rxjs/operators';

import { ContentData } from './contentdata';

@Injectable({
  providedIn: 'root'
})

export class ApiService {

    private url = 'youtube';

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
        return this.http.get<string>(this.url)
        .pipe(
            tap(heroes => console.log('fetched heroes')),
            catchError(this.handleError<string>('getHeroes', 'Error'))
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
