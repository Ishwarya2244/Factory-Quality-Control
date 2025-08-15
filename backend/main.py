from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Enable CORS for frontend-backend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define data model
class MachineData(BaseModel):
    temperature: float
    machine_speed: float
    energy_usage: float

@app.get("/")
async def root():
    return {"message": "API is running!"}

@app.post("/predict")
async def predict_quality(data: MachineData):
    if data.temperature > 50 or data.machine_speed > 1500:
        return {"status": "Warning", "message": "Machine parameters exceed safe limits!"}
    else:
        return {"status": "OK", "message": "Machine running within normal limits"}
