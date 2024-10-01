import smtplib
import os
import re


class Email:
    def __init__(self):
        self.my_email = os.environ["MY_EMAIL"]
        self.password = os.environ["MY_PASSWORD"]

    def send_email(self, receiver_email, message, header):
        message = message.get("1.0", "end-1c")
        receiver_email = receiver_email.get()
        header = header.get()
        pattern = r"\w+@[A-Za-z]+\.(com|edu|net)"
        if re.search(pattern, receiver_email):
            try:
                with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                    connection.starttls()
                    connection.login(user=self.my_email, password=self.password)
                    connection.sendmail(from_addr=self.my_email,
                                        to_addrs=receiver_email,
                                        msg=f"Subject:{header}\n\n{message}")
            except Exception:
                print("There was an error. Please try again.")
        else:
            pass
