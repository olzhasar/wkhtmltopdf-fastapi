# wkhtmltopdf_fastapi

Simple http API service around wkhtmltopdf. Receives url of the webpage in a POST request and returns generated pdf file.

## Features:

- API powered by [FastAPI](https://github.com/tiangolo/fastapi)
- Lightweight resulting container (less than 300 MB including fonts). Docker image based on [docker-alpine-wkhtmltopdf](https://github.com/madnight/docker-alpine-wkhtmltopdf)
- Includes Windows fonts (msttcorefonts package)
