# Mobile Store Inventory

This project is an inventory management system for registering and managing mobile phone information. The system allows users to manage the inventory of mobile phones and generate necessary reports.

## Features

- Register mobile phone information
- Manage inventory
- Generate reports
- Implemented using Docker

## 🚀 Getting Started

These instructions will guide you through getting a copy of the project up and running on your local machine for development and testing purposes.

## Prerequisites

Before you begin, ensure you have the following installed:

- [Docker](https://www.docker.com/get-started)

## Setup

To run the project using Docker, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/realsoli/Mobile_Store_Inventory.git
   cd Mobile_Store_Inventory
   ```
 2. **Dockerize the Application**
     ```bash
      docker-compose up --build
      ```
   This command builds the Docker images and starts the services as defined in `docker-compose.yml`.

3. **Access the Application**
   Visit `http://localhost:3000` in your browser after the build process completes.
