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