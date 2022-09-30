from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def get_root():
    return {"msg": "Hello, data science."}
