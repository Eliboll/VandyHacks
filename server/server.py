import re
from flask import Flask, request, g, jsonify
import sqlite3
import requests
import json
import os
from twilio.rest import Client



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
    if "restaurant" in types:
        return "restaurant"
    elif "gas_station" in types:
        return "gas"
    elif "grocery_or_supermarket" in types:
        return "grocery"
    elif "pharmacy" in types:
        return "pharmacy"
    else:
        return "no_type"

@app.route("/api", methods=['GET'])
def api_main():
    #**********************************
    #Verify input data
    #**********************************
    uid, lat, lon = None, None, None
    args = request.args 
    if "uid" in args:
        uid = args["uid"]
    if "lat" in args:
        lat = args["lat"]
    if "lon" in args:
        lon = args ["lon"]
    if lat == None or uid == None or lon == None:
        return_data = { "code" : 400 }
        return jsonify(return_data)
    #**********************************
    #Get location info from google API
    #**********************************
    file = open("key.txt", "r")
    credentials = file.readlines()
    file.close()
    key = credentials[0]
    req_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={0},{1}&radius=6&key={2}".format(lat,lon,key)
    response = requests.get(req_url).json()
    results = response["results"]
    #**********************************
    #Filter out non buisnesses
    #**********************************
    name = ""
    business_type = ""
    FLAG = 0
    for location in results:
        if "business_status" in location:
            
            name = location["name"].lower().replace("'","")
            business_type = list_to_types(name, location["types"])     
            FLAG = 1
            break
    if  FLAG==0: #returnif its not a buisness
        return_data = { "code" : 100 }
        return jsonify(return_data)
    #**********************************
    #get list of credit cards per specific user
    #**********************************
    userEntry = query_db("SELECT * FROM users WHERE userid=?", (uid,))
    if userEntry == []:
        return_data = { "code" : 401 }
        return jsonify(return_data)
    ccids = userEntry[0][1].split(",")
    print(userEntry)
    last_location = userEntry[0][2]
    if name==last_location or name=="":
        return_data = { "code" : 100 }
        return jsonify(return_data)
    
    connection = sqlite3.connect('database.db')
    cur = connection.cursor()
    cur.execute("UPDATE users SET last_location = '{}' WHERE userid={}".format(name,uid))
    connection.commit()
    connection.close()
    
    #**********************************
    #select best credit card
    #**********************************
    
    best_cc = 0
    best_rate = 0
    best_name =  0
    for ccid in ccids:
        ccinfo      = query_db("SELECT * FROM cards WHERE id=?",(ccid,))
        specials    = ccinfo[0][1].split(",")
        categories  = ccinfo[0][2].split(",")
        base        = float(ccinfo[0][3])
        cc_name     = ccinfo[0][4]
        for special in specials:
            if special == "":
                continue
            entry = special.split(":")
            special_location = entry[0]
            reward = float(entry[1])
            if special_location in name:
                if reward > best_rate:
                    best_name = cc_name
                    best_cc = ccid
                    best_rate = reward
        for category in categories:
            if category == "":
                continue
            entry = category.split(":")
            category_type = entry[0]
            reward = float(entry[1])
            if category_type == business_type:
                if reward > best_rate:
                    best_name = cc_name
                    best_cc = ccid
                    best_rate = reward         
        if base > best_rate:
            best_name = cc_name
            best_cc = ccid
            best_rate = base
            
    #**********************************
    # Set up Return data
    #**********************************
    account_sid = credentials[1]
    auth_token = credentials[2]
    file.close()
    client = Client(account_sid, auth_token)
    
    message = client.messages \
                .create(
                     body="Use your {} card at {}".format(best_name,name),
                     from_='+13143505427',
                     to='+1{}'.format(userEntry[0][3])
                 )

    print(message.sid)
    
    return_data = {
        "code" : 200,
        "cc_name" : best_name,
        "buisiness_name" : name           
                   }
    return jsonify(return_data)

    
if __name__ == "__main__":
    app.run(debug=True)
    
    

    