from pyppeteer.launcher import launch
from fastapi import FastAPI
from pydantic import BaseModel
from starlette.responses import Response

app = FastAPI(
    docs_url="/print_service/docs",
    openapi_url="/print_service/openapi.json"
)


class PostData(BaseModel):
    url: str
    filename: str = "result"


@app.post("/")
async def index(data: PostData):
    browser = await launch(
        headless=True,
        executablePath="/usr/bin/chromium-browser",
        args=['--no-sandbox', '--disable-gpu']
    )
    page = await browser.newPage()
    await page.goto(data.url)
    pdf = await page.pdf({'path': 'page.pdf', 'format': 'A4'})
    filename = data.filename or "output"
    response = Response(
        pdf,
        headers={
            "Content-Type": "application/pdf",
            "Content-Disposition": f"attachment; filename={filename}.pdf",
            "Content-Length": str(len(pdf)),
        },
    )
    return response
