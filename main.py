from model import model_pipeline
from fastapi import FastAPI, UploadFile
from typing import Union
from PIL import Image
import io

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello World"}

@app.post("/ask")
def ask(text: str, image: UploadFile):
    content = image.file.read()
    image = Image.open(io.BytesIO(content))
    # image = Image(image.file)
    result = model_pipeline(text=text, image=image)
    return {"Answer": result}