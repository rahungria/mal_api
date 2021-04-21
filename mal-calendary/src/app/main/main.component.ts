import { formatCurrency } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup } from '@angular/forms';
import { Router } from '@angular/router';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {

  constructor(private router: Router) { }


  username="";

  form = new FormGroup({
    id: new FormControl('')
  });
  routeSchedule() {
    this.router.navigate(['schedule/' + this.username]);
  }
  ngOnInit(): void {
  }

}
