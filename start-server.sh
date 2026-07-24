#!/bin/bash
# Simple launcher script for the submission server

PORT=${1:-8000}

echo "🚀 Starting Project 01 Submission Server..."
echo "📍 Access at: http://localhost:$PORT"
echo ""

python3 submit_server.py "$PORT"
