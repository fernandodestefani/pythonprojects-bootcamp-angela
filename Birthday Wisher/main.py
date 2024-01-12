import pandas
import datetime as dt
import random
import smtplib

MY_EMAIL = 'personal_email@email.com'
PASSWORD = 'personal_password'

now = dt.datetime.now()
today_month = now.month
today_day = now.day
today = (today_month, today_day)

birthday_data = pandas.read_csv('birthdays.csv')
birthdays_dict = {(row['month'], row['day']): (row['name'],row['email'],row['year'],row['month'],row['day']) for (index, row) in birthday_data.iterrows()}

random_number = random.randint(1, 3)

if today in birthdays_dict:
    with open(f'letter_templates/letter_{random_number}.txt', mode='r') as letter_file:
        letter_content = letter_file.read()
    personalized_letter = letter_content.replace('[NAME]', birthdays_dict[today][0])

    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthdays_dict[today][1],
            msg=f'Subject:Happy Birthday\n\n{personalized_letter}'
        )
