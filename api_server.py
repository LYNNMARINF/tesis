from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import JSONResponse
import shutil
import tempfile
import asyncio
from agents.graspmas import GraspMAS

app = FastAPI()

def run_graspmas(api_file, prompt, image_path, max_round=4):
    graspmas = GraspMAS(api_file=api_file, max_round=max_round)
    return asyncio.run(graspmas.query(prompt, image_path))

@app.post("/grasp")
async def grasp_endpoint(
    prompt: str = Form(...),
    file: UploadFile = File(...),
    max_round: int = Form(4),
    api_file: str = Form('api.key')
):
    # Guardar imagen temporalmente
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp:
        shutil.copyfileobj(file.file, tmp)
        tmp_path = tmp.name
    try:
        save_path, grasp_pose = run_graspmas(api_file, prompt, tmp_path, max_round)
        return JSONResponse({
            "save_path": save_path,
            "grasp_pose": grasp_pose
        })
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)
    finally:
        # Limpieza del archivo temporal
        try:
            import os
            os.remove(tmp_path)
        except Exception:
            pass
