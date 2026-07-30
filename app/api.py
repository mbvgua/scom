"""
setup the application API routes

these routes do not render any pages,but instead interact with data in JSON
format, and mostly return JSONResponse. contains 2 routes:
    - contact_us_form
    - get_involved_form
"""

from typing import Annotated

from fastapi import APIRouter, Form, Request, BackgroundTasks, status
from fastapi.responses import JSONResponse

from app.schemas import ContactForm, GetInvolvedForm
from app.email_utils import send_contact_us_email, send_get_involved_email

router = APIRouter(prefix="/api", tags=["api"])


@router.post("/contact-us")
def contact_us_form(
    request: Request,
    form: Annotated[ContactForm, Form()],
    background_tasks: BackgroundTasks,
):
    """
    endpoint receives the data contained in the contact form, rendered in the
    "/contact-us" URL, and delivers it to the admins email. form data is
    validated in the "ContactForm" schema.

    appropriate success/error messages and codes are returned as JSON
    """

    try:
        background_tasks.add_task(
            send_contact_us_email,
            reply_to=form.from_email,
            subject=f"Contact Form Inquisition by {form.username}",
            username=form.username,
            phone_number=form.phone_number if form.phone_number else None,
            message=form.message,
        )

        # if sent email successfully
        return JSONResponse(
            content={
                "status": "success",
                "message": "Message sent successfully!",
            },
            status_code=status.HTTP_200_OK,
        )
    except Exception as e:
        # if sth went wrong whilst sending email
        return JSONResponse(
            content={
                "status": "error",
                "message": f"An error occurred: {e}. Please try again.",
            },
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


@router.post("/get-involved")
def get_involved_form(
    request: Request,
    form: Annotated[GetInvolvedForm, Form()],
    background_tasks: BackgroundTasks,
):
    """
    endpoint receives the data contained in the get involved form, rendered in the
    "/get-involved" URL, and delivers it to the admins email. form data is
    validated in the "GetInvolvedForm" schema.

    appropriate success/error messages and codes are returned as JSON
    """

    try:
        background_tasks.add_task(
            send_get_involved_email,
            reply_to=form.from_email,
            subject=f"Get Involved Form Inquisition by {form.username}",
            username=form.username,
            phone_number=form.phone_number if form.phone_number else None,
            interest=form.interest,
            message=form.message,
        )

        # if sent email successfully
        return JSONResponse(
            content={
                "status": "success",
                "message": "Message sent successfully!",
            },
            status_code=status.HTTP_200_OK,
        )
    except Exception as e:
        # if sth went wrong whilst sending email
        return JSONResponse(
            content={
                "status": "error",
                "message": f"An error occurred: {e}. Please try again.",
            },
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
