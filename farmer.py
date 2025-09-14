import streamlit as st
import smtplib
from email.mime.text import MIMEText

# ----------------- APP UI -----------------
st.set_page_config(page_title="Smart Dairy - Password Recovery", page_icon="🐄")

st.title("🐄 Smart Dairy - Recover Password Mailer")

st.info("Use your Brevo SMTP login and key to send recovery emails.")

# ----------------- BREVO CONFIG -----------------
SMTP_SERVER = "smtp-relay.brevo.com"
SMTP_PORT = 587

# Credentials (from Brevo dashboard)
login_email = st.text_input("Brevo SMTP Login (e.g., 96fca9001@smtp-brevo.com)")
password = st.text_input("SMTP Key (Master Password)", type="password")

# Fixed sender & receiver
from_email = "sagar8796841091@gmail.com"   # must be verified in Brevo
to_email = "sagar9665278681@gmail.com"
subject = "Smart Dairy Recover Password"

# Recovery message
message = st.text_area(
    "Recovery Message", 
    "Hello, here is your Smart Dairy password reset link or temporary password."
)

# ----------------- SEND MAIL -----------------
if st.button("📧 Send Recovery Mail"):
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
