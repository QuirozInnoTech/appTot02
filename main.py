from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
def read_root():
    print("hi")
    return {"message2": "API local funcionando correctamente"}


@app.post("/webhook")
async def receive_webhook(request: Request):
    data = await request.json()
    print("Webhook2 recibido:", data)
    print("segunda sub recibido:", data)
    return {"status": "ok"}