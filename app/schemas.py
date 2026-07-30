"""
defines schemas to be utilized in the application. Helps in improved validation
and type hinting via use of pydantic models.

currently 2 schemas:
    - ContactForm
    - GetInvolvedForm
"""

from enum import Enum

from pydantic import BaseModel, EmailStr


class ContactForm(BaseModel):
    """
    inherits fomr the BaseModel
    schemas used by the contact us form, in the "/contact-us" URL. it contains:
        - username
        - from_email: used in the "reply-to" while replying
        - phone_number
        - message

    NOTE:
    - model_config here helps prevent user from sending in any additional data
      alongside those required. improved security
    """

    # forbid client from sending extra data
    model_config = {"extra": "forbid"}

    username: str
    from_email: EmailStr
    phone_number: str | None
    message: str


class GetInvolvedForm(ContactForm):
    """
    inherits from the ContactForm, which inherits from the BaseModel
    schema used by the get involved form in the "get-involved" URl. to the
    pre-existing types, it adds:
        - interest: what user wants to help out with
    """

    interest: str


class PostCategory(str, Enum):
    """
    defines the categories of posts to beused in the application
    """

    stories = "stories"
    events = "events"
    updates = "updates"
    impact = "impact"
