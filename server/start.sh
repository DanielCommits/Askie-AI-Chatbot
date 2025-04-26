#!/bin/bash

# Use port 8000 locally if $PORT is not set
PORT=${PORT:-8000}

# Start the server
uvicorn server:app --host 0.0.0.0 --port $PORT
