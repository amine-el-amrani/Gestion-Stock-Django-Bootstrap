# Stock Management

Stock Management is a web application developed in Python using the Django framework. It allows managing a stock of products and distributing them to beneficiaries. The user interface is designed using HTML, CSS, and Bootstrap.

# Features

The project is split into two main apps:

- Addition, modification, and deletion of products using forms.
- Addition, modification, and deletion of beneficiaries using forms.
- Assignment of products to one or more beneficiaries.
- Import or export data in CSV format

# Instructions to Run the Application

To run the application, follow these steps:

1. Make sure you have Docker installed on your machine

2. Clone this Git repository to your local machine:
git clone https://github.com/amine-el-amrani/Gestion-Stock-Django-Bootstrap.git

3. Navigate to the project directory

4. Build the Docker image:
docker-compose build

5. Start the Docker containers:
docker-compose up

The application will be accessible in your browser at http://localhost:8000/