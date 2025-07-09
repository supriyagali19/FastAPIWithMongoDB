from fastapi import FastAPI, HTTPException, APIRouter
from configrations import collection
from database.schema import all_employees, individual_employee
from database.models import Employee

app=FastAPI()
router=APIRouter()

@router.get("/")
async def get_all_employee_data():
    data= collection.find()
    return all_employees(data)
@router.get("/{id}")
async def get_employee_by_id(id: str):
    data = collection.find_one({"id":id})
    if not data:
        raise HTTPException(status_code=404, detail="Employee not found")
    return individual_employee(data)
@router.post("/")
async def create_employee(employee: Employee):
    existing_employee = collection.find_one({"id": employee.id})
    if existing_employee:
        raise HTTPException(status_code=400, detail="Employee with this ID already exists")
    collection.insert_one(employee.model_dump())
    return {"message": "Employee created successfully"}
@router.put("/{id}")
async def update_employee(id: str, employee: Employee):
    existing_employee = collection.find_one({"id": id})
    if not existing_employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    collection.update_one({"id": id}, {"$set": employee.model_dump()})
    return {"message": "Employee updated successfully"}
@router.delete("/{id}")
async def delete_employee(id: str):
    existing_employee = collection.find_one({"id": id})
    if not existing_employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    collection.delete_one({"id": id})
    return {"status_code":200,"message": "Employee deleted successfully"}

app.include_router(router)

