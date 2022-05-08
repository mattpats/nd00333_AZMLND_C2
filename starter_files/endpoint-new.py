import urllib.request
import json
import os
import ssl
def allowSelfSignedHttps(allowed):
    # bypass the server certificate verification on client side
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context
allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.
# Request data goes here
data = {
    "Inputs": {
        "data":
        [
            {
                "age": 17,
                "job": "blue-collar",
                "marital": "married",
                "education": "university.degree",
                "default": "no",
                "housing": "yes",
                "loan": "yes",
                "contact": "cellular",
                "month": "may",
                "day_of_week": "mon",
                "duration": 971,
                "campaign": 1,
                "pdays": 999,
                "previous": 1,
                "poutcome": "failure",
                "emp.var.rate": -1.8,
                "cons.price.idx": 92.893,
                "cons.conf.idx": -46.2,
                "euribor3m": 1.299,
                "nr.employed": 5099.1
            },
	    {
                "age": 87,
                "job": "blue-collar",
                "marital": "married",
                "education": "university.degree",
                "default": "no",
                "housing": "yes",
                "loan": "yes",
                "contact": "cellular",
                "month": "may",
                "day_of_week": "mon",
                "duration": 471,
                "campaign": 1,
                "pdays": 999,
                "previous": 1,
                "poutcome": "failure",
                "emp.var.rate": -1.8,
                "cons.price.idx": 92.893,
                "cons.conf.idx": -46.2,
                "euribor3m": 1.299,
                "nr.employed": 5099.1
            },
        ]
    },
    "GlobalParameters": {
        "method": "predict"
    }
}
body = str.encode(json.dumps(data))
url = 'http://79c06ab4-0c05-4797-b3d9-eeecb1deb056.southcentralus.azurecontainer.io/score'  # Replace this 
api_key = '' # Replace this with the API key for the web service
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}
req = urllib.request.Request(url, body, headers)
try:
    response = urllib.request.urlopen(req)
    result = response.read()
    print(result)
except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))
    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())
    print(error.read().decode("utf8", 'ignore'))