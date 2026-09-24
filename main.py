import json
import random
from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware
from slowapi.util import get_remote_address


def custom_key_func(request: Request) -> str:
    # Fallback if header missing (or for non-CF)
    return request.headers.get("cf-connecting-ip") or get_remote_address(request)

# Rate limiter: 120 requests per minute per IP
limiter = Limiter(key_func=custom_key_func, default_limits=["120/minute"], headers_enabled=True)
app = FastAPI()
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
app.add_middleware(SlowAPIMiddleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load reasons from JSON
reasons = json.loads((Path(__file__).parent / "reasons.json").read_text(encoding="utf-8"))


# Random rejection reason endpoint
@app.get("/no")
async def no():
    reason = random.choice(reasons)
    return {"reason": reason}
