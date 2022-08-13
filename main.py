import os
import json
import random
import shutil
from fastapi import FastAPI, HTTPException, UploadFile, Request
from fastapi.responses import JSONResponse
from typing import  Union
from pyquery import PyQuery
from pydantic import BaseModel
from uuid import uuid4 # Universally Unique Identifier
import jsonpath
from urllib.request import urlopen
from urllib import response

# PyDantic BaseModel Class
class Item(BaseModel):
    id: int
    name: Union[str, None] = None
    price: int
    calories: float
    sugar_content: float

# Exception Class
class MyException(Exception):
    def __init__(self, name: str):
        self.name = name

class IDNotFound(Exception):
    def __init__(self, name: str):
        self.name = name
                    
class UploadFailed(Exception):
    def __init__(self, name: str):
        self.name = name
                    
app = FastAPI() # FastAPI Module

# Local data initialize
my_items = []
my_file = '50bluelist.json'
my_file_names = []
# Load local json file if exist
if os.path.exists(my_file):
    with open(my_file, "r") as f:
        my_items = json.load(f)

# GET Method Exercise (Basic)
@app.get('/')
def root():
    return {"message": "Hello, welcome to my drinks shop!"}

@app.get('/all-products')
def all_products():
    drinksname=[]
    for i in my_items:
        drinksname.append(i['name'])
    return {'These are our products for all below:' : drinksname}

@app.get('/over-calories/{cnt}')
def over_caloriess(cnt: int = 1):
    listname=[]
    for i in my_items:
        if float(i['calories']) >= cnt:
            listname.append(i);
    return {'list: ': listname}

@app.get('/find-drinks/{id}')
def find_drinks(id: int = 1):
    if id > len(my_items):
        raise IDNotFound(name = id)
    else:
        for x in my_items:
            if int(x['id']) == id:
                return {f"Product {id} is: {x['name']}, its price is: {x['price']}. And the calories are {x['calories']} with sugar {x['sugar_content']}g contents."}

# Exception Handler
@app.exception_handler(IDNotFound)
def IDNotExist(request: Request, exc: IDNotFound):
    return JSONResponse (
        status_code= 404,
        content= {
            'Message' : f'Oops ! Product {exc.name} is not on the list, try again please.'
        }
    )
@app.post('/highest')
def highest_class():
    max_calories = 0
    for y in my_items:
        if int(y['calories']) > max_calories:
            max_calories = int(y['calories'])
    return {'Message':f' The highest calories drinks is: {max_calories}.'} 
   
@app.post('/upload')
def Upload_file(file: Union[UploadFile, None] = None):
    if not file:
        return {"message": "No file upload"}
    try:
        file_location = './' + file.filename
        with open(file_location, "wb") as f:
            shutil.copyfileobj(file.file, f)
            file.close()
        my_file_names.append(file.filename)
        return {"Result": "File {file.name} uploaded."}
    except:
        raise UploadFailed(name=f'{file.filename}')

@app.exception_handler(UploadFailed)
def FileNotFound(request: Request, exc: UploadFailed):
    return JSONResponse(
        status_code=404,
        content={
            'Message': f'Sorry, file {exc.name} not uploaded.'
        }
    )
