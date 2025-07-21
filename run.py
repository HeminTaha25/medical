#!/usr/bin/env python3
"""
Simple runner script for MediLab Pro Flask Application
"""

import os
import sys
from app import app

def main():
    """Run the Flask application"""
    print("Starting MediLab Pro Flask Application...")
    print(f"Application will be available at: http://localhost:5000")
    print("Press CTRL+C to stop the application")
    
    # Set environment variables for development
    os.environ.setdefault('FLASK_ENV', 'development')
    os.environ.setdefault('FLASK_DEBUG', 'True')
    
    try:
        app.run(debug=True, host='0.0.0.0', port=5000)
    except KeyboardInterrupt:
        print("\nApplication stopped by user")
        sys.exit(0)
    except Exception as e:
        print(f"Error starting application: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()