from fastapi import APIRouter, HTTPException, Depends, status

from backend.app.models import User

router = APIRouter(prefix="")

@router.post("/post/",status_code=2-1,response_model = User)
async def add_todo(user_data = User)