from fastapi import FastAPI
import os
app = FastAPI()


@app.get("/")
def read_root():
    return {"Aloha": f"Abdulrehman Javed{os.environ.get('HOSTNAME','DEFAULT_ENV')}"}