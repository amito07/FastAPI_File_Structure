from fastapi import HTTPException, status

def CustomMessage(message, data=[]) -> dict:
    return {
        'message': message,
        'data': data
    }

def InternalServerError():
    return HTTPException(status_code= status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")


def UnauthorizedError():
    return HTTPException(status_code= status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")
