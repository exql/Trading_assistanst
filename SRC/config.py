from dotenv import load_dotenv
import os
from pathlib import Path


load_dotenv('.env')


class restCredencial:
    AUTHORIZED_CLIENT:str= os.getenv("AUTHORIZED_CLIENT")
    CLIENT_KEY:str= os.getenv("CLIENT_KEY")
    API_KEY:str= os.getenv("API_KEY")
    API_SECRET:str= os.getenv("API_SECRET")
    BASE_URL:str= os.getenv("BASE_URL")
    LOGIN_REST_URL:str= os.getenv("LOGIN_REST_URL")
    REFRESH_TOKEN_URL:str= os.getenv("REFRESH_TOKEN_URL")
    ACCOUNT_URL:str= os.getenv("ACCOUNT_URL")
    CASH_URL:str= os.getenv("CASH_URL")
    BALANCE_URL:str= os.getenv("BALANCE_URL")
    


if __name__== "__main__":
    credencials = restCredencial()