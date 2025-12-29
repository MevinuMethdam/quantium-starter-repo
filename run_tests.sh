#!/bin/bash

source venv/Scripts/activate

pytest test_app.py

if [ $? -eq 0 ]; then
    echo "Tests passed successfully!"
    exit 0
else
    echo "Tests failed!"
    exit 1
fi