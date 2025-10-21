import { bootstrapApplication } from '@angular/platform-browser';
import { AppComponent } from './app/app.component';
import { importProvidersFrom } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';
import { appConfig } from './app/app.config';

bootstrapApplication(AppComponent, {
  providers: [
    // include the app-level providers (router, hydration, etc.)
    ...appConfig.providers,
    importProvidersFrom(HttpClientModule, FormsModule)
  ],
}).catch(err => console.error(err));
