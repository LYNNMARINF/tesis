from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/process")
async def process_image(prompt: str = Form(...), file: UploadFile = File(...)):
    # Aquí procesarías la imagen y el prompt
    # Por ahora solo devuelve el nombre del archivo y el prompt recibido
    return JSONResponse({"filename": file.filename, "prompt": prompt})
