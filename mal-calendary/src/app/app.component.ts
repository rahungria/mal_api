import { calcPossibleSecurityContexts } from '@angular/compiler/src/template_parser/binding_parser';
import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  pinto() {
    console.log(this.animes["Monday"])
    for (let anime of this.animes["Monday"]) {
      console.log(anime)
    }
  }
  ngOnInit() {
    this.pinto()
  }
  title = 'mal-calendary';

  animes = {
    "Monday": [
      {
        "title": "Tatoeba Last Dungeon Mae no Mura no Shounen ga Joban no Machi de Kurasu Youna Monogatari",
        "time": {
          "weekday": 0,
          "hour": 10,
          "minute": 0
        },
        "image_url": "https://cdn.myanimelist.net/images/anime/1282/106599.jpg?s=21a5c188ce7a6dc0c65eab3fc4b337f2",
        "score": 7,
        "studios": [
          "LIDENFILMS"
        ]
      },
      {
        "title": "Tatoeba Last Dungeon Mae no Mura no Shounen ga Joban no Machi de Kurasu Youna Monogatari",
        "time": {
          "weekday": 0,
          "hour": 10,
          "minute": 0
        },
        "image_url": "https://cdn.myanimelist.net/images/anime/1282/106599.jpg?s=21a5c188ce7a6dc0c65eab3fc4b337f2",
        "score": 7,
        "studios": [
          "LIDENFILMS"
        ]
      },
      {
        "title": "Tatoeba Last Dungeon Mae no Mura no Shounen ga Joban no Machi de Kurasu Youna Monogatari",
        "time": {
          "weekday": 0,
          "hour": 10,
          "minute": 0
        },
        "image_url": "https://cdn.myanimelist.net/images/anime/1282/106599.jpg?s=21a5c188ce7a6dc0c65eab3fc4b337f2",
        "score": 7,
        "studios": [
          "LIDENFILMS"
        ]
      },
      {
        "title": "Mushoku Tensei: Isekai Ittara Honki Dasu",
        "time": {
          "weekday": 0,
          "hour": 12,
          "minute": 0
        },
        "image_url": "https://cdn.myanimelist.net/images/anime/1068/111129.jpg?s=df374f49dcbec6ac3bb6a0a878d00c0c",
        "score": 9,
        "studios": [
          "Studio Bind"
        ]
      },
      {
        "title": "Shingeki no Kyojin: The Final Season",
        "time": {
          "weekday": 0,
          "hour": 12,
          "minute": 10
        },
        "image_url": "https://cdn.myanimelist.net/images/anime/1000/110531.jpg?s=95d739fe2a46e7cadb72b3879dea917b",
        "score": 10,
        "studios": [
          "MAPPA"
        ]
      },
      {
        "title": "Non Non Biyori Nonstop",
        "time": {
          "weekday": 0,
          "hour": 13,
          "minute": 35
        },
        "image_url": "https://cdn.myanimelist.net/images/anime/1159/107670.jpg?s=42d4c0f7c8b812341260cd1d5a1d1a0e",
        "score": 0,
        "studios": [
          "SILVER LINK."
        ]
      }
    ],
    "Tuesday": [
      {
        "title": "Tensei shitara Slime Datta Ken 2nd Season",
        "time": {
          "weekday": 1,
          "hour": 11,
          "minute": 0
        },
        "image_url": "https://cdn.myanimelist.net/images/anime/1271/109841.jpg?s=b92722b58ae0e9de4ac915641bdf5de1",
        "score": 9,
        "studios": [
          "8bit"
        ]
      }
    ],
    "Wednesday": [
      {
        "title": "Log Horizon: Entaku Houkai",
        "time": {
          "weekday": 2,
          "hour": 7,
          "minute": 25
        },
        "image_url": "https://cdn.myanimelist.net/images/anime/1510/108026.jpg?s=b5765939d4788c029bb2e98f12d2d6d1",
        "score": 0,
        "studios": [
          "Studio Deen"
        ]
      },
      {
        "title": "Re:Zero kara Hajimeru Isekai Seikatsu 2nd Season Part 2",
        "time": {
          "weekday": 2,
          "hour": 10,
          "minute": 30
        },
        "image_url": "https://cdn.myanimelist.net/images/anime/1132/110666.jpg?s=75738884c6a867756d6c6c175199d1de",
        "score": 10,
        "studios": [
          "White Fox"
        ]
      },
      {
        "title": "Kaifuku Jutsushi no Yarinaoshi",
        "time": {
          "weekday": 2,
          "hour": 11,
          "minute": 30
        },
        "image_url": "https://cdn.myanimelist.net/images/anime/1301/110018.jpg?s=c8cd4cb006e0b6f6a9718b9579df61ec",
        "score": 0,
        "studios": [
          "TNK"
        ]
      }
    ],
    "Thursday": [
      {
        "title": "Dr. Stone: Stone Wars",
        "time": {
          "weekday": 3,
          "hour": 10,
          "minute": 30
        },
        "image_url": "https://cdn.myanimelist.net/images/anime/1711/110614.jpg?s=51db32f980c882f08d08d06fe6279963",
        "score": 0,
        "studios": [
          "TMS Entertainment"
        ]
      },
      {
        "title": "Yuru Camp\u25b3 Season 2",
        "time": {
          "weekday": 3,
          "hour": 11,
          "minute": 0
        },
        "image_url": "https://cdn.myanimelist.net/images/anime/1255/110636.jpg?s=092742599df6b06e461bf1f290838f5d",
        "score": 0,
        "studios": [
          "C-Station"
        ]
      },
      {
        "title": "Higurashi no Naku Koro ni Gou",
        "time": {
          "weekday": 3,
          "hour": 11,
          "minute": 30
        },
        "image_url": "https://cdn.myanimelist.net/images/anime/1287/109031.jpg?s=153a2e1ce796614d779d1d5c52a35e3e",
        "score": 0,
        "studios": [
          "Passione"
        ]
      }
    ],
    "Friday": [
      {
        "title": "Kumo Desu ga, Nani ka?",
        "time": {
          "weekday": 4,
          "hour": 9,
          "minute": 30
        },
        "image_url": "https://cdn.myanimelist.net/images/anime/1609/110322.jpg?s=18645eb98c7ef9cfca8cdfbbe26705cf",
        "score": 8,
        "studios": [
          "Millepensee"
        ]
      }
    ],
    "Saturday": [
      {
        "title": "Ore dake Haireru Kakushi Dungeon",
        "time": {
          "weekday": 5,
          "hour": 14,
          "minute": 25
        },
        "image_url": "https://cdn.myanimelist.net/images/anime/1266/109120.jpg?s=06c98a3c2dd3aee6555fdbfb87b0ab6b",
        "score": 8,
        "studios": [
          "Okuruto Noboru"
        ]
      }
    ],
    "Sunday": [
      {
        "title": "Yatogame-chan Kansatsu Nikki Sansatsume",
        "time": {
          "weekday": 6,
          "hour": 9,
          "minute": 54
        },
        "image_url": "https://cdn.myanimelist.net/images/anime/1389/111080.jpg?s=3befb7927d678870f7da292d4f4b5050",
        "score": 0,
        "studios": [
          "Creators in Pack",
          "LEVELS"
        ]
      },
      {
        "title": "Kemono Jihen",
        "time": {
          "weekday": 6,
          "hour": 10,
          "minute": 0
        },
        "image_url": "https://cdn.myanimelist.net/images/anime/1258/108331.jpg?s=f293eb0eb8189afa44226e2357cd3668",
        "score": 0,
        "studios": [
          "Ajia-Do"
        ]
      }
    ]
  }
}
