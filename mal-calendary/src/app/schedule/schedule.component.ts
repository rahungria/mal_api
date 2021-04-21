import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import * as $ from 'jquery';

@Component({
  selector: 'app-schedule',
  templateUrl: './schedule.component.html',
  styleUrls: ['./schedule.component.css']
})
export class ScheduleComponent {

  constructor(private router: Router, private http: HttpClient, private activatedRoute: ActivatedRoute) {

  }
  API_URI = "http://127.0.0.1:5000";
  username = "";
  animes;
  ngOnInit() {
    var differenceHoursLocalJapan = (540+new Date().getTimezoneOffset())/60;
    var localTimeSign = (differenceHoursLocalJapan<0) ? "negative" : "positive";
    this.username = this.activatedRoute.snapshot.paramMap.get("username");
    console.log(`${this.API_URI}/${this.username}/${differenceHoursLocalJapan}/${localTimeSign}`);
    this.http.get(`${this.API_URI}/${this.username}/${differenceHoursLocalJapan}/${localTimeSign}`,).subscribe(
      res => {
        this.animes = res;

        console.log(this.animes);
      });
  }
  home() {
    this.router.navigate(['']);
  }

  title = 'mal-calendary';



}
