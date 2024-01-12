# Workout Tracker with Nutritionix and Google Sheets Integration
Track your workouts effortlessly using this Python script! Based on the input provided, the script interacts with the Nutritionix API to identify exercises and records the workout details in a Google Sheets document. This project is part of the Angela Yu's 100 Days of Code course.

## How to Use
Obtain API Keys:
Sign up on Nutritionix to get your API keys.

Set Environment Variables:
Create a .env file in the project directory.

Add the following variables to the file:
API_ID='your_nutritionix_api_id'
API_KEY='your_nutritionix_api_key'
USERNAME='your_nutritionix_username'
PASSWORD='your_nutritionix_password'
SHEET_ENDPOINT='your_google_sheets_endpoint'

Install Dependencies:
Run the following command to install the required Python packages:
pip install requests

Run the Script:
Execute the script in a Python environment.
python workout_tracker.py

## Features
Nutritionix API Integration: Utilizes the Nutritionix API to identify exercises based on user input.
Google Sheets Logging: Records workout details, including date, time, exercise, duration, and calories, in a Google Sheets document.
Environment Variables: Protects sensitive information by using environment variables for API keys and credentials.
Stay fit and organized with the Workout Tracker! Special thanks to Angela Yu's 100 Days of Code course for providing the inspiration and guidance.