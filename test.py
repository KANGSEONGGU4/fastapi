from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

app = FastAPI()

# HTML 파일 제공
@app.get("/", response_class=HTMLResponse)
async def read_index():
    with open("index.html", "r") as file:
        return file.read()

# POST 요청 처리
@app.post("/submit")
async def submit_form(request: Request):
    form_data = await request.form()
    print(form_data)
    name = form_data.get("name")
    print(name)
    return {"message": f"Hello, {name}!"}
