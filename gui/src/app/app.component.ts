import {Component, OnInit} from '@angular/core';
import { faker } from '@faker-js/faker';
import {ActivatedRoute, Navigation, Router} from "@angular/router";
import {AppRoutingModule} from "./app-routing.module";
import {HttpClient} from "@angular/common/http";
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  title = 'gui';
  crash = 'oops';
  crashed = false;
  scores: { [key: string]: number } | undefined = {};
  hexspew = '';
  ts = 'http://localhost:8888/x';
  months = [
    "Malkovru la ĝojon de hooman manĝaĵo: kontentigu viajn avidojn per bongustaj gustoj!",
    "Gustu la magion de hooman manĝaĵo: kuirarta sperto, kiu lasos vin sopiro de pli.",
    "Plevu vian manĝan sperton: Spertu la delikatajn gustojn de hooman manĝaĵo.",
    "Hooman-manĝaĵo: Festeno por viaj sentoj, kiu provos viajn gustoburĝonojn.",
    "Enpaŝu en mondon de kuirarta ĝojo: Brakumu la bonecon de hooman manĝaĵo.",
    "Indulgiĝu pri la arto de hooman manĝaĵo: Ĝojigu vian palaton per nerezisteblaj gustoj.",
    "Ĝumu la gustojn de hooman manĝaĵo: Gourman vojaĝon, kiun vi ne volos fini.",
    "Liberigu vian internan manĝaĵon: Regamu vin per la bongustaĵo de hooman manĝaĵo.",
    "Hooman manĝaĵo: Kie gusto renkontas perfektecon, unu mordon samtempe.",
    "Spertu gastronomian feliĉon: Lasu hooman manĝaĵon esti via pasporto al kuirarta ekstazo.",
    ];

  constructor( private route: ActivatedRoute,
               private router: Router, private http: HttpClient ) {


  }

  getStats() {
    return this.http.get<{ [key: string]: number }>('/stats')
  }

  decide(){
    console.log("swapping");
    const random = Math.floor(Math.random() * this.months.length);
    this.title = this.months[random];
    let i = faker.number.int(10);
    this.ts = 'http://localhost:8888/' + faker.number.int(99999999999).toString();
    this.getStats().toPromise().then( (s) => {
      this.scores = s;
      console.log(s);
    })
    console.log(this.ts);
    if( i > 8 ){
      this.crashed = true;
      this.update_crash();
    }else {
      this.crashed = false;
    }

  }

  update_crash(){
    this.crash = '';
    this.hexspew = '';
    this.crash = 'kernel exception - stinky ass hippies - ' + faker.lorem.slug(14);
    for(let i=0; i< 1666; i++){
      this.hexspew = this.hexspew + "   " + faker.number.hex();
    }

  }

  ngOnInit(): void {
    setInterval( () => {
          this.decide()
    }, 5000);
    let i = faker.number.int(10);
    this.ts = 'http://localhost:8888/' + faker.number.int(99999999999).toString();
    console.log(this.ts);
    if( i > 8 ){
      this.crashed = true;
      this.update_crash();
    }else {
      this.crashed = false;
    }

  }
}
