import re
from flask import Flask, request
import requests
import json

app = Flask(__name__)

@app.route("/api", methods=['GET'])
def api_main():
    uid, lat, lon = None, None, None
    args = request.args 
    if "uid" in args:
        uid = args["uid"]
    if "lat" in args:
        lat = args["lat"]
    if "lon" in args:
        lon = args ["lon"]
    if lat == None or uid == None or lon == None:
        return 400
    key = "AIzaSyAMCYVYNVINDg2taIs7FhlxtUKb9apJOSs"
    req_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={0},{1}&radius=10&key={2}".format(lat,lon,key)
    response = requests.get(req_url).json()
    results = response["results"]
    
    for location in results:
        if "business_status" in location:
            print(location["types"])
        
    return response

    
if __name__ == "__main__":
    app.run(debug=True)