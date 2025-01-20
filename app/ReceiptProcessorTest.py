import pytest
from fastapi.testclient import TestClient
from ReceiptProcessorAPI import app

client = TestClient(app)

class TestReceiptProcessor:
    def testTargetReceiptExample(self):
        receipt_data = {
            "retailer": "Target",
            "purchaseDate": "2022-01-01",
            "purchaseTime": "13:01",
            "items": [
                {
                    "shortDescription": "Mountain Dew 12PK",
                    "price": "6.49"
                },
                {
                    "shortDescription": "Emils Cheese Pizza",
                    "price": "12.25"
                },
                {
                    "shortDescription": "Knorr Creamy Chicken",
                    "price": "1.26"
                },
                {
                    "shortDescription": "Doritos Nacho Cheese",
                    "price": "3.35"
                },
                {
                    "shortDescription": "   Klarbrunn 12-PK 12 FL OZ  ",
                    "price": "12.00"
                }
            ],
            "total": "35.35"
        }

        response = client.post("/receipts/process", json=receipt_data)
        assert response.status_code == 200
        receiptId = response.json()["id"]

        pointsResponse = client.get(f"/receipts/{receiptId}/points")
        assert pointsResponse.status_code == 200
        assert pointsResponse.json()["points"] == 28

    def testMMCornerMarketReceiptExample(self):
        receipt_data = {
            "retailer": "M&M Corner Market",
            "purchaseDate": "2022-03-20",
            "purchaseTime": "14:33",
            "items": [
                {
                    "shortDescription": "Gatorade",
                    "price": "2.25"
                },
                {
                    "shortDescription": "Gatorade",
                    "price": "2.25"
                },
                {
                    "shortDescription": "Gatorade",
                    "price": "2.25"
                },
                {
                    "shortDescription": "Gatorade",
                    "price": "2.25"
                }
            ],
            "total": "9.00"
        }

        response = client.post("/receipts/process", json=receipt_data)
        assert response.status_code == 200
        receiptId = response.json()["id"]

        pointsResponse = client.get(f"/receipts/{receiptId}/points")
        assert pointsResponse.status_code == 200
        assert pointsResponse.json()["points"] == 109

    def testInvalidReceiptId(self):
        response = client.get("/receipts/nonexistent-id/points")
        assert response.status_code == 404
        assert response.json()["detail"] == "No receipt found for that ID."


    def testInvalidReceipt(self):
        badReceiptJson = {
            "retailer": "Target",
            "items": [
                {"shortDescription": "Mountain Dew 12PK", "price": "6.49"},
            ],
            "total": "BAD INPUT"
        }

        response = client.post("/receipts/process", json=badReceiptJson)
        assert response.status_code == 400, f"Unexpected status code {response.status_code}"
        assert response.json()["detail"] == "The receipt is invalid."
