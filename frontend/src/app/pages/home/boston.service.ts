import {Injectable} from '@angular/core';
import {Http} from "@angular/http";
import {Observable} from "rxjs/Observable";
import 'rxjs/add/operator/map';
import {
    Price,
    ProbabilityPrediction,
    GradResult,
    GRADParameters
} from "./types";

const SERVER_URL: string = 'api/';

@Injectable()
export class BostonService {

    constructor(private http: Http) {
    }

    public trainModel(gradParameters: GRADParameters): Observable<GradResult> {
        return this.http.post(`${SERVER_URL}train`, gradParameters).map((res) => res.json());
    }

    public predictIris(p: Price): Observable<ProbabilityPrediction[]> {
        return this.http.post(`${SERVER_URL}predict`, p).map((res) => res.json());
    }
}
