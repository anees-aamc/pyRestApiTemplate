import { Routes } from '@angular/router';
import { ProgramsComponent } from './components/programs/programs.component';
import { SurveysComponent } from './components/surveys/surveys.component';
import { DashboardComponent } from './components/dashboard/dashboard.component';

export const routes: Routes = [
	{ path: 'programs', component: ProgramsComponent },
	{ path: 'surveys', component: SurveysComponent },
	{ path: '', component: DashboardComponent, pathMatch: 'full' },
	{ path: 'dashboard', component: DashboardComponent },
	// fallback: redirect unknown paths to dashboard
	{ path: '**', redirectTo: '' }
];
