from fastapi import APIRouter
import google.generativeai as genai
import os
from pydantic import BaseModel

router = APIRouter()

# Old test route
@router.get("/api/test")
def test_route():
    return {"message": "Test Working Da!"}

# Pudusa - AI Fitness Plan
class FitnessRequest(BaseModel):
    age: int
    weight: float
    height: float
    goal: str  # weight loss / muscle gain

@router.post("/api/generate-plan")
def generate_plan(data: FitnessRequest):
    try:
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        model = genai.GenerativeModel("gemini-1.5-flash")
        
        prompt = f"Create diet and workout plan for {data.age} years old, {data.weight}kg, {data.height}cm, goal is {data.goal}. Give in simple format."
        
        response = model.generate_content(prompt)
        return {"plan": response.text, "status": "success"}
    except Exception as e:
        return {"error": str(e), "status": "failed"}