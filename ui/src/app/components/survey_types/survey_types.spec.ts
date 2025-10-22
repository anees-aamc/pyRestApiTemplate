import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SurveyTypes } from './survey_types';

describe('Surveys', () => {
  let component: SurveyTypes;
  let fixture: ComponentFixture<SurveyTypes>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [SurveyTypes]
    })
    .compileComponents();

    fixture = TestBed.createComponent(SurveyTypes);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
