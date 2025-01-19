from fastapi import FastAPI
from mangum import Mangum
from fastapi.middleware.cors import CORSMiddleware
from ReceiptProcessor import calculatePoints, Receipt

app = FastAPI()
handler = Mangum(app)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/receipts/process")
async def process_api(receipt: Receipt):
    # generate the id
    receiptId = str(uuid4())
    calculatePoints(receipt)
    return {}

@app.get("/receipts/{id}/points")
async def get_point_api(receiptId : str):
   
    return {}
