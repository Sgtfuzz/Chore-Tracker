import smtplib
from email.mime.text import MIMEText

def send_email(subject, body, to_emails):
    from_email = #app email address goes here
    app_password = #app password goes here
    
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = ', '.join(to_emails)
    
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(from_email, app_password)
            server.sendmail(from_email, to_emails, msg.as_string())
        print("Email sent successfully.")
    except Exception as e:
        print("Failed to send email:", e)
    