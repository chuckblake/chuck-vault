#!/usr/bin/env python3
"""Simple Gmail sender using App Password from 1Password."""

import os
import smtplib
import subprocess
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

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

def send_email(to_addr: str, subject: str, body: str, html: bool = False, attachment_path: str = None) -> bool:
    """Send an email via Gmail SMTP."""
    try:
        app_password = get_app_password()
        if not app_password:
            print("Error: Could not retrieve password from 1Password")
            return False
            
        msg = MIMEMultipart('mixed')
        msg['From'] = EMAIL
        msg['To'] = to_addr
        msg['Subject'] = subject
        
        # Add body
        content_type = 'html' if html else 'plain'
        msg.attach(MIMEText(body, content_type))
        
        # Add attachment if provided
        if attachment_path and os.path.exists(attachment_path):
            with open(attachment_path, 'rb') as f:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(f.read())
            encoders.encode_base64(part)
            filename = os.path.basename(attachment_path)
            part.add_header('Content-Disposition', f'attachment; filename="{filename}"')
            msg.attach(part)
        
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
        print("Usage: send_email.py <to> <subject> <body> [--html] [--attach <file>]")
        sys.exit(1)
    
    is_html = "--html" in sys.argv
    attachment = None
    if "--attach" in sys.argv:
        attach_idx = sys.argv.index("--attach")
        if attach_idx + 1 < len(sys.argv):
            attachment = sys.argv[attach_idx + 1]
    
    send_email(sys.argv[1], sys.argv[2], sys.argv[3], html=is_html, attachment_path=attachment)
