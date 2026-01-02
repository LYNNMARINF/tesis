from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import JSONResponse
import shutil
import tempfile
import asyncio

import httpx


app = FastAPI()


# Set your pod's GRASP API endpoint URL here
POD_GRASP_URL = "http://69.30.85.49:8080/grasp"  # <-- Pod public IP

@app.post("/grasp")
async def grasp_endpoint(
    prompt: str = Form(...),
    file: UploadFile = File(...),
    max_round: int = Form(4),
    api_file: str = Form('api.key')
):
    # Save image temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp:
        shutil.copyfileobj(file.file, tmp)
        tmp_path = tmp.name
    try:
        # Forward the image and prompt to the remote pod
        async with httpx.AsyncClient() as client:
            with open(tmp_path, "rb") as img_file:
                files = {"file": (file.filename, img_file, file.content_type)}
                data = {"prompt": prompt, "max_round": str(max_round), "api_file": api_file}
                response = await client.post(POD_GRASP_URL, data=data, files=files)
        return JSONResponse(response.json(), status_code=response.status_code)
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)
    finally:
        # Temporary file cleanup
        try:
            import os
            os.remove(tmp_path)
        except Exception:
            pass
