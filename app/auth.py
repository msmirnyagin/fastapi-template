from fastapi import Security, HTTPException, status
from fastapi.security import APIKeyHeader
   
api_key_header = APIKeyHeader(name="X-API-Key")
    
def get_user(api_key_header: str = Security(api_key_header)):
    if check_api_key(api_key_header):
        user = get_user_from_api_key(api_key_header)
        return user
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Missing or invalid API key"
        )

def check_api_key(api_key: str):
    return api_key in "12345"


def get_user_from_api_key(api_key: str):
    return "ok"