import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { GoogleObj } from '../models/google_obj';
import { environment } from '../environment/environment';

@Injectable({
  providedIn: 'root',
})
export class GoogletranslateService {
  url = 'https://translation.googleapis.com/language/translate/v2?key=';
  key = environment.apiKey;

  constructor(private http: HttpClient) {}
  translate(obj: GoogleObj) {
    return this.http.post(this.url + this.key, obj);
  }
}
