import uvicorn
from fastapi import FastAPI

from routers import flights as flights_router


app = FastAPI()


@app.get("/")
def get_root():
    return "The server is running."


app.include_router(flights_router.router)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
