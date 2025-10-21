import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ProgramsComponent } from '../programs/programs.component';
import { SurveysComponent } from '../surveys/surveys.component';

@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [CommonModule, ProgramsComponent, SurveysComponent],
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent {}

