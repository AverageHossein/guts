from core.extensions import api

@api.errorhandler
def handle_exception(error: Exception):
    message = "Error: " + getattr(error, 'message', str(error))
    return {'message': message}, getattr(error, 'code', 500)


api._default_error_handler = Exception
api.error_handlers[Exception] = handle_exception