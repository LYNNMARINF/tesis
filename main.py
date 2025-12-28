from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/process")
async def process_image(prompt: str = Form(...), file: UploadFile = File(...)):
    # Here you would process the image and the prompt
    # For now it only returns the filename and the received prompt
    return JSONResponse({"filename": file.filename, "prompt": prompt})
