import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms'

interface Program {
  id?: number;
  program_name: string;
  program_code: string;
  cal_year: number;
}

@Component({
  selector: 'app-programs',
  standalone: true,
  imports: [CommonModule, FormsModule, HttpClientModule],
  templateUrl: './programs.component.html',
})
export class ProgramsComponent implements OnInit {
  programs: Program[] = [];
  newProgram: Program = { program_name: '', program_code: '', cal_year: new Date().getFullYear() };

  constructor(private http: HttpClient) {}

  ngOnInit(): void {
    this.loadPrograms();
  }

  loadPrograms(): void {
    this.http.get<Program[]>('http://127.0.0.1:8000/programs')
      .subscribe({
        next: (data) => this.programs = data,
        error: (err) => console.error('Failed to load programs', err)
      });
  }

  addProgram(): void {
    this.http.post<Program>('http://127.0.0.1:8000/programs', this.newProgram)
      .subscribe({
        next: (p) => {
          this.programs.push(p);
          this.newProgram = { program_name: '', program_code: '', cal_year: new Date().getFullYear() };
        },
        error: (err) => console.error('Failed to create program', err)
      });
  }
}
