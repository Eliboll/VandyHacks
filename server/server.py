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
    
    key = "AIzaSyAMCYVYNVINDg2taIs7FhlxtUKb9apJOSs"
    req_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={0},{1}&radius=10&key={2}".format(lat,lon,key)
    response = requests.get(req_url).json()
    print(response["results"])
    return response#["results"]
    #return "{},latitude = {}, longitute = {}".format(uid,lat,lon)
    
if __name__ == "__main__":
    app.run(debug=True)