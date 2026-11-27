from fastapi import FastAPI
import json

app=FastAPI()

@app.get("/")
def hello():
    return{'msg':"hii"}


@app.get('/a')
def about():
    return{'msg':'vedika'}

def load_json():
    with open("stu_info.json",r):
        

