#!/bin/bash
set -e
echo "Starting AI-Powered Health Risk Predictor..."
uvicorn app:app --host 0.0.0.0 --port 9095 --workers 1
