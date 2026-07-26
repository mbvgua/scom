from email.message import EmailMessage
from pathlib import Path

import aiosmtplib
from fastapi.templating import Jinja2Templates

from app.config import settings

# ensure paths are absolute for vercel
BASE_DIR = Path(__file__).resolve().parent.parent

# define email templates to use
templates: Jinja2Templates = Jinja2Templates(directory=BASE_DIR / "templates/emails")


async def send_email(
    # from_email: str,
    reply_to: str,
    subject: str,
    plain_text: str,
    html_content: str | None = None,
) -> None:
    message = EmailMessage()
    message["From"] = f"{settings.mail_from} <{settings.mail_username}>"
    message["To"] = settings.official_home_mail
    message["Reply-To"] = reply_to
    message["Subject"] = subject

    # ifbrowser used doesnt allow rendering html pages
    message.set_content(plain_text)

    # if browser used allows rendering html
    if html_content:
        message.add_alternative(html_content, subtype="html")

    await aiosmtplib.send(
        message,
        hostname=settings.mail_server,
        port=settings.mail_port,
        username=settings.mail_username if settings.mail_username else None,
        password=settings.mail_password.get_secret_value() or None,
        start_tls=settings.mail_use_tls,
    )


async def send_contact_us_email(
    reply_to: str,
    subject: str,
    username: str,
    phone_number: str | None,
    message: str,
) -> None:
    template = templates.env.get_template("contact-us-email.html")
    html_content = template.render(
        username=username, email=reply_to, phone_number=phone_number, message=message
    )

    plain_text = f"""
    Hi SCOM,

    New inquiring received from website contact form:
    Name: {username}
    Email: {reply_to}
    Phone: {phone_number if phone_number else 'Not provided'}

    Message:
    ------------------------------------
    {message}
    ------------------------------------

    Best regards,
    {username}.
    """

    await send_email(
        reply_to=reply_to,
        subject=subject,
        plain_text=plain_text,
        html_content=html_content,
    )


async def send_get_involved_email(
    reply_to: str,
    subject: str,
    username: str,
    phone_number: str | None,
    interest: str,
    message: str,
) -> None:
    template = templates.env.get_template("get-involved-email.html")
    html_content = template.render(
        username=username,
        email=reply_to,
        phone_number=phone_number,
        interest=interest,
        message=message,
    )

    plain_text = f"""
    Hi SCOM,

    New inquiring received from website get involved form:
    Name: {username}
    Email: {reply_to}
    Phone: {phone_number if phone_number else 'Not provided'}

    Message:
    ------------------------------------
    {message}
    ------------------------------------

    Best regards,
    {username}.
    """

    await send_email(
        reply_to=reply_to,
        subject=subject,
        plain_text=plain_text,
        html_content=html_content,
    )
