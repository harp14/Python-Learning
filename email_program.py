import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class EmailProgram:
    def __init__(self, receiver_email, subject, body):
        self.receiver_email = receiver_email
        self.subject = subject
        self.body = body

    # Send email - pass in parameters: receiver_email, subject, body
    def send_email(self):
        sender_email = "harp4491@gmail.com"
        password = "behqnnkfusgqgsac"

        message = MIMEMultipart("alternative")
        message["Subject"] = self.subject
        message["From"] = sender_email
        message["To"] = self.receiver_email

        # Create the HTML version message
        body = f"""
        <html>
            <head>
            </head>
            <body>
                {self.body}
            </body>
        </html>
        """

        # Turn these into plain/html MIMEText objects
        html = MIMEText(body, "html")

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        message.attach(html)

        # Create secure connection with server and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(
                sender_email, self.receiver_email, message.as_string()
            )
            server.close()
