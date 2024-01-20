# SESSION AUTHENTICATION

### Authentication:

__Definition:__

 Authentication is the `process of verifying the identity of a user or system to ensure that they are who they claim to be.` It is a fundamental aspect of security in computer systems and applications.

__Purpose:__

 Authentication helps protect resources and data from unauthorized access. It ensures that only authorized users or systems can access certain information or perform specific actions.

### Session Authentication:

**Definition:**

 Session authentication is a `method of authentication that involves creating a session for a user after they successfully log in`. This session typically includes a session identifier or token that is used to identify the user for the duration of their interaction with a web application.

**Purpose:**

 Session authentication helps maintain a user's identity throughout their session without requiring them to repeatedly enter their credentials. It is commonly used in web applications to keep users logged in until they explicitly log out or their session expires.

### Cookies:

**Definition:**

 Cookies are `small pieces of data that a web server sends to a user's web browser and are stored on the user's device.` They are often used to track user interactions and store information about the user's session.

**Purpose:**

 Cookies have various purposes, including session management, user tracking, personalization, and authentication. They are commonly used to store session identifiers or tokens to facilitate session authentication.

### How to Send Cookies:

Cookies are sent from a web server to a user's browser as part of the HTTP response. To send cookies, the server includes a Set-Cookie header in the response with the cookie's name and value.

For example:

``` css
Set-Cookie: username=johndoe; expires=Wed, 19 Jan 2025 12:00:00 GMT; path=/
```

The browser will then store this cookie and include it in subsequent requests to the same domain.

### How to Parse Cookies:

To parse cookies in a web application, you typically access them from the
document.cookie property in JavaScript on the client side or from the
server-side framework you're using.

In JavaScript, you can parse cookies like this:

``` javascript
const cookies = document.cookie.split('; ');
const cookieObject = {};
cookies.forEach(cookie => {
  const [name, value] = cookie.split('=');
  cookieObject[name] = value;
});
// Now you can access individual cookies using their names, e.g., cookieObject.username
```

The concepts are crucial for understanding how authentication and session management work in web applications and how cookies play a role in maintaining user sessions and identity.
