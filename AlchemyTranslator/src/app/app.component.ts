import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl, Validators } from '@angular/forms';
import { GoogletranslateService } from './services/googletranslate.service';
import languageList from '../assets/supported_languages.json';
import { GoogleObj } from './models/google_obj';
import { NgxSpinnerService } from 'ngx-spinner';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})
export class AppComponent implements OnInit {
  languageList: any;
  form: FormGroup;
  submitted: boolean = false;
  translatedText: string = '';
  spinnerType: string = 'ball-pulse';
  browserLanguage = navigator.language;

  constructor(
    private googleTranslate: GoogletranslateService,
    private spinnerService: NgxSpinnerService
  ) {
    this.form = new FormGroup({
      to: new FormControl('', [Validators.required]),
      from: new FormControl('', [Validators.required]),
      text: new FormControl('', [
        Validators.required,
        Validators.maxLength(255),
      ]),
    });

    this.languageList = languageList.languages;
  }

  ngOnInit(): void {
    this.setUserLanguage(this.browserLanguage);
  }

  private setUserLanguage(language: string): void {
    const aux = language.split('-');
    const userLanguage = aux[0];
    this.form.get('from')?.setValue(userLanguage);
  }

  title = 'AlchemyTranslator';
  text: string = '';
  fromLanguage: string = '';
  toLanguage: string = '';

  public getFromLanguage(event: any) {
    this.fromLanguage = (event.target as HTMLInputElement)?.value;
  }

  public getToLanguage(event: any) {
    this.toLanguage = (event.target as HTMLInputElement)?.value;
  }

  onSubmit(): void {
    this.submitted = true;

    if (this.form.invalid) {
      return;
    }

    const googleObj: GoogleObj = {
      q: this.form.get('text')?.value,
      source: this.form.get('from')?.value,
      target: this.form.get('to')?.value,
    };

    this.doTranslation(googleObj);
  }

  doTranslation(googleObj: GoogleObj) {
    this.spinnerService.show();

    this.googleTranslate.translate(googleObj).subscribe({
      next: (response: any) => {
        this.translatedText = response.data.translations[0].translatedText;
      },
      error: (err) => {
        console.log(err);
      },
      complete: () => {
        this.spinnerService.hide();
      },
    });
  }

  onReset(): void {
    this.submitted = false;
    this.form.reset();
    this.form.get('from')?.setValue('');
    this.form.get('to')?.setValue('');
  }
}
