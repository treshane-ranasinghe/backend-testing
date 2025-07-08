from fastapi import FastAPI

app = FastAPI() # very important

@app.get("/") # @app = is the decorater
def read_root():
    return {"data": "blog list"} 


@app.get("/blog/{id}") # none as the path
def about(id): # path operation function 
    return { 'data': id }


@app.get("/blog/{id}/comments") # with a parameter {id}
def comments(id):
    # fectch comments of blog woth id = id
    return {'data':  {'1', '2'}}