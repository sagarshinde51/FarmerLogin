import streamlit as st
import smtplib
from email.mime.text import MIMEText

st.title("📧 Smart Dairy - Recover Password Mailer")

# Brevo SMTP details
SMTP_SERVER = "smtp-relay.brevo.com"
SMTP_PORT = 587

# Credentials (from Brevo SMTP settings)
login_email = "96fca9001@smtp-brevo.com"   # This is the SMTP Login from Brevo
password = "CHLfKzFp1xSUQym5..."           # This is the SMTP Key (Master Password)


# Fixed sender/receiver and subject
from_email = "sagar8796841091@gmail.com"   # must be verified in Brevo
to_email = "sagar9665278681@gmail.com"
subject = "Smart Dairy Recover Password"

# Recovery message
message = st.text_area("Enter Recovery Message", 
                       "Hello, here is your Smart Dairy password reset link or temporary password.")

if st.button("Send Recovery Mail"):
    try:
        # Create plain text email
        msg = MIMEText(message, "plain")
        msg["From"] = from_email
        msg["To"] = to_email
        msg["Subject"] = subject

        # Connect and send via Brevo SMTP
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(login_email, password)
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit()

        st.success(f"✅ Recovery mail sent to {to_email} from {from_email}")

    except Exception as e:
        st.error(f"❌ Failed to send email: {e}")
