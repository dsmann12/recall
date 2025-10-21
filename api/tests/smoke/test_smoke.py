import os

import httpx

ACCEPTANCE_TEST_API_URL = os.getenv("ACCEPTANCE_TEST_API_URL", "http://localhost:8000")

class TestSmoke:
    def test_read_root(self):
        # Act
        response = httpx.get(f"{ACCEPTANCE_TEST_API_URL}/")

        # Assert
        assert response.status_code == 200
        assert response.json() == {"Hello": "World"}

    def test_read_item(self):
        # Arrange
        item_id = 42

        # Act
        response = httpx.get(f"{ACCEPTANCE_TEST_API_URL}/items/{item_id}", params={"q": "test"})

        # Assert
        assert response.status_code == 200
        assert response.json() == {"item_id": item_id, "q": "test"}

    def test_read_health(self):
        # Act
        response = httpx.get(f"{ACCEPTANCE_TEST_API_URL}/health")

        # Assert
        assert response.status_code == 200
        assert response.json() == {"status": "ok"}