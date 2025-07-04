from flask import Flask, render_template
import os

# Initialize the Flask application
app = Flask(__name__)

# Define the main route for the website
@app.route('/')
def home():
    """
    This function handles requests to the root URL ('/').
    It renders the main HTML page for the website.
    The actual date logic is handled by JavaScript in the user's browser.
    """
    return render_template('index.html')

if __name__ == '__main__':
    # Get the port from the environment variable, default to 5000
    port = int(os.environ.get('PORT', 5000))
    # Run the app. '0.0.0.0' makes it accessible from any IP address.
    app.run(host='0.0.0.0', port=port)
