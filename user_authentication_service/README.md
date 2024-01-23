# User authentication service

### How to Declare API Routes in a Flask App:

In Flask, you declare API routes using the `@app.route` decorator.
- This decorator allows you to define which URL should trigger a specific function or view.

For example, you can declare a route like this:

``` python
@app.route('/api/user', methods=['GET'])
def get_user():
    # Your code to handle the GET request for '/api/user' goes here
```

In this example, when a GET request is made to the '/api/user' URL, the get_user function will be executed.

### How to Get and Set Cookies:

You can work with cookies in Flask using the request and response objects.

- To get a cookie's value from an incoming request, you can use `request.cookies.get('cookie_name')`.
- To set a cookie in a response, you can use the `make_response` method, like this:

```python

from flask import make_response

response = make_response('Response content')
response.set_cookie('cookie_name', 'cookie_value')
return response
```

### How to Retrieve Request Form Data:

To retrieve form data from a POST request in Flask, you can use the `request.form` object.

For example, if you have a form with fields 'username' and 'password', you can retrieve their values like this:

``` python

username = request.form.get('username')
password = request.form.get('password')
```

Make sure to set the method attribute of your HTML form to 'POST' when submitting data.

### How to Return Various HTTP Status Codes:

In Flask, you can return various HTTP status codes using the return statement in your view functions.

For example:

- to return a '200 OK' response:
``` python

return 'Success', 200
```

- To return a '201 Created' response:
``` python
return 'Resource Created', 201
```

- For errors, you can return appropriate status codes along with error messages:
``` python
return 'Bad Request', 400
```

Flask provides built-in constants for common HTTP status codes like 
- HTTP_200_OK
- HTTP_201_CREATED
- HTTP_400_BAD_REQUEST

which you can use for clarity.
