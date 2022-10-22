import re
from flask import Flask, request, g
import sqlite3
import requests
import json

app = Flask(__name__)

DATABASE = "database.db"

BAD_STORES = ["walmart","target"]

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def query_db(query, args=()):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return rv

def list_to_types(name, types):
    for store in BAD_STORES:
        if store in name:
            return "no_type"
    if "restraunt" in types:
        return "restraunt"
    elif "gas-station" in types:
        return "gas"
    elif "grocery_or_supermarket" in types:
        return "grocery"
    elif "pharmacy" in types:
        return "pharmacy"
    else:
        return "no_type"

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
    file = open("key.txt", "r")
    key = file.readline()
    req_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={0},{1}&radius=10&key={2}".format(lat,lon,key)
    response = requests.get(req_url).json()
    results = response["results"]
    name = ""
    business_type = ""
    for location in results:
        if "business_status" in location:
            name = location["name"].lower()
            business_type = list_to_types(name, location["types"])          
            break
    userEntry = query_db("SELECT * FROM users WHERE userid=?", (uid,))
    if userEntry == []:
        return 401
    ccids = userEntry[0][1].split(",")
    best_cc = 0
    best_rate = 0
    for ccid in ccids:
        ccinfo      = query_db("SELECT * FROM cards WHERE id=?",(ccid,))
        specials    = ccinfo[0][1].split(",")
        categories  = ccinfo[0][2].split(",")
        base        = float(ccinfo[0][3])
        for special in specials:
            entry = special.split(":")
            special_location = entry[0]
            reward = float(entry[1])
            
            print(entry)
            print(name)
            print(business_type)
            if special_location in name:
                if reward > best_rate:
                    best_cc = ccid
                    best_rate = reward
        for category in categories:
            entry = category.split(":")
            category_type = entry[0]
            reward = float(entry[1])
            if category_type == business_type:
                if reward > best_rate:
                    best_cc = ccid
                    best_rate = reward         
        if base > best_rate:
            best_cc = ccid
            best_rate = base
    return best_cc

    
if __name__ == "__main__":
    app.run(debug=True)
    
    

    