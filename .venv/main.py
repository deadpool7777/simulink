from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# during dev, allow localhost and your static app origin
origins = ["http://localhost:3000", "https://<YOUR-FRONTEND-DOMAIN>"]
app.add_middleware(
    CORSMiddleware, allow_origins=origins, allow_credentials=True,
    allow_methods=["*"], allow_headers=["*"]
)

class SimInput(BaseModel):
    voltage: float
    current: float

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/simulate")
def simulate(inp: SimInput):
    # DUMMY RESPONSE for now:
    P = inp.voltage * inp.current
    return {"P": P, "message": "dummy backend running in Azure"}
