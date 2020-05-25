import requests
import json

def read_username():
    username = input("Please insert the username that you want to search: ")
    if username is None or len(username) == 0:
        print("The username can't be blank")
        read_username()
    else:
        return username


def read_json(filename):
    with open(filename) as json_file:
        data = json.load(json_file)
        return data

def check_profile(username, sm_name, url):
    request = requests.get(url + username)
    if request.status_code == 200:
        return sm_name + " : " + url + username
    else:
        return (sm_name) 

print("Welcome to CodeWithMojo Social Spider")
print("*************************************")

username = read_username()
social_media_list = read_json("assets/social_media_urls.json")
success = ""
fails = []

print("Username: " + username)
for social_media in social_media_list:
    r = check_profile(username, social_media['name'], social_media['url']) + "\n"
    if (":" in r):
        success += r
    else:
        fails.append(r)

if len(fails) > 0:
    success += "\nNot found username " + username + " in : \n"
    
    for fail in fails:
        success += fail

print (success)