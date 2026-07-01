# Student Portal Application

![Python](https://img.shields.io/badge/Python-3.13-blue?style=flat-square&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.1.3-black?style=flat-square&logo=flask&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-3-003B57?style=flat-square&logo=sqlite&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6-F7DF1E?style=flat-square&logo=javascript&logoColor=black)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)

A full-stack web application that allows students to submit their personal and academic details, and enables administrators to manage student records including admission status updates — all through a clean, responsive interface.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Database Schema](#database-schema)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Application](#running-the-application)
- [Application Pages](#application-pages)
- [API Endpoints](#api-endpoints)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

The Student Portal Application is a capstone fullstack project built with Python (Flask) on the backend and vanilla HTML, CSS, and JavaScript on the frontend. It demonstrates core web development concepts including form handling, file uploads, relational database management, asynchronous JavaScript, and RESTful routing.

---

## Features

- Multi-page application with a consistent navbar and footer across all pages
- Student registration form with full client-side and server-side validation
- Passport photograph upload saved to the server; filename stored in the database
- Dynamic select boxes (Department, Level, Region) populated asynchronously from a JSON data source
- Students index table listing all registered students fetched from the database
- Individual student details page displaying all submitted information including the uploaded photo
- Asynchronous admission status update (Pending / Admitted / Rejected) without page reload
- Responsive layout compatible with desktop and mobile viewports
- SQLite database with automatic initialization on first run

---

## Tech Stack

| Layer      | Technology                        |
|------------|-----------------------------------|
| Backend    | Python 3.13, Flask 3.1.3          |
| Database   | SQLite 3 (via Python `sqlite3`)   |
| Frontend   | HTML5, CSS3, Vanilla JavaScript   |
| Templating | Jinja2                            |
| File I/O   | Werkzeug `secure_filename`        |

---

## Project Structure

```
Student-s-Portal-Application/
|-- app.py                  # Flask application, routes, and business logic
|-- database.py             # Database connection and schema initialization
|-- requirements.txt        # Python dependencies
|-- students.db             # SQLite database (auto-generated, git-ignored)
|-- .gitignore
|-- static/
|   |-- css/
|   |   └── style.css       # Global stylesheet
|   |-- js/
|   |   |-- form.js         # Async select population and form validation
|   |   └── details.js      # Async admission status update
|   |-- data/
|   |   └── data.json       # Source data for dynamic select boxes
|   └── uploads/            # Uploaded student passport photos (git-ignored)
└── templates/
    |-- base.html           # Shared layout (navbar + footer)
    |-- index.html          # Landing page
    |-- form.html           # Student application form
    |-- students.html       # Students index table
    └── details.html        # Individual student details
```

---

## Database Schema

**Table: `students`**

| Column             | Type     | Constraints              |
|--------------------|----------|--------------------------|
| `id`               | INTEGER  | PRIMARY KEY AUTOINCREMENT |
| `first_name`       | TEXT     | NOT NULL                 |
| `last_name`        | TEXT     | NOT NULL                 |
| `email`            | TEXT     | NOT NULL                 |
| `phone`            | TEXT     | NOT NULL                 |
| `address`          | TEXT     | NOT NULL                 |
| `dob`              | TEXT     | NOT NULL                 |
| `gender`           | TEXT     | NOT NULL                 |
| `department`       | TEXT     | NOT NULL                 |
| `level`            | TEXT     | NOT NULL                 |
| `state`            | TEXT     | NOT NULL                 |
| `age`              | INTEGER  | NOT NULL                 |
| `image`            | TEXT     | NOT NULL                 |
| `admission_status` | TEXT     | DEFAULT `'Pending'`      |

---

## Getting Started

### Prerequisites

- Python 3.10 or higher
- pip (Python package manager)
- Git

### Installation

1. Clone the repository:

```bash
git clone https://github.com/reuben-idan/Student-s-Portal-Application.git
cd Student-s-Portal-Application
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

### Running the Application

```bash
python app.py
```

The application will automatically initialize the database on first run and start the development server.

Open your browser and navigate to:

```
http://127.0.0.1:5000
```

---

## Application Pages

| Route                  | Page              | Description                                                  |
|------------------------|-------------------|--------------------------------------------------------------|
| `/`                    | Landing Page      | Introduction to the portal with a call-to-action button      |
| `/form`                | Application Form  | Multi-field student registration form                        |
| `/students`            | Students Index    | Table of all registered students with View buttons           |
| `/student/<id>`        | Student Details   | Full profile of a selected student with status update form   |

---

## API Endpoints

| Method | Endpoint                    | Description                              |
|--------|-----------------------------|------------------------------------------|
| GET    | `/`                         | Render landing page                      |
| GET    | `/form`                     | Render application form                  |
| POST   | `/submit`                   | Process form submission and save to DB   |
| GET    | `/students`                 | Render students index table              |
| GET    | `/student/<int:student_id>` | Render individual student details        |
| POST   | `/update_status/<int:id>`   | Async JSON endpoint to update admission status |

**`POST /update_status/<id>` — Request Body:**

```json
{
  "status": "Admitted"
}
```

**Response:**

```json
{
  "success": true,
  "message": "Status updated to Admitted"
}
```

---

## Configuration

Key configuration values in `app.py`:

| Config Key           | Default Value       | Description                          |
|----------------------|---------------------|--------------------------------------|
| `UPLOAD_FOLDER`      | `static/uploads/`   | Directory where images are saved     |
| `ALLOWED_EXTENSIONS` | `png, jpg, jpeg, gif` | Permitted image file types         |
| `debug`              | `True`              | Flask debug mode (disable in production) |

> For production deployment, set `debug=False`, use a production WSGI server such as Gunicorn, and store configuration values in environment variables.

---

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Commit your changes: `git commit -m "Add your feature description"`
4. Push to the branch: `git push origin feature/your-feature-name`
5. Open a Pull Request

---

## License

This project is licensed under the MIT License.

---

&copy; 2026 StudentPortal. All rights reserved.
