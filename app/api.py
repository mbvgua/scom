from typing import Annotated

from fastapi import APIRouter, Form, Request, BackgroundTasks, status
from fastapi.responses import JSONResponse
from pydantic import EmailStr

from app.main import templates
from app.config import settings
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
            phone_number=form.phone_number,
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
            send_contact_us_email,
            reply_to=form.from_email,
            subject=f"New Get Involved inquiry form",
            username=form.username,
            phone_number=form.phone_number,
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


# @router.post("/get-involved")
# def get_involved_form(
#     request: Request,
#     background_tasks: BackgroundTasks,
#     username: str = Form(...),
#     user_email: EmailStr = Form(...),
#     phone_number: str = Form(None),
#     message: str = Form(...),
# ):
#     background_tasks.add_task(
#         send_get_involved_email,
#         to_email=settings.official_home_mail,
#         username=username,
#         subject=f"Get involved Us email",
#         phone_number=phone_number,
#         message=message,
#     )
#     return {"message": "involvement confirmation sent"}
