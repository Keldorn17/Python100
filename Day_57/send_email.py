import smtplib
import os
from dotenv import load_dotenv

load_dotenv('.env')


class SendEmail:
    def __init__(self, form_data: dict):
        self.__form_data: dict = form_data

    def send_email(self) -> None:
        try:
            with smtplib.SMTP('smtp.gmail.com') as connection:
                connection.starttls()
                connection.login(user=os.getenv('FROM_EMAIL'), password=os.getenv('PASSWORD'))
                connection.sendmail(from_addr=os.getenv('FROM_EMAIL'), to_addrs=os.getenv('TO_EMAIL'),
                                    msg=f'Name: {self.__form_data['name']}\n'
                                        f'Email: {self.__form_data['email']}\n'
                                        f'Phone: {self.__form_data['phone']}\n'
                                        f'Message: {self.__form_data['message']}')
        except smtplib.SMTPException as e:
            print(f"Failed to send email: {e}")
