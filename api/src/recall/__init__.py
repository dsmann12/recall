from typing import Union
import argparse
import os

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/health")
def read_health():
    return {"status": "ok"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

def main():
    """Entry point for the recall api module"""
    parser = argparse.ArgumentParser(description="Run the Recall API server")
    parser.add_argument(
        "--port",
        type=int,
        default=int(os.getenv("PORT", "8000")),
        help="Port to run the server on (default: 8000, or PORT env var)"
    )
    parser.add_argument(
        "--host",
        type=str,
        default=os.getenv("HOST", "0.0.0.0"),
        help="Host to bind to (default: 0.0.0.0, or HOST env var)"
    )
    parser.add_argument(
        "--reload",
        action="store_true",
        default=os.getenv("ENVIRONMENT", "dev") == "dev",
        help="Enable auto-reload for development"
    )
    
    args = parser.parse_args()

    import uvicorn
    uvicorn.run("recall:app", host=args.host, port=args.port, reload=args.reload)

if __name__ == "__main__":
    main()