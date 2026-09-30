# 📘 Assignment: SQLite and CRUD with Python

## 🎯 Objective

Learn how to use SQLite with Python to store and manage data in a small database application. Students will practice creating tables, inserting records, and performing CRUD operations.

## 📝 Tasks

### 🛠️ Set Up the Database

#### Description
Create a SQLite database and define a table for storing student or task records.

#### Requirements
Completed program should:

- Connect to a SQLite database using Python
- Create a table with at least a few columns, such as `id`, `name`, and `status`
- Make sure the table is created only once so repeated runs do not fail
- Print a confirmation message when the database is ready

### 🛠️ Create and Read Records

#### Description
Add data to the database and retrieve records so the user can see what is stored.

#### Requirements
Completed program should:

- Insert at least three sample records into the table
- Use `SELECT` queries to read all records
- Display each record in a clear, readable format
- Show the total number of records in the database

### 🛠️ Update and Delete Records

#### Description
Practice modifying and removing database entries using SQL commands.

#### Requirements
Completed program should:

- Update an existing record using `UPDATE`
- Delete a record using `DELETE`
- Confirm the changes with a successful message or a refreshed list of records
- Demonstrate both the before-and-after result of the update or deletion

### 🛠️ Build a Simple User Menu

#### Description
Create a small command-line menu so users can interact with the database without editing code.

#### Requirements
Completed program should:

- Offer menu options such as add, view, update, and delete
- Prompt the user for the needed input values
- Repeat until the user chooses to exit
- Handle invalid input gracefully with a clear message
