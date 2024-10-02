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
   Visit `http://localhost:8000` in your browser after the build process completes.

## Create a Superuser

To access the Django admin panel and manage products, you need to create a superuser. Follow these steps:

1. **While Docker Compose is running**, you need to open a new terminal in the same directory

2. **Create a superuser** by running the following command:
   
   ```bash
   docker-compose exec web python manage.py createsuperuser

   ```
    You will be prompted to enter a username, email, and password for the superuser. Make sure the password meets Django's security requirements.
   
## Add Product
 3. **After creating the superuser,** you can access the admin interface at:
 
     ```bash
     http://localhost:8000/admin/
     ```
      OR:
    
      **after creating the superuser, go to the http://localhost:8000/**

      **There is a "Login Panel" button that you can click. Enter the username and password you created for the superuser.**

      **Once logged in, an "Add Product" button will appear on the  http://localhost:8000/, allowing you to start adding products.**









        
