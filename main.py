from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI"} 


@app.get("/about")
def about():
    return { 'data': {'name':'Treshane'}}