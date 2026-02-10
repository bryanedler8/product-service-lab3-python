from flask import Flask, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv

# Load environment variables from .env file (for local development)
load_dotenv()

app = Flask(__name__)

# Configure CORS to allow any origin
CORS(app, resources={r"/*": {"origins": "*", "methods": ["GET"]}})

@app.route('/products', methods=['GET'])
def get_products():
    """Return a list of products as JSON"""
    products = [
        {"id": 1, "name": "Dog Food", "price": 19.99},
        {"id": 2, "name": "Cat Food", "price": 34.99},
        {"id": 3, "name": "Bird Seeds", "price": 10.99}
    ]
    return jsonify(products)

if __name__ == '__main__':
    # Get port from environment variable or default to 3030
    port = int(os.environ.get('PORT', 3030))
    
    # For local development, use debug mode
    # For production on Azure, Gunicorn will handle the server
    debug = os.environ.get('FLASK_ENV') == 'development'
    
    app.run(host='0.0.0.0', port=port, debug=debug)