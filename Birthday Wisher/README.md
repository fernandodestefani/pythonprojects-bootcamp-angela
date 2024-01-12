# Birthday Emailer with Personalized Greetings
Celebrate birthdays in style with an automated Birthday Emailer! This Python script utilizes a CSV file (birthdays.csv) to store birthday information and sends personalized birthday emails using Gmail. The email content is chosen randomly from three available templates.

## How to Use
Fill in the required information in the CSV file (birthdays.csv):

name: Name of the person.
email: Email address of the person.
year: Birth year of the person.
month: Birth month (numerical format) of the person.
day: Birth day (numerical format) of the person.
Customize the birthday greeting templates in the letter_templates folder. Use [NAME] as a placeholder for the person's name.

Run the script in a Python environment.

The script checks for birthdays on the current date. If there's a match, a personalized birthday email is sent to the respective person.

## Features
Automated Emailing: Send birthday wishes automatically based on the information in the CSV file.
Personalized Greetings: Choose from three different birthday greeting templates for a varied and personal touch.
Gmail Integration: Utilizes the Gmail SMTP server for sending emails securely.

Ensure that the CSV file is appropriately filled, and the letter templates suit your preference. Run the script, and let the Birthday Emailer take care of the celebrations!
