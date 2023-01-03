from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from app.server.database import (
    add_car,
    delete_car,
    retrieve_car,
    retrieve_cars, update_car
)
from app.server.models.car import (
    ErrorResponseModel,
    ResponseModel,
    CarSchema,
    UpdateCarModel,
)

router = APIRouter()


@router.post("/", response_description="Car data added into the database")
async def add_car_data(car: CarSchema = Body(...)):
    car = jsonable_encoder(car)
    new_car = await add_car(car)
    return ResponseModel(new_car, "Car added successfully.")


@router.get("/", response_description="Cars retrieved")
async def get_cars():
    cars = await retrieve_cars()
    if cars:
        return ResponseModel(cars, "Cars data retrieved successfully")
    return ResponseModel(cars, "Empty list returned")


@router.get("/{id}", response_description="Car data retrieved")
async def get_car_data(id):
    car = await retrieve_car(id)
    if car:
        return ResponseModel(car, "Car data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Car doesn't exist.")


@router.put("/{id}")
async def update_car_data(id: str, req: UpdateCarModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_car = await update_car(id, req)
    if updated_car:
        return ResponseModel(
            "Car with ID: {} name update is successful".format(id),
            "Car name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred", 404, "There was an error updating the Car data.",
    )


@router.delete("/{id}", response_description="Car data deleted from the database")
async def delete_car_data(id: str):
    deleted_car = await delete_car(id)
    if deleted_car:
        return ResponseModel(
            "Car with ID: {} removed".format(id), "Car deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Car with id {0} doesn't exist".format(id)
    )
