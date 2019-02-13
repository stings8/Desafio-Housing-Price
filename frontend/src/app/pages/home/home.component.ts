import {Component, OnInit} from '@angular/core';
import {BostonService} from "./boston.service";
import {
    Price,
    ProbabilityPrediction,
     GradResult,
    GRADParameters,
    GRADResult,

} from "./types";

@Component({
    selector: 'home',
    templateUrl: './home.component.html',
    styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {

    public gradResult: GradResult;
    public Boston: Price = new Price();
    public probabilityPredictions: ProbabilityPrediction[];

    // graph styling
    public colorScheme = {
        domain: ['#1a242c', '#e81746', '#e67303', '#f0f0f0']
    };

    constructor(private irisService: BostonService) {
    }

    ngOnInit() {
    }



    public predictPrice() {
        this.irisService.predictIris(this.Boston).subscribe((probabilityPredictions) => {
            this.probabilityPredictions = probabilityPredictions;
        });
    }

}
