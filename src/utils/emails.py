"""
utility functions used for sending emails from the application to the admins
inbox. currently only two forms in the application, which warrant two main
functions for each of those, alongside one main send_email function that both
will ineherit from. plus a wrapper that runs a send as a background task
and logs its outcome. Hence has 4 functions:
    - send_email
    - send_in_background
    - send_contact_us_email
    - send_get_involved_email
"""

from collections.abc import Awaitable, Callable
from email.message import EmailMessage

import aiosmtplib

from src.config import get_settings
from src.main import templates

settings = get_settings()


async def send_email(
    reply_to: str,
    subject: str,
    plain_text: str,
    html_content: str | None = None,
) -> None:
    """
    this defines the main functionality for sending mail in the application.
    it styles it as needed, and sends its, checking to see ifthe browser
    supports html styled emails, else a plain text email will be sent.

    performs this async
    """
    message = EmailMessage()
    message["From"] = f"{settings.mail_from} <{settings.mail_username}>"
    message["To"] = settings.official_home_mail
    message["Reply-To"] = reply_to
    message["Subject"] = subject
    message.set_content(plain_text)  # send as plain text, no html

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


async def send_in_background(
    send_fn: Callable[..., Awaitable[None]],
    success_message: str,
    failure_message: str,
    **kwargs,
) -> None:
    """
    run an email send as a background task without losing errors.

    background tasks run after the response has been sent, so exceptions
    they raise never reach the route handler's try/except. catching and
    logging them here is the only way to know a send failed.
    """
    from src.main import logger  # lazy import avoids a circular import

    try:
        await send_fn(**kwargs)
        logger.info(success_message)
    except Exception:
        logger.exception(failure_message)


async def send_contact_us_email(
    reply_to: str,
    subject: str,
    username: str,
    phone_number: str | None,
    message: str,
) -> None:
    """
    defines how emails are sent in the "/contact-us" URL form.fetches the
    template and input needed place holders using jinja2 syntax and sends the
    email.

    all actions are performed async
    """
    template = templates.env.get_template("emails/contact_us.html")
    html_content = template.render(
        username=username, reply_to=reply_to, phone_number=phone_number, message=message
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
    """
    defines how emails are sent in the "/get-involved" URL form.fetches the
    template and input needed place holders using jinja2 syntax and sends the
    email.

    all actions are performed async
    """
    template = templates.env.get_template("emails/get_involved.html")
    html_content = template.render(
        username=username,
        reply_to=reply_to,
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
