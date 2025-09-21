from fastapi import FastAPI

app = FastAPI(title="CRM Mobile App Starter")

@app.get("/health")
def health_check():
    return {"status": "ok"}
