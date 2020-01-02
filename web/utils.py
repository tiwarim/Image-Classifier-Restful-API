# importing libraries and helper functions
from sys_utils import *

# Resource Register
"""
    Resource Register takes input on a POST protocol and creates new accounts 
    Parameters:
        namepass: contains username and password of the user <JSON>
    Returns:
        retJson: contains status code and message <JSON>
"""
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


# resource classify
"""
    Resource Classify takes input on a POST protocol and returns categories with a score
    Parameters:
        namepassimg: contains username, password of the user and image url <JSON>
    Returns:
        retJson: contains status code and message <JSON>
"""
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
"""
    Resource Refill takes input on a POST protocol and adds to the existing tokens 
    Parameters:
        namepassref: contains username, admin password and refill amount <JSON>
    Returns:
        retJson: contains status code and message <JSON>
"""
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

