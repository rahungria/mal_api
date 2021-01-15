import { Component, Input, OnInit } from '@angular/core';

@Component({
  selector: 'app-anime-card',
  templateUrl: './anime-card.component.html',
  styleUrls: ['./anime-card.component.css']
})
export class AnimeCardComponent implements OnInit {

  constructor() { }
  @Input() anime: JSON;
  ngOnInit(): void {
  }

}
