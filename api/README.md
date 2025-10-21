# Recall API

REST API for the Recall flashcard application. This API handles user management, flashcard creation, deck organization, and study session tracking.

## Overview

The Recall API is built with FastAPI and provides endpoints for:

- User authentication and registration
- Deck management and organization
- Flashcard CRUD operations within decks
- Study session tracking and progress
- Spaced repetition algorithms

## Getting Started

### Prerequisites

- Python 3.10+
- uv (for dependency management)

### Installation

```bash
# Install dependencies
uv sync

# Start development server
uv run fastapi dev src/recall

# Start uvicorn server
uv run recall
```

The API will be available at `http://localhost:8000`

### API Documentation

Once running, visit:
- **Interactive docs**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## Project Structure

```
api/
├── src/recall_api/          # Main application code
├── tests/                   # Test suite
├── pyproject.toml          # Project configuration
└── README.md               # This file
```

## Development

```bash
# Run with auto-reload
uv run fastapi dev

# Run on custom port
uv run fastapi dev --port 8002
```

## API Endpoints

### Authentication
- `POST /auth/register` - User registration
- `POST /auth/login` - User login
- `POST /auth/refresh` - Refresh access token

### Decks
- `GET /decks` - List user's decks
- `POST /decks` - Create new deck
- `GET /decks/{id}` - Get deck with cards
- `PUT /decks/{id}` - Update deck
- `DELETE /decks/{id}` - Delete deck

*Note: API endpoints are currently in development*

## License

This project is licensed under the GNU General Public License v3.0.