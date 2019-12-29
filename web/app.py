# import libraries

from flask import Flask, jsonify, request # request is different from requests
from flask_restful import Api, Resource
from pymongo import MongoClient
import bcrypt # for hashing the password
import requests # used to download image from web and get the content
import json
import subprocess

app = Flask(__name__)
api = Api(app) # initialize that this app would be an api

client = MongoClient("mongodb://db:27017") # connecting mkongodb to our database db at the default port

db = client.ImageRecognitionDB
users = db["users"] # our collection users


def userExists(username):
    if users.find({"username": username}).count() == 0:
        return False
    else:
        return True

# Resource Register
class Register(Resource):
    def post(self):
        namepass = request.get_json()
        username = namepass["username"]
        password = namepass["password"]

        # check if the user already exists
        if userExists(username):
            retJson = {
                "statuscode" : 301,
                "message" : "User Already exists"
            }
            return jsonify(retJson)

        hashedpw = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())
        users.insert({
            "username" : username,
            "password" : hashedpw,
            "tokens" : 2
        })
        retJson = {
            "statuscode" : 200,
            "message" : "you successfuly signed up for the api"
        }
        return jsonify(retJson)


def verifypw(username, password):
    hashed_pw = users.find({
        "username" : username
    })[0]["password"]

    if bcrypt.hashpw(password.encode('utf8'), hashed_pw) == hashed_pw:
        return True
    else:
        return False

def countTokens(username):
    num_tokens = users.find({
        "username" : username
    })[0]["tokens"]
    return num_tokens


# resource classify
class Classify(Resource):
    def post(self):
        namepassimg = request.get_json()
        username = namepassimg["username"]
        password = namepassimg["password"]
        imgurl = namepassimg["imgurl"]

        if not userExists(username):
            retJson = {
                "statuscode" : 301,
                "message" : "User does not exit"
            }
            return jsonify(retJson)

        correct_pw = verifypw(username, password)
        if not correct_pw :
            retJson = {
                "statuscode" : 302,
                "message" : "Incorrect password"
            }
        
        num_tokens = countTokens(username)
        if num_tokens <= 0 :
            retJson = {
                "statuscode" : 303,
                "message" : "Out of tokens, please refill"
            }
            return jsonify(retJson)


        img = requests.get(imgurl)
        retJson = {}
        
        # store a temperory image, write into temp img the content of url img
        # a new subprocess and write the command for the process and pass the arguments for the command
        # wait untill the subprocess is done 
        # 
        with open("temp.jpg", "wb") as f:   # open temp file temp.jpg and write the content of image in that file
            f.write(img.content)
            process = subprocess.Popen('python classify_image.py --model_dir =. --image_file=./temp.jpg', shell=True)
            process.communicate()[0]
            process.wait()

            # after the process is finished, we open the file (text.txt) that te classify_image has written and we get the json file from it
            with open("text.txt") as g:
                retJson = json.load(g)


        # deduct one token as service charge
        new_tokens =  num_tokens -1
        users.update({
            "username":username,
        },
        {
            "$set": {
                "tokens" : new_tokens
            }
        }
        )
        return retJson


# Resource refill
class Refill(Resource):
    def post(self):
        namepassref = request.get_json()
        username = namepassref["username"]
        admin_password = namepassref["admin_password"]
        refill_amt = namepassref["refill_amt"]

        if not userExists(username):
            retJson = {
                "statuscode" : 301,
                "message" : "User does not exit"
            }
            return jsonify(retJson)
        
        correct_admin_password = "Admiral123"

        if not correct_admin_password == admin_password:
            retJson = {
                "statuscode" : 304,
                "message" : "Invalid admin password"
            }
            return jsonify(retJson)

        num_tokens = countTokens(username)

        users.update({
            "username":username,
        },
        {
            "$set": {
                "tokens" : num_tokens + refill_amt
            }
        }
        )

        retJson = {
            "statuscode" : 200,
            "message" : "Tokens refilled successfully"
        }
        return jsonify(retJson)

api.add_resource(Register, "/register")
api.add_resource(Classify, "/classify")
api.add_resource(Refill, "/refill")

if __name__ == "__main__":
    app.run(host="0.0.0.0")



