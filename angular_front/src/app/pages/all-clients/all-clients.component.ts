import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ClientService, Client } from '../../services/client.service';

@Component({
  selector: 'app-all-clients',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './all-clients.component.html',
  styleUrls: ['./all-clients.component.css'],
})
export class AllClientsComponent implements OnInit {
  clients: Client[] = [];

  constructor(private clientService: ClientService) {}

  ngOnInit(): void {
    this.clientService.getClients().subscribe((data) => {
      this.clients = data;
    });
  }
}