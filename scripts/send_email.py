#!/usr/bin/env python3
"""Simple Gmail sender using App Password from 1Password."""

import smtplib
import subprocess
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Gmail SMTP settings
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL = "gomezbot602@gmail.com"

def get_app_password() -> str:
    """Fetch app password from 1Password."""
    result = subprocess.run(
        ["op", "item", "get", "Google", "--vault", "Gomez", "--fields", "app password", "--reveal"],
        capture_output=True, text=True, timeout=15
    )
    if result.returncode != 0:
        # Fallback: try the regular password field
        result = subprocess.run(
            ["op", "item", "get", "Google", "--vault", "Gomez", "--fields", "Passwd", "--reveal"],
            capture_output=True, text=True, timeout=15
        )
    return result.stdout.strip()

def send_email(to_addr: str, subject: str, body: str, html: bool = False) -> bool:
    """Send an email via Gmail SMTP."""
    try:
        app_password = get_app_password()
        if not app_password:
            print("Error: Could not retrieve password from 1Password")
            return False
            
        msg = MIMEMultipart('alternative')
        msg['From'] = EMAIL
        msg['To'] = to_addr
        msg['Subject'] = subject
        
        content_type = 'html' if html else 'plain'
        msg.attach(MIMEText(body, content_type))
        
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL, app_password)
            server.send_message(msg)
        
        print(f"Email sent to {to_addr}")
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: send_email.py <to> <subject> <body> [--html]")
        sys.exit(1)
    
    is_html = "--html" in sys.argv
    send_email(sys.argv[1], sys.argv[2], sys.argv[3], html=is_html)
