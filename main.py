from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def root():
    return {"message": "hello from fast api"}


if __name__ == '__main__':
    uvicorn.run(app,host='0.0.0.0',port=8002)