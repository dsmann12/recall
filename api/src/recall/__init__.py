"""Recall API module.

This module sets up a FastAPI application for the recall service, which allows
users to create, edit, study, and manage flashcards.

Example:
    from recall import app
    uvicorn.run(app, host="0.0.0.0", port=8000)

Attributes:
    app (FastAPI): The FastAPI application instance for the recall API.
"""

import argparse
import os

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    """Get the root endpoint of the API.

    Simply returns a greeting message for now.

    Returns:
        dict: A dictionary with a greeting message.

    """
    return {"Hello": "World"}


@app.get("/health")
def read_health():
    """Health check endpoint.

    Returns:
        dict: A dictionary indicating the health status of the API.
    """
    return {"status": "ok"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    """Get an item by its ID.

    This is really just a placeholder endpoint for testing purposes.

    Returns:
        dict: A dictionary containing the item ID and an optional query
            parameter.
    """
    return {"item_id": item_id, "q": q}


def main():
    """Entry point for the recall api module.

    This function sets up and runs the API server.

    Can take optional command-line arguments for host, port, and reload mode.

    Example:
        python -m recall --port 8080 --host 127.0.0.1 --reload
    """
    parser = argparse.ArgumentParser(description="Run the Recall API server")
    parser.add_argument(
        "--port",
        type=int,
        default=int(os.getenv("PORT", "8000")),
        help="Port to run the server on (default: 8000, or PORT env var)",
    )
    parser.add_argument(
        "--host",
        type=str,
        default=os.getenv("HOST", "0.0.0.0"),
        help="Host to bind to (default: 0.0.0.0, or HOST env var)",
    )
    parser.add_argument(
        "--reload",
        action="store_true",
        default=os.getenv("ENVIRONMENT", "dev") == "dev",
        help="Enable auto-reload for development",
    )

    args = parser.parse_args()

    # This is the only place where we import uvicorn, to avoid unnecessary
    # dependency if the module is imported elsewhere.
    import uvicorn

    uvicorn.run(
        "recall:app", host=args.host, port=args.port, reload=args.reload
    )


if __name__ == "__main__":
    main()
