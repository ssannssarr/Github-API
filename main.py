import func as gh
import subprocess as sp

from rich.console import Console
from rich.panel import Panel
from rich.table import Table

try:    
    import readline
except ModuleNotFoundError:
    permission = input("Do you want to Download readline (in windows it will not work)\n(y/n):>>").strip().lower()
    if permission == "y":
        print("readline library is downloading...")
        sp.run("python -m pip install readline")
    else:
        pass
        print("passing readline")
    

console = Console()

# Text section
WELCOME_TEXT = """
[bold green]Welcome to SaanS Github query terminal app.[/bold green]
For command list type [cyan]/help[/cyan]
^_^
"""
HELP_TEXT = """
[bold green]Github API Commands List[/bold green]

[green]/qry[/green]   -> This will fetch some info of the given username 
[green]/repo[/green]  -> This fetches all repo list of given username    
[green]/help[/green]  -> To open this help text                          
[green]/exit[/green]  -> To exit this py app                             
"""
gh.pnl(WELCOME_TEXT)

# The main loop 
usr_in = ""
try:
    while usr_in != "/exit":
        usr_in = input(">> ").strip().lower()
        if usr_in == "/help":
            gh.pnl(HELP_TEXT)
        elif usr_in == "/qry":
            gh.usr_info()
        elif usr_in == "/repo":
            gh.usr_repo()
        elif usr_in != "/exit":
            gh.pnl("I think that cmd is not available T.T")
    console.print("[yellow]\nGoodbye!![/yellow]")
except KeyboardInterrupt:
    console.print("[yellow]\nGoodbye!![/yellow]")
        
