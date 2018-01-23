import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'app';
  emails = [{
    email: "nelson@nelson.com",
    importance: false,
    subject: "About those TPS reports...",
    content: "Yeah...if you could...get those in to me..."
  },
  {
    email: "bill@gates.com",
    importance: true,
    subject: "Microsoft just got hacked!!",
    content: "What do I pay you for!!!!!!"
  }
  ]
}
