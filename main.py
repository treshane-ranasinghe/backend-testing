from fastapi import FastAPI

app = FastAPI() # very important

@app.get("/") # @app = is the decorater
def read_root():
    return {"message": "Hello, FastAPI"} 


@app.get("/about") # none as the path
def about(): # path operation function 
    return { 'data': {'name':'Treshane'}}