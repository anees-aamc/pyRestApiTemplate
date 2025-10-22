import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms'

interface SurveyType {
  survey_type_cd: string;
  survey_type_desc: string;
}

@Component({
  selector: 'app-surveys',
  standalone: true,
  imports: [CommonModule, FormsModule, HttpClientModule],
  templateUrl: './survey_types.component.html',
})
export class SurveyTypesComponent implements OnInit {
  surveyTypes: SurveyType[] = [];
  newSurveyType: SurveyType = {
    survey_type_cd: '',
    survey_type_desc: '',
  };

  constructor(private http: HttpClient) {}

  ngOnInit(): void {
    this.loadSurveyTypes();
  }

  loadSurveyTypes(): void {
    this.http.get<SurveyType[]>('http://127.0.0.1:8000/survey_types')
      .subscribe({
        next: (data) => this.surveyTypes = data,
        error: (err) => console.error('Failed to load survey_types', err)
      });
  }

  addSurveyType(): void {
    this.http.post<SurveyType>('http://127.0.0.1:8000/survey_types', this.newSurveyType)
      .subscribe({
        next: (p) => {
          this.surveyTypes.push(p);
          this.newSurveyType = {
            survey_type_cd: '',
            survey_type_desc: '',
          };
        },
        error: (err) => console.error('Failed to create survey_types', err)
      });
  }
}

