from fastapi import FastAPI, UploadFile, File, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from src.helper import parse_file, query_financial_llm
import pandas as pd

app = FastAPI()
templates = Jinja2Templates(directory="frontend/")

df_store = {}


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request,
        "upload_result": "",
        "query_result": ""
    })


@app.post("/upload")
async def upload(request: Request, file: UploadFile = File(...)):
    try:
        contents = await file.read()
        df = parse_file(file.filename, contents)
        df_store["data"] = df
        upload_message = f"✅ Successfully uploaded: {file.filename}"
    except Exception as e:
        upload_message = f"❌ Upload failed: {str(e)}"

    return templates.TemplateResponse("index.html", {
        "request": request,
        "upload_result": upload_message,
        "query_result": ""
    })


@app.post("/query", response_class=HTMLResponse)
async def query(request: Request, prompt: str = Form(...)):
    if "data" not in df_store:
        return templates.TemplateResponse("index.html", {
            "request": request,
            "upload_result": "",
            "query_result": "❗ Please upload a file first."
        })

    df = df_store["data"]
    result = query_financial_llm(df, prompt)

    if "error" in result:
        result_text = result["error"]
    else:
        result_text = "\n".join([f"{k}: {v}" for k, v in result.items()])

    return templates.TemplateResponse("index.html", {
    "request": request,
    "upload_result": "✅ File already uploaded.",
    "query_result": result_text,
    "prompt": prompt   
})

