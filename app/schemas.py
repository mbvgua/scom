from pydantic import BaseModel, EmailStr

class ContactForm(BaseModel):
    # forbid client from sending extra data
    model_config = {"extra": "forbid"}

    username: str
    from_email: EmailStr
    phone_number: str | None
    message: str


class GetInvolvedForm(ContactForm):
    interest: str

