import logging
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class LogIPMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Get client IP
        client_ip = request.client.host
        logger.info(f"Received request: {request.method} {request.url} from {client_ip}")
        response = await call_next(request)
        logger.info(f"Response status: {response.status_code} for {client_ip}")
        return response