# myfirst_capstone - Employee Database System

## Preface
The **Employee Database System** is a terminal-based application built as a capstone project during the Data Science, Machine Learning & AI Bootcamp at **Purwadhika Digital Technology School**. This project aims to apply fundamental Python skills to build a practical system for managing employee records in a fictional company, *Straight Event Organizer*.

## Introduction
The Employee Database System is designed to support HR administrative functions by enabling users to manage employee data effectively. Users can perform essential CRUD operations (Create, Read, Update, Delete) through a structured menu system in the terminal. The program stores employee data in a dictionary and provides user interaction through text input.

## Features

| Feature | View | Create | Update | Delete |
|--------|------|--------|--------|--------|
| **Employees** | ✅ | ✅ | ✅ | ✅ |

> All features are accessible using the employee's `employee_id` as the main identifier for updating and deleting records.

### View
Users can view the entire list of employees in a structured table format, displaying the following fields: Number, Name, Employee ID, Gender, Age, Job Level, and Salary.

### Create
Users can add new employee data by entering the required information: Name, Employee ID, Gender, Age, Job Level, and Salary. The system automatically assigns a sequential number to each new employee.

### Update
To update a record, the user must provide a valid `employee_id`. Once identified, the user can choose which field to modify. The system then confirms the update and displays the modified data.

### Delete
This feature allows users to remove an employee record by entering the corresponding `employee_id`. Once deleted, the data table is refreshed to reflect the change.

## Technology
- **Python** – The entire application is built using core Python (no external libraries), making it lightweight and easy to run on any system with Python installed.

## Installation

1. Ensure Python is installed on your machine.
2. Clone this repository using the following command:
   ```bash
   git clone https://github.com/<your-username>/employee-database-system.git
3. Navigate to the project directory:
   ```bash
   cd employee-database-system
4. Run the program
   ```bash
   python employee_database_system.py

## Author
**Gregorius Daniel Aditya Pratama**
Capstone Project – Purwadhika Bootcamp
Straight Event Organizer (Fictional Company)


