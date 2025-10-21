import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms'

interface Survey {
  id?: number;
  program_name: string;
  program_code: string;
  cal_year: number;
}

@Component({
  selector: 'app-surveys',
  standalone: true,
  imports: [CommonModule, FormsModule, HttpClientModule],
  templateUrl: './surveys.component.html',
})
export class SurveysComponent implements OnInit {
  surveys: Survey[] = [];
  newSurvey: Survey = { program_name: '', program_code: '', cal_year: new Date().getFullYear() };

  constructor(private http: HttpClient) {}

  ngOnInit(): void {
    this.loadSurveys();
  }

  loadSurveys(): void {
    this.http.get<Survey[]>('http://127.0.0.1:8000/surveys')
      .subscribe({
        next: (data) => this.surveys = data,
        error: (err) => console.error('Failed to load surveys', err)
      });
  }

  addSurvey(): void {
    this.http.post<Survey>('http://127.0.0.1:8000/surveys', this.newSurvey)
      .subscribe({
        next: (p) => {
          this.surveys.push(p);
          this.newSurvey = { program_name: '', program_code: '', cal_year: new Date().getFullYear() };
        },
        error: (err) => console.error('Failed to create survey', err)
      });
  }
}

