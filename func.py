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

console = Console()

# Function that gets every info about the usr
def usr_info():
    console.print("[cyan]Enter Username:[/cyan]")
    usr_name = input(">> ").strip()
    response = rq.get(
        f"https://api.github.com/users/{usr_name}"
    )
    if response.status_code == 200:
        data = response.json()
        GIT = f"""
This is Evry thing about {data.get('name')}

[green]Username[/green] : {data.get('login')}
[green]ID[/green]       : {data.get('id')} 
[green]Name[/green]     : {data.get('name')}
[green]Email[/green]    : {data.get('email')}
[green]Followers[/green]: {data.get('followers')}
[green]Following[/green]: {data.get('following')}
[green]Created[/green]  : {data.get('created_at')}
[green]Twitter[/green]  : {data.get('twitter_username')}
[green]Repos[/green]    : {data.get('public_repos')}
[green]Gists[/green]    : {data.get('public_gists')}
[green]Bio[/green]      : 
{data.get('bio')}
"""
        console.print(Panel(GIT, border_style="cyan"))
    elif response.status_code == 404:
        console.print("[red]User not found!![/red]")
    else:
        console.print("[yellow]UNKNOWN ERROR!![/yellow]")
        
def usr_repo():
    console.print("[cyan]Enter the Username[/cyan]:")
    usr = input(">>").strip()
    repos = rq.get(
        f"https://api.github.com/users/{usr}/repos"
    )
    
    if repos.status_code == 200:
        repo = repos.json()
        console.print(f"\nRepos of [cyan]{usr}[/cyan]")
        for r in repo:
            console.print(f"[cyan]-[/cyan] [yellow]{r.get('name')}[/yellow]")
    elif repos.status_code == 404:
        console.print(f"[red]The user {usr} not found\nCheck the name correctly.[/red]")
    else:
        print("[yellow]Couldn't Fetch Info try again later.[/yellow]")




if __name__ == "__main__":
 usr_info()
