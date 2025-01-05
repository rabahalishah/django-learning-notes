# Django Restaurant App

This is a Django-based web application for managing a restaurant. 

## Installation

### Prerequisites

- Python 3.8+
- Django 4.0+
- PostgreSQL (optional, can use SQLite for development)

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/restaurant-app.git
   cd restaurant-app
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```bash
     source venv/bin/activate
     ```

4. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Set up the database:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. Create a superuser for admin access:
   ```bash
   python manage.py createsuperuser
   ```

7. Run the development server:
   ```bash
   python manage.py runserver
   ```

8. Access the application in your browser at `http://127.0.0.1:8000/`.

## Usage

- Navigate to the homepage to view the menu and place orders.
- Admin can log in to the dashboard at `/admin/` to manage the restaurant.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for review.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

