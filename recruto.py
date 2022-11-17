from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get('/url_name/')
def hello(name: str = 'name', message: str = 'message'):
    return f'Hello {name}! {message}!'
