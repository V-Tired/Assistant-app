import smtplib
import os


class Email:
    def __init__(self, ):
        self.my_email = os.environ["MY_EMAIL"]
        self.password = os.environ["MY_PASSWORD"]

    def send_email(self, receiver_email, message, header):
        message = message.get("1.0", "end-1c")
        receiver_email = receiver_email.get()
        header = header.get()
        if "@" in receiver_email and ".com" in receiver_email:
            try:
                with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                    connection.starttls()
                    connection.login(user=self.my_email, password=self.password)
                    connection.sendmail(from_addr=self.my_email,
                                        to_addrs=receiver_email,
                                        msg=f"Subject:{header}\n\n{message}")
            except KeyError:
                print("There was an error. Please try again.")
        else:
            pass
