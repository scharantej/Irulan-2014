
# Import necessary libraries
from flask import Flask, render_template

# Create a Flask application
app = Flask(__name__)

# Define the main route
@app.route('/')
def index():
    """
    This function handles requests to the main page.
    
    Returns:
        A rendered HTML template showcasing the landing page for Dune: Imperium.
    """
    
    return render_template('index.html')

# Run the application
if __name__ == '__main__':
    app.run()
