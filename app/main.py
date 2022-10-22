import uvicorn

from fastapi import FastAPI

app = FastAPI()


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, host="0.0.0.0", reload=True)
