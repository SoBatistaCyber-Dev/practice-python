'''
    Exercise: Create a Flask Endpoint
    Description:

    Your task is to create a simple web server using the Flask framework in Python. The server should expose a single GET endpoint that returns the text "Hello, World!" when accessed.
    Task:

        Install Flask if you don't already have it (pip install flask).
        Create a Python script that:
            Initializes a Flask app.
            Defines a GET endpoint at the root URL (/).
            When the endpoint is accessed, it should return the string "Hello, World!".
        Run the Flask application and ensure it listens on http://127.0.0.1:5000/.

    Example Output:

    When accessing http://127.0.0.1:5000/ in a browser or using a tool like curl:

    curl http://127.0.0.1:5000/

    The output should be:

    Hello, World!

    Bonus Challenge:

    Modify the endpoint to accept an optional query parameter name, and return a personalized greeting. For example:

        Accessing / still returns "Hello, World!".
        Accessing / with ?name=Alice should return "Hello, Alice!".
'''

from flask import Flask, request, jsonify

app = Flask(__name__)

def reverse_string(input_string):
    return input_string[::-1]

@app.route("/")
def home():
    name = request.args.get("name", "World")
    return f"Hello {name}!", 200
    
@app.route("/reverse-string")
def reverse():
    string_to_reverse = request.args.get("string", "World")
    return f"This is the reverted string: {reverse_string(string_to_reverse)}!", 200


if __name__ == "__main__":
    app.run(debug=True )