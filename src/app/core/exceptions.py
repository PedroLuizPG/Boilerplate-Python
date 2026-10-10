class AppError(Exception):
     """Erro de domínio base. O handler global converte em resposta HTTP."""
     
     status_code: int = 400
     message: str = "Request Error"
     headers: dict[str, str] | None = None
     
     def __init__(self, message : str | None) -> None:
        if message:
            self.message = message
        super().__init__(self.message)
        
class NotFoundError(AppError):
    status_code = 404
    message = "Not Found"
    
class ConflictError(AppError):
    status_code = 409
    message = "Conflict with the current status of the resource"
    
class UnauthorizedError(AppError):
    status_code = 401
    message = "Not authenticated"
    headers = {"WWW-Authenticate": "Bearer"}
    
class ForbiddenError(AppError):  
    status_code = 403
    message = "You are not allowed this action"