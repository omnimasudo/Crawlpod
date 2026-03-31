"""
Module: email_service.py
Description: Sends emails and manages notifications.
"""

import smtplib
from email.mime.text import MIMEText
from typing import List

class EmailService:
    def __init__(self, smtp_server: str, port: int):
        self.smtp_server = smtp_server
        self.port = port

    def send_email(self, sender: str, recipients: List[str], subject: str, body: str) -> bool:
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = ', '.join(recipients)
        try:
            with smtplib.SMTP(self.smtp_server, self.port) as server:
                server.sendmail(sender, recipients, msg.as_string())
            return True
        except Exception:
            return False
