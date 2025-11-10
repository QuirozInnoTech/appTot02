from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
def read_root():
    return {"message2": "API local funcionando correctamente"}

@app.post("/webhook1")
async def receive_webhook(request: Request):
    data = await request.json()
    print("Webhook1 recibido:", data)
    return {"status": "ok"}