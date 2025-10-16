import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface Program {
  id: number;
  program_name?: string;
  program_code?: string;
  cal_year?: number;
  program_description?: string;
}

@Injectable({
  providedIn: 'root'
})
export class ProgramService {
  private apiUrl = 'http://127.0.0.1:8000';

  constructor(private http: HttpClient) {}

  listPrograms(): Observable<Program[]> {
    return this.http.get<Program[]>(`${this.apiUrl}/programs`);
  }

  getProgram(id: number): Observable<Program> {
    return this.http.get<Program>(`${this.apiUrl}/programs/${id}`);
  }

  createProgram(program: Program): Observable<Program> {
    return this.http.post<Program>(`${this.apiUrl}/programs`, program);
  }
}
