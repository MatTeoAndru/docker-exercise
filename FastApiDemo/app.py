#uvicorn app:app --reload
# http://127.0.0.1:8000/docs

#brew install boom
# boom http://127.0.0.1:8000/sleep_slow -c 200 -n 200
# boom http://127.0.0.1:8000/sleep_fast -c 200 -n 200



#1)
# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def root():
#     return {"message": "hello world again"}

#1)

#2)

# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def root():
#     return {"message": "hello world again"}

# @app.get("/users/{user_id}")
# def read_user(user_id: str):
#     return {"user_id": user_id}

#2)


#3)
# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def root():
#     return {"message": "hello world again"}

# @app.get("/users/{user_id}")
# def read_user(user_id: str):
#     return {"user_id": user_id}

# from pydantic import BaseModel, validator

# class Item(BaseModel):
#     name: str
#     price: float

# @app.post("/items/")
# def create_item(item: Item):
#     return item


#3)


#4)
# from fastapi import FastAPI
# from pydantic import BaseModel, validator

# app = FastAPI()

# @app.get("/")
# def root():
#     return {"message": "hello world again"}

# @app.get("/users/{user_id}")
# def read_user(user_id: str):
#     return {"user_id": user_id}



# class Item(BaseModel):
#     name: str
#     price: float

#     @validator("price")
#     def price_must_be_positive(cls, value):
#         if value <= 0:
#             raise ValueError(f"we expect price >= 0, we received {value}")
#         return value

# @app.post("/items/")
# def create_item(item: Item):
#     return item
# #4)

# #5)
# import time
# import asyncio

# @app.get("/sleep_slow")
# def sleep_slow():
#     time.sleep(1)
#     return {"status": "done"}

# @app.get("/sleep_fast")
# async def sleep_fast():
#     await asyncio.sleep(1)
#     return {"status": "done"}

#5)

#6 Unit test

import time
import asyncio

from pydantic import BaseModel, validator
from fastapi import FastAPI

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float

    @validator("price")
    def price_must_be_positive(cls, value):
        if value <= 0:
            raise ValueError(f"we expect price >= 0, we received {value}")
        return value


@app.get("/")
def root():
    return {"message": "hello world again"}


@app.get("/users/{user_id}")
def read_user(user_id: str):
    return {"user_id": user_id}


@app.post("/items/")
def create_item(item: Item):
    return item


@app.get("/sleep_slow")
def sleep_slow():
    r = time.sleep(1)
    return {"status": "done"}


@app.get("/sleep_fast")
async def sleep_fast():
    r = await asyncio.sleep(1)
    return {"status": "done"}

#6