# URLShortner

A Django RESTful API based url shortner application consisting of two majot API endpoints:

# API Endpoint I) POST Request: urlshortner/mini/

EG: Request body: {"url": "https://www.xyz.com"}  

# API Endpoint II) GET Request: urlshortner/<miniURL>

EG: Parameter argument: urlshortner/1Ulee
     

# Application Workflow

1. User invokes API Endpoint I, request redirected to MiniURLView.
2. Insert a record ie. Original URL into SQLite database
3. Insert a URL ID (generated using random.getrandbits(8)) associated with that original URL in URLID model
4. Pass the URL ID generated into encode_func(ref_id) wherein, python oct() function to create a shortned url value
5. Return the shortend url to the User as a return value of the POST request
6. User invokes API Endpoint II, request redirected to RedirectURLView
7. Extract URL (passed as an argument) and pass it into decode_func(miniURL) wherein, python int(url, 8) function re-generates the ref_id value
8. Fetch the ref_id -> Fetch the Original URL (associated with it) -> Simple Redirect to Website

# Development 

POSTMAN API Tool to create request body and receive response from API endpoints created

# Testing

MiniURLTestCase(APITestCase) and RedirectURLTestCase(APITestCase) test classes developed and tested successfully.

Python Coverage test tool utilized. Code coverage achieved: 97%.

# Setup and Installation

1. Create virtual environment
2. Run requirements.txt file (install Python packages as req.)
3. Make database migrations
4. Execute API endpoints using POSTMAN tool
5. Test API endoints with the command: manage.py test URLShortner.tests

# Deployment

Since URL Shortner is a small Django application, it would be suitable to deploy it on Free-of-cost platforms eg. Heroku

