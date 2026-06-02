try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.table import Table
    import requests as rq
except ModuleNotFoundError:
    print("""
The required modules are not installed 
Install them by:
"pip install -r requirements.txt"
""")
exit()

console = Console()

# Just Panel shortcut (I love shortcuts)
def pnl(content):
    console.print(Panel(content, border_style="cyan"))

# Function that gets every info about the usr
def usr_info():
    pnl("[green]Enter Username:[/green]")
    usr_name = input("[qry]>> ").strip()
    response = rq.get(
        f"https://api.github.com/users/{usr_name}"
    )
    if response.status_code == 200:
        data = response.json()
        GIT = f"""
This is Evry thing about [cyan]{data.get('name')}:[/cyan]

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
        pnl(GIT)
    elif response.status_code == 404:
        pnl("[red]User not found!![/red]")
    else:
        pnl("[yellow]UNKNOWN ERROR!![/yellow]")

# Fetches the list of all the repos the given user have
def usr_repo():
    pnl("[cyan]Enter the Username[/cyan]:")
    usr = input("[repo]>> ").strip()
    repos = rq.get(
        f"https://api.github.com/users/{usr}/repos"
    )
    
    if repos.status_code == 200:
        repo = repos.json()
        pnl(f"Repos of [cyan]{usr}[/cyan]")
        for r in repo:
            console.print(f"[cyan]-[/cyan] [yellow]{r.get('name')}[/yellow]")
    elif repos.status_code == 404:
        pnl(f"[red]The user {usr} not found\nCheck the name correctly.[/red]")
    else:
        pnl("[yellow]Couldn't Fetch Info try again later.[/yellow]")




if __name__ == "__main__":
 usr_info()
