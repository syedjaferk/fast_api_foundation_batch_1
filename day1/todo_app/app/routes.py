from fastapi import APIRouter, HTTPException
from app.models import Todo, TodoDB
from app.database import collection
from bson import ObjectId

router = APIRouter()

@router.post("/todos", response_model=TodoDB)
async def create_todo(todo: Todo):
    result = await collection.insert_one(todo.dict())
    return {**todo.dict(), "id": str(result.inserted_id)}

@router.get("/todos", response_model=list[TodoDB])
async def list_todos():
    todos = []
    async for todo in collection.find():
        todos.append({**todo, "id": str(todo["_id"])})
    return todos

@router.get("/todos/{todo_id}", response_model=TodoDB)
async def get_todo(todo_id: str):
    todo = await collection.find_one({"_id": ObjectId(todo_id)})
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return {**todo, "id": str(todo["_id"])}

@router.delete("/todos/{todo_id}")
async def delete_todo(todo_id: str):
    result = await collection.delete_one({"_id": ObjectId(todo_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Todo not found")
    return {"message": "Todo deleted"}
