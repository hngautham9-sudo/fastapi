from fastapi import FastAPI
from fastapi import Request


# Create FastAPI Application
app = FastAPI()


# Middleware Function
# Executes before and after every request
@app.middleware("http")
async def log_requests(
    request: Request,
    call_next
):


    # Before Request Processing
    print("Request Received")
    print("URL:", request.url)
    print("Method:", request.method)


    # Send Request to Endpoint
    response = await call_next(request)


    # After Response Processing
    print("Response Sent")
    print("Status Code:", response.status_code)


    return response




# Home Endpoint
@app.delete("/")
def home():


    return {
        "message": "Welcome"
    }





