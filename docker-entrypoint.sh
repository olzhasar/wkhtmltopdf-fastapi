#!/bin/sh

port=${PORT-8000};
workers=${WORKERS-4};

uvicorn app:app --host=0.0.0.0 --port=$port --workers=$workers
