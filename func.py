import subprocess as sp
try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.table import Table
except ModuleNotFoundError:
    permission = input("\nWill you download rich?(y/n):> ").strip().lower()
    if permission == "y":
        print("Downloading Rich Module...")
        sp.run("python -m pip install rich")
try:
    import requests as rq
except ModuleNotFoundError:
    permission = input("I think the request module is not download\nWill you downlaod(y/n):>").strip().lower()
    if permission == "y":
        print("Module requests is downloading...")
        sp.run("python -m pip install requests")

# Function that gets every info about the usr
def usr_info():
    usr_name = input("Enter Username:>> ").strip()
    response = rq.get(
        f"https://api.github.com/users/{usr_name}"
    )
    if response.status_code == 200:
        data = response.json()
        GIT = f"""
This is Evry thing about {data.get('name')}

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
        
def usr_repo():
    usr = input("Enter the Username:>>").strip()
    repos = rq.get(
        f"https://api.github.com/users/{usr}/repos"
    )
    
    if repos.status_code == 200:
        repo = repos.json()
        print(f"\nRepos of {usr}")
        for r in repo:
            print(f"- {r.get('name')}")
    elif repos.status_code == 404:
        print(f"The user {usr} not found\nCheck the name correctly.")
    else:
        print("Couldn't Fetch Info try again later.")




if __name__ == "__main__":
 usr_info(),usr_repo()
