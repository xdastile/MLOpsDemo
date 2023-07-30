#!/bin/bash
set -e
. /venv/bin/activate
uvicorn src.app:app --host 0.0.0.0 --port 80
