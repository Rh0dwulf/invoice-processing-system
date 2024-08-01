#!/bin/bash

# Check if conda is available
if command -v conda &> /dev/null; then
    echo "Conda is available. Setting up environment..."
    
    # Create conda environment
    conda create -n invoice_processor python=3.9 -y
    
    # Activate environment
    source $(conda info --base)/etc/profile.d/conda.sh
    conda activate invoice_processor
    
    # Install requirements
    pip install -r requirements.txt
else
    echo "Conda is not available. Please set up the environment manually."
    echo "See README.md for manual setup instructions."
fi

# Set environment variables
echo "CLIENT_ID_ENV=your_client_id" >> .env
echo "CLIENT_SECRET_ENV=your_client_secret" >> .env
echo "USERNAME_ENV=your_username" >> .env
echo "API_KEY_ENV=your_api_key" >> .env

echo "Environment variables set in .env file."
echo "Please edit .env file with your actual API credentials."