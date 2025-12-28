FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["uvicorn", "api_server:app", "--host", "0.0.0.0", "--port", "8080"]

async def run_graspmas(api_file, prompt, image_path, max_round=4):
    graspmas = GraspMAS(api_file=api_file, max_round=max_round)
    return await graspmas.query(prompt, image_path)
