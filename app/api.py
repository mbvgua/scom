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

    try:
        background_tasks.add_task(
            send_contact_us_email,
            reply_to=form.from_email,
            subject=f"New Contact form inquiry",
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

    try:
        background_tasks.add_task(
            send_get_involved_email,
            reply_to=form.from_email,
            subject=f"New Get Involved inquiry form",
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
