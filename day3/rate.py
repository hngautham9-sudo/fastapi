from fastapi import FastAPI, Request
 
# Import Rate Limiter
from slowapi import Limiter
 
# Get Client IP Address
from slowapi.util import get_remote_address
 
# Middleware for Rate Limiting
from slowapi.middleware import SlowAPIMiddleware
 
# Create FastAPI Application
app = FastAPI()
 
# Create Limiter Object
# Uses client IP address to identify users
limiter = Limiter(
	key_func=get_remote_address
)
 
# Register limiter with FastAPI
app.state.limiter = limiter
 
# Add Rate Limiting Middleware
app.add_middleware(SlowAPIMiddleware)
 
# Home Endpoint
@app.get("/")
 
# Allow only 5 requests per minute
@limiter.limit("5/minute")
def home(request: Request):
 
	return {
    	"message": "Welcome to FastAPI"
	}



