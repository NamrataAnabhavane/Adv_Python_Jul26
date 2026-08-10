from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, field_validator, model_validator, Field, EmailStr
import uvicorn

app = FastAPI()


class UserLogin(BaseModel):
    username: str = Field(..., min_length=3, max_length=20)
    password: str = Field(..., min_length=8)

    @field_validator("password")
    @classmethod
    def validator_password(cls, v):
        if not any(c.isupper() for c in v):
            raise ValueError("Password must contain at least one uppercase letter")

        if not any(c.islower() for c in v):
            raise ValueError("Password must contain at least one lowercase letter")

        if not any(c.isdigit() for c in v):
            raise ValueError("Password must contain at least one digit")

        return v


class UserRegistration(BaseModel):
    username: str
    email: EmailStr
    password: str
    password_confirm: str

    @model_validator(mode="after")
    def password_match(self):
        if self.password != self.password_confirm:
            raise ValueError("Passwords do not match")

        return self


@app.post("/login")
async def login(login_data: UserLogin):

    if login_data.username == "admin" and login_data.password == "Admin123":
        return {
            "message": "Login successful",
            "tokens": "fake-jwt-token"
        }

    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )


@app.post("/register")
async def register(user_data: UserRegistration):

    return {
        "message": "User registered successfully",
        "username": user_data.username,
        "email": user_data.email
    }


if __name__ == "__main__":
    uvicorn.run(
        "P1:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )