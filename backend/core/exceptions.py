from rest_framework.views import exception_handler
from rest_framework.response import Response


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if response is not None:
        if response.status_code == 404:
            data = {
                "success": False, 
                "error": {
                    "code": "Not_Found",
                    "message": "The URL you're looking for does not found.",
                    "details": "The page doesn't exist, you may entered a wrong URL."
                }
            }
            return Response(data=data, status=response.status_code)
        
        elif response.status_code == 403:
            data = {
                "success": False, 
                "error": {
                    "code": "Permission_Denied",
                    "message": "You don't have permission to enter this URL.",
                    "details": "The URL may need you to log in or it may belong to Admin."
                }
            }
            return Response(data=data, status=response.status_code)

        
        elif response.status_code == 400:
            data = {
                "success": False, 
                "error": {
                    "code": "Validation_ERROR",
                    "message": "The validation doesn't accept the input.",
                    "details": "You may entered a wrong input data."
                }
            }
            return Response(data=data, status=response.status_code)
        
        else:
            return response