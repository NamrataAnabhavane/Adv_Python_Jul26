from datetime import datetime, timedelta, timezone
from typing import Optional
import bcrypt
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import oauth2PasswordBearer, oAuth2PasswordRequestForm
from jose import JWTError, jwt
from pydantic import BaseModel


app = FastAPI()

SECRET_KEY = "Your-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def verify_password(plain_password:str,hashed_password:str)->bool:
    return bcrypt.checkpw(
        plain_password.encode("utf-8"),
        hashed_password.encode("utf-8")
    )

def get_password_hash(password:str)->str:
    return bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt()
    ).decode("utf-8")

def create_access_token(data:dict, expires_delta:Optional[timedelta]=None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp":expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

oauth2_scheme = oauth2PasswordBearer(tokenUrl="token")

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class User(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None

class UserInDB(User):
    hashed_password: str

fake_users_db = {
    "namrata": {
        "username": "namrata",
        "email": "namrata@example.com",
        "full_name": "Namrata Anabhavane",
        "disabled": False,
        "hashed_password": get_password_hash("secret123"),
        "disabled": False,
    },
    "bipin": {
            "username": "bipin",
            "email": "bip@example",
            "full_name": "Bipin Anabhavane",
            "hashed_password": get_password_hash("secret123"),
            "disabled": True,
        },
}

def get_User(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)
    return None

async def authenticate_user(username: str, password: str):
    user = get_User(fake_users_db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception

        token_data = TokenData(username=username)

    except JWTError:
        raise credentials_exception
    user = get_User(fake_users_db, username=token_data.username)

    if user is None:
        raise credentials_exception
    return user

async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Inactive user"
        )
    return current_user

async def get_current_active_user(current_user: User = Depends(get_current_active_user)):
    if current_username != "namrata":
        raise HTTPException(
            status_code=status.HTTP_403_BAD_REQUEST,
            detail="Admin privileges required"
        )
    return current_user

@app.post("/token", response_model=Token)
async def login(form_data: oAuth2PasswordRequestForm = Depends()):
    user = await authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    
    return {"access_token": access_token, "token_type": "bearer"}