
# Copilot Instructions for AI Coding Agents

## Project Overview
This repository implements a FastAPI-based server for exposing a GRASP (robotic grasping) model as an HTTP API. The service receives an image and a prompt, processes them using the GRASP model, and returns grasping results. The project is designed for deployment on platforms like RunPod using Docker.

## Key Files and Structure
- `main.py`: (Optional) Entry point for FastAPI or other scripts.
- `api_server.py`: Main FastAPI app exposing the `/grasp` endpoint. Handles image upload, prompt, and calls the GRASP model.
- `requirements.txt`: Python dependencies (FastAPI, Uvicorn, etc.).
- `Dockerfile`: Containerizes the app for deployment.
- `.github/copilot-instructions.md`: This file.

## Developer Workflows
- **Local development:**
	1. Install dependencies: `pip install -r requirements.txt`
	2. Run the server: `uvicorn api_server:app --reload --host 0.0.0.0 --port 8080`
	3. Test the `/grasp` endpoint with an HTTP client (e.g., curl, Postman, or Python requests).
- **Docker/Cloud deployment:**
	1. Build image: `docker build -t grasp-api .`
	2. Run: `docker run -p 8080:8080 grasp-api`
	3. Deploy to RunPod: Import GitHub repo and follow RunPod’s deployment flow.

## Project-Specific Patterns
- The endpoint `/grasp` expects a multipart/form-data POST with fields:
	- `prompt`: string
	- `file`: image file
	- (optional) `max_round`, `api_file`
- Uploaded images are saved as temporary files and deleted after processing.
- The GRASP model is invoked via the `GraspMAS` class (see `api_server.py`).
- Avoid using `asyncio.run()` inside async endpoints; use `await` for coroutines.

## Integration Points
- Designed for serverless or pod-based deployment (e.g., RunPod).
- Expects the GRASP model and its dependencies to be available in the container.

---
*Last updated: December 28, 2025*
