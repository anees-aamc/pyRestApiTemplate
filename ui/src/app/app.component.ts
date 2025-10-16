import { Component } from '@angular/core';
import { ProgramsComponent } from './components/programs/programs.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [ProgramsComponent],
  template: `<app-programs></app-programs>`
})
export class AppComponent {}
