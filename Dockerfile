FROM tiangolo/uvicorn-gunicorn:python3.7-alpine3.8

RUN apk -U add chromium udev ttf-freefont msttcorefonts-installer
RUN update-ms-fonts && fc-cache -f

COPY requirements.txt /

RUN pip install --upgrade pip
RUN pip install -r /requirements.txt

WORKDIR /app

COPY app.py /app

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8989"]
