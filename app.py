import pdfkit
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
def index(data: PostData):
    pdf = pdfkit.from_url(data.url, False)
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
