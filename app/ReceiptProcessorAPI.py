from uuid import uuid4
from fastapi import FastAPI
from mangum import Mangum
from fastapi.middleware.cors import CORSMiddleware
from ReceiptProcessor import calculatePoints, Receipt,id_receipts_map, id_points_map

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
    id_receipts_map[receiptId] = receipt
    curPoints = calculatePoints(receipt)
    id_points_map[receiptId] = curPoints
    return {"id": receiptId}

@app.get("/receipts/{receiptId}/points")
async def get_point_api(receiptId : str):
    return {"points": id_points_map[receiptId]}

@app.get("/")
async def root():
    return {"message": "Hello World"}
