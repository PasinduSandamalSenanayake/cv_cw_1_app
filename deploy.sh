#!/bin/bash

# Deployment script for Streamlit Cloud
echo "🚀 Preparing for Streamlit Cloud deployment..."

# Check if required files exist
required_files=("app.py" "requirements.txt" "my_model.h5")
for file in "${required_files[@]}"; do
    if [ ! -f "$file" ]; then
        echo "❌ Error: $file is missing!"
        exit 1
    else
        echo "✅ $file found"
    fi
done

# Check Python version
python_version=$(python --version 2>&1 | awk '{print $2}')
echo "🐍 Python version: $python_version"

# Test imports
echo "🔍 Testing imports..."
python -c "
import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np
print('✅ All imports successful!')
"

# Check model loading
echo "🤖 Testing model loading..."
python -c "
from tensorflow.keras.models import load_model
model = load_model('my_model.h5')
print('✅ Model loaded successfully!')
print(f'Model input shape: {model.input_shape}')
"

echo ""
echo "🎉 Ready for deployment!"
echo ""
echo "📝 Next steps:"
echo "1. Push all changes to GitHub:"
echo "   git add ."
echo "   git commit -m 'Ready for deployment'"
echo "   git push origin main"
echo ""
echo "2. Go to https://share.streamlit.io"
echo "3. Connect your GitHub repository"
echo "4. Set main file path to: app.py"
echo "5. Deploy!"
