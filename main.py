from fastapi import FastAPI

app = FastAPI() # very important

@app.get("/blog") # @app = is the decorater . ? query parameter
def index(limit):
    # only get 10 published blogs
    return {'data': f'{limit} blog list'} 


@app.get("/blog/{id}") # none as the path
def about(id : int): # path operation function . fastapi converts sting into int automatically when declared in the parenthesis
    return { 'data': id }


@app.get("/blog/{id}/comments") # with a parameter {id}
def comments(id):
    # fectch comments of blog woth id = id
    return {'data':  {'1', '2'}}

@app.get("/blog/unpublished")
def unpublished():
    return { 'data': 'all unpublished blogs '}