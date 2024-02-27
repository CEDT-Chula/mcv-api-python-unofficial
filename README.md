# Mycoursevile API Python Unofficial
Reverse engineering of the Mycourseville API to create a Python API wrapper.
Developed by CEDT
## Purpose
Interact with the Mycourseville Website in a programmatic way.
As we're a GigaChad Computer Engineering Student, we need to automate everything.
## Installation
```bash
pip install mcv-api-python-unofficial
```
## Disclaimer
This is an unofficial API wrapper and is not affiliated with Mycourseville in any way.
The use of this API wrapper is at your own risk.
We do not take responsibility for any misuse of this API.

## Contributing
### Understanding the Mycourseville Session Structure
Mycourseville was buit using the Laravel Framework.
#### Necessary Cookies
```json
{
    "laravel_session": "string",
    "XSRF-TOKEN": "string",
    "SESSeb912a58562fbbdf6ad5e9a19524d1c0": "string"
}
```
The session is stored in a cookie called `laravel_session` could be obtained by sending a GET request to the Mycourseville website root.
`XSRF-TOKEN` which is used to prevent CSRF attacks was stored on the website login page html as a tag, and could be obtained by parsing the html.
`SESSeb912a58562fbbdf6ad5e9a19524d1c0` is the `session key` obtainable by calling the callback url after logging in with the credentials with `laravel_session` and `XSRF-TOKEN` cookies set.
#### Authentication Flow
with the prerequisites above, we can now authenticate with the Mycourseville API.
but in practice, we need to obtain those cookies first.
by following the steps below:
1. Intialize a new session this could be done using the `requests.Session()` object or any other library that supports session management.
2. Send a GET request to the Mycourseville website root to obtain `laravel_session` cookies (although any page would work, the root page is the most reliable)
3. Extract the `XSRF-TOKEN` cookies from the response headers and store them in the session object. (was stored in the `<input type="hidden" name="_token" value="randomstring">` tag)
4. Send a POST request to the Mycourseville login page with the credentials and the cookies set. for example:
To `https://www.mycourseville.com/api/chulalogin` with the following cookies:
```json
{
    "laravel_session": "string",
    "XSRF-TOKEN": "string",
}
```
5. Locate the link in `เข้าใช้งาน` button located in `https://www.mycourseville.com/api/` to obtain the `Session Key` cookies. simply jsut by doing get request to the link referenced in the button.
this usually be `https://www.mycourseville.com/api/oauth/authorize` with a lot of`?params=...` as the query string.
6. Now your session should have the necessary cookies to authenticate with the Mycourseville API.
7. You could now implemented a custom beautifulsoup parser to parse the html to get the information you need from the website.