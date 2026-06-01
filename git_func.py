import requests as rq 

def usr_info():
    usr_name = input("Enter Username:>> ").strip()
    response = rq.get(
        f"https://api.github.com/users/{usr_name}"
    )
    if response.status_code == 200:
        data = response.json()
        GIT = f"""
This Evry thing about {data.get('name')}

Username : {data.get('login')}
ID       : {data.get('id')} 
Name     : {data.get('name')}
Email    : {data.get('email')}
Followers: {data.get('followers')}
Following: {data.get('following')}
Created  : {data.get('created_at')}
Twitter  : {data.get('twitter_username')}
Repos    : {data.get('public_repos')}
Gists    : {data.get('public_gists')}
Bio      : 
{data.get('bio')}
"""
        print(GIT)
    elif response.status_code == 404:
        print("User not found!!")
    else:
        print("UNKNOWN ERROR!!")
        
if __name__ == "__main__":
 usr_info()