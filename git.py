import requests as rq

usr_name = input("Enter Username : ").strip()

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
else:
    print("Retry!!")
