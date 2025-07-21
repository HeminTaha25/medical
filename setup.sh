#!/bin/bash
# MediLab Pro Flask Application Setup Script

echo "🧪 MediLab Pro - Medical Laboratory Website Setup"
echo "=================================================="

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

# Check Python version
python_version=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
echo "✅ Python $python_version detected"

# Create virtual environment if it doesn't exist
if [ ! -d "medilabpro_env" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv medilabpro_env
    if [ $? -eq 0 ]; then
        echo "✅ Virtual environment created successfully"
    else
        echo "❌ Failed to create virtual environment"
        exit 1
    fi
else
    echo "✅ Virtual environment already exists"
fi

# Activate virtual environment and install dependencies
echo "📥 Installing dependencies..."
source medilabpro_env/bin/activate

pip install -r requirements.txt
if [ $? -eq 0 ]; then
    echo "✅ Dependencies installed successfully"
else
    echo "❌ Failed to install dependencies"
    exit 1
fi

# Create .env file if it doesn't exist
if [ ! -f ".env" ]; then
    echo "⚙️  Creating environment configuration..."
    cp .env.example .env
    echo "✅ Created .env file from template"
    echo "📝 Please edit .env file to configure your settings"
else
    echo "✅ Environment configuration already exists"
fi

echo ""
echo "🎉 Setup completed successfully!"
echo ""
echo "To run the application:"
echo "1. Activate the virtual environment: source medilabpro_env/bin/activate"
echo "2. Run the application: python app.py"
echo "3. Open your browser to: http://localhost:5000"
echo ""
echo "For more information, see README_FLASK.md"