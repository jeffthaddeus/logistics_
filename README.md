# Load Management Application

This is a simple Flask application to manage loads for a logistics company.

## Features

- View all loads
- Add a new load
- Delete a load

## Technologies Used

- Python
- Flask
- SQLAlchemy
- SQLite

## Setup Instructions

1. Clone the repository:
    ```
    git clone <repository_url>
    cd <repository_directory>
    ```

2. Create a virtual environment and activate it:
    ```
    python -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```
    pip install -r requirements.txt
    ```

4. Set up the database:
    ```
    flask shell
    >>> from app import db
    >>> db.create_all()
    >>> exit()
    ```

5. Run the application:
    ```
    flask run
    ```

## Usage

- Navigate to `http://127.0.0.1:5000/` to view all loads.
- Use the "Add Load" button to add a new load.
- Use the "Delete" button next to each load to delete it.

## Configuration

You can configure the application by modifying the `app.config` dictionary in `app.py`.

- `SQLALCHEMY_DATABASE_URI`: The database URI that should be used for the connection.
- `SECRET_KEY`: A secret key for the session.
