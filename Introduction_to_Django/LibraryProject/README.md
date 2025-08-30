# LibraryProject

This repository contains a basic Django project (`LibraryProject`) created as part of an introduction to Django development. It includes a `bookshelf` application with a `Book` model, configured for use with the Django admin interface, and documented CRUD operations.

## Project Structure

The project has the following key components:

- `manage.py`: Django's command-line utility for administrative tasks.
- `LibraryProject/`: The main Django project directory.
    - `settings.py`: Project-wide configurations.
    - `urls.py`: Project's URL declarations.
- `bookshelf/`: A Django application for managing books.
    - `models.py`: Defines the `Book` model.
    - `admin.py`: Configures the Django admin interface for the `Book` model.
    - `migrations/`: Contains database migration files.

## Setup and Installation

To set up and run this project locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Youssef-Bouhssina/Alx_DjangoLearnLab.git
    cd Alx_DjangoLearnLab/Introduction_to_Django/LibraryProject
    ```

2.  **Install Django:**
    Ensure you have Python installed. Then, install Django using pip:
    ```bash
    pip install django
    # Or, if 'pip' is not found, try 'pip3':
    # pip3 install django
    ```

3.  **Apply Migrations:**
    Although the migrations were not run during development due to environment issues, a dummy migration file is provided. In a functional environment, you would run:
    ```bash
    python manage.py makemigrations bookshelf
    python manage.py migrate
    ```

4.  **Create a Superuser (for Admin access):**
    ```bash
    python manage.py createsuperuser
    ```
    Follow the prompts to create an admin user.

5.  **Run the Development Server:**
    ```bash
    python manage.py runserver
    ```
    Open your web browser and go to `http://127.0.0.1:8000/`. You should see the Django welcome page.
    To access the admin interface, go to `http://127.0.0.1:8000/admin/` and log in with your superuser credentials.

## Bookshelf Application

### Book Model

The `bookshelf` app defines a `Book` model with the following fields in `bookshelf/models.py`:

-   `title`: `CharField` with a maximum length of 200 characters.
-   `author`: `CharField` with a maximum length of 100 characters.
-   `publication_year`: `IntegerField`.

### Django Admin Configuration

The `Book` model is registered with the Django admin in `bookshelf/admin.py` and includes custom configurations:

-   `list_display`: Displays `title`, `author`, and `publication_year` in the admin list view.
-   `list_filter`: Allows filtering by `publication_year` and `author`.
-   `search_fields`: Enables searching by `title` and `author`.

## CRUD Operations Documentation

The following Markdown files in the `bookshelf/` directory document the expected Python commands and outputs for basic CRUD (Create, Retrieve, Update, Delete) operations on the `Book` model, typically performed in the Django shell:

-   `bookshelf/create.md`: Details how to create a `Book` instance.
-   `bookshelf/retrieve.md`: Details how to retrieve a `Book` instance.
-   `bookshelf/update.md`: Details how to update a `Book` instance.
-   `bookshelf/delete.md`: Details how to delete a `Book` instance.
