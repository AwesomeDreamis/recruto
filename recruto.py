from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get('/url_name/')
def hello(name: str = 'name', message: str = 'message'):
    return f'Hello {name}! {message}!'


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
