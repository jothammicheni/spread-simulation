from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

# Define a route for the root URL '/'
@app.route('/')
def hello_world():
    return "Hello, World!"

# This block ensures that the server only runs if the script is executed directly
if __name__ == "__main__":
    # Run the Flask application in debug mode on localhost port 5000
    app.run(debug=True)
