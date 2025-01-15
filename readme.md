# WheelDeal: Vehicle Rental and Sales Application

WheelDeal is a Django-based web application that allows users to register, log in, and manage vehicle listings for rent or sale. Users can browse available vehicles, contact owners, and list their vehicles for others to see.

## Features

- User Registration and Authentication: Secure user registration, login, and logout functionality.

- Vehicle Management: Users can list their vehicles for rent or sale, including details like make, model, price, and images.

- Browse Listings: View all available vehicles and their details.

- Contact Owners: Send inquiries to vehicle owners directly from the application.

## Prerequisites

- Python 3.8+

- Django 4.x
 
- Bootstrap (for frontend styling)

- Virtual Environment (recommended)

## Installation

Step 1: **Clone the Repository**
```
https://github.com/shreyaskoshti9/wheelDeal.git
cd wheeldeal
```
Step 2: **Set Up a Virtual Environment**
```
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```
Step 3: **Install Dependencies**
```
pip install -r requirements.txt
```
Step 4: **Apply Migrations**
```
python manage.py makemigrations
python manage.py migrate
```
Step 5: **Run the Development Server**
```
python manage.py runserver
```
Visit http://127.0.0.1:8000/ in your browser.

## Directory Structure

```
WheelDeal/
|-- main/
|   |-- static/           # Static files (CSS, images, etc.)
|   |-- templates/        # HTML templates
|   |-- migrations/       # Database migrations
|   |-- admin.py          # Django admin site configuration
|   |-- apps.py           # App configuration
|   |-- forms.py          # Form definitions
|   |-- models.py         # Database models
|   |-- urls.py           # App-specific URLs
|   |-- views.py          # View functions
|-- WheelDeal/
|   |-- settings.py       # Project settings
|   |-- urls.py           # Project URLs
|   |-- wsgi.py           # WSGI configuration
|-- manage.py             # Django management script
|-- README.md             # Project documentation (this file)
|-- requirements.txt      # Python dependencies
```

## Usage

1. **Register an Account**

- Navigate to the Register page.

- Fill in the required fields and submit.

2. **Log In**

- Use the credentials to log in from the Login page.

3. **List a Vehicle**

- Go to List Vehicle.

- Fill out the form with details like title, make, model, price, and upload an image.

4. **Browse Vehicles**

- Navigate to Browse Vehicles to view all listed vehicles.

5. **Contact Vehicle Owner**

- Select a vehicle and use the Contact Owner form to send an inquiry.

## Built With

- Django: Backend framework

- Bootstrap: Frontend styling

- SQLite: Default database (can be replaced with PostgreSQL, MySQL, etc.)

## Screenshots

- Home Page: A welcoming interface.

- Register Page: User-friendly registration form.

- List Vehicles: Add details for a vehicle listing.

- Browse Vehicles: View all available vehicles.

## Future Enhancements

- Add search and filter functionality for vehicle listings.

- Enable users to upload multiple images per vehicle.

- Implement a booking system for rentals.

- Add user profile management.

## Contributing

Contributions are welcome! Please create a pull request or submit an issue for any bugs or feature requests.

## License

## Contact

For any inquiries or support, please contact.
