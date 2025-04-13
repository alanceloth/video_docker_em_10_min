from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Aplicação com Dockerfile completo"}

@app.get("/health")
def health_check():
    return {"status": "ok"}
