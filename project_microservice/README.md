"# Django Project: Project Tracker

This Django project, "Project Tracker," is a simple application designed to manage projects, tasks, and users. It consists of three Django apps: `projects`, `tasks`, and `users`.

## Features

* **Projects:** Create, read, update, and delete projects.
* **Tasks:** Create, read, update, and delete tasks, assign tasks to users.
* **Users:** Create, read, update, and delete users, user authentication (login, logout), user designation.
* **REST API:** Provides API endpoints for projects, tasks, and users.
* **Bootstrap Styling:** Uses Bootstrap for a responsive and user-friendly interface.
* **PostgreSQL Database:** Uses PostgreSQL for data storage.
* **Date Pickers:** Uses HTML5 date pickers for easy date selection.
* **Password Confirmation:** Ensures password confirmation during user creation and update.
* **Data Validation:** Validates data before saving to the database, including date format checks.
* **Success Popups:** Displays success messages after successful CRUD operations.
* **Error Handling:** Provides error handling for form submissions and API requests.

## Prerequisites

* Python 3.x
* PostgreSQL
* Virtual environment (recommended)

## Setup and Installation

1.  **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd <project_directory>
    ```

2.  **Create a virtual environment:**

    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**

    * **On macOS/Linux:**

        ```bash
        source venv/bin/activate
        ```

    * **On Windows:**

        ```bash
        venv\Scripts\activate
        ```

4.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

    (If you don't have a requirements.txt file, install them manually)

    ```bash
    pip install django djangorestframework psycopg2-binary python-dotenv django-bootstrap5
    ```

5.  **Create a `.env` file:**

    Create a `.env` file in the `tracker_project` directory with your database and secret key settings:

    ```
    DATABASE_NAME=your_database_name
    DATABASE_USER=your_database_user
    DATABASE_PASSWORD=your_database_password
    DATABASE_HOST=localhost
    DATABASE_PORT=5432
    SECRET_KEY=your_secret_key
    DEBUG=True
    ```

    Replace the placeholders with your actual database credentials and a secure secret key.

6.  **Create and apply migrations:**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

7.  **Create a superuser:**

    ```bash
    python manage.py createsuperuser
    ```

8.  **Run the development server:**

    ```bash
    python manage.py runserver
    ```

9.  **Access the application:**

    Open your web browser and navigate to `http://127.0.0.1:8000/`.

## Running Tests

To run the project's tests:

```bash
python manage.py test"