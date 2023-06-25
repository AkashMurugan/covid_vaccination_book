# COVID Vaccination Booking Web Application

The COVID Vaccination Booking Web Application is a comprehensive solution built using the Django framework, designed to facilitate the process of COVID-19 vaccination appointments. It offers distinct features for both users and administrators.

## Hosted Site
https://covid-vaccination-booking.onrender.com/

## User Features

### Login and Sign up
Users can securely log in to their accounts or create new accounts with appropriate data validations. This ensures that only authorized individuals can access the system.

### Search Vaccination Centre
Users can search for nearby vaccination centres. The application provides information about the centres and working hours. This feature helps users identify convenient vaccination options.

### Book Vaccination Slot
Once logged in, users can apply for a vaccination slot. However, to ensure efficient vaccine distribution, the application restricts each day's appointments to a maximum of 10 candidates. Users can select their preferred time slot from the available options and reserve their spot.

### Logout
Users can log out of their accounts, ensuring the security of their personal information and preventing unauthorized access to their accounts.

## Admin Features

### Admin Login
Administrators have a separate login portal to access the administrative functionalities of the application. This provides enhanced security and control over the system.

### Add Vaccination Centres
Admins can add new vaccination centres to the system. They enter relevant details such as the centre's name, address, contact information, and working hours. This ensures that the application stays up-to-date with the latest vaccination centre information.

### Get Vaccination Details
Admins can access vaccination details provided by vaccination centres. This gives us that the users of the vacccination slots where they have booked at the reespective date.

### Get Dosage Details
Admins can access dosage details provided by the vaccination centres. The application groups the dosage information according to the respective centres, enabling administrators to monitor and manage the vaccine distribution efficiently.

### Remove Vaccination Centres
Admins have the authority to remove vaccination centres from the system when necessary. This ensures that outdated or closed centres are promptly removed from the application, preventing users from accessing inaccurate information.

## Tech Stack

The COVID Vaccination Booking Web Application utilizes the following tech stack:

- Backend: Django (a powerful Python web framework)
- Database: Django Administration 
- Frontend: HTML and CSS and Tailwind

The Django framework provides a robust foundation for building secure and scalable web applications, while HTML and CSS are used to create a user-friendly and visually appealing frontend.

## Getting Started

To run the application on your local machine, follow these steps:

1. Clone the repository: `git clone <https://github.com/AkashMurugan/covid_vaccination_booking>`
2. Install the required dependencies by running: `pip install -r requirements.txt`
3. Configure the database settings in the `<project-directory>/settings.py` file.
4. Apply migrations to set up the database schema: `python manage.py migrate`
5. Start the development server: `python manage.py runserver`
6. Access the application in your web browser at `http://localhost:8000/`

## Contributing

Contributions to the COVID Vaccination Booking Web Application are welcome. To contribute, follow these steps:

1. Fork the repository on GitHub.
2. Create a new branch for your feature or bug fix: `git checkout -b feature/your-feature-name`
3. Make your changes, commit them, and push to your branch.
4. Submit a pull request, describing the changes you made and their purpose.

## License

This project is licensed under the MIT License. You can find more details in the [LICENSE](LICENSE) file.

## Acknowledgements

We would like to acknowledge the following resources that have assisted in the development of this web application:

- Django documentation: [https://docs.djangoproject.com/](https://docs.djangoproject.com/)
- HTML and CSS tutorials: [https://www.w3schools.com/](https://www.w3schools.com/)

These resources have been invaluable in understanding and implementing the features

 of the COVID Vaccination Booking Web Application.
