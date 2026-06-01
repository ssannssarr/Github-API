import func as gh

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
    import subprocess
except ModuleNotFoundError:
    print("Module subprocess not found its for radline downloading")
    pass

try: 
    import readline
except ModuleNotFoundError:
    permission = input("Do you want to Download readline (in windows it will not work)\n(y/n):>>").strip().lower()
    if permission == "y":
        print("readline library is downloading...")
        subprocess.run("python -m pip install readline")
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
[green]/qry[/green]   -> This will fetch some info of the given username 
[green]/repo[/green]  -> This fetches all repo list of given username    
[green]/help[/green]  -> To open this help text                          
[green]/exit[/green]  -> To exit this py app                             
"""

console.print(Panel(WELCOME_TEXT, border_style="cyan"))

# The main loop 
usr_in = ""
try:
    while usr_in != "/exit":
        usr_in = input(">> ").strip().lower()
        if usr_in == "/help":
            console.print(Panel(HELP_TEXT, border_style="cyan"))
        elif usr_in == "/qry":
            gh.usr_info()
        elif usr_in == "/repo":
            gh.usr_repo()
        elif usr_in != "/exit":
            print("I think that cmd is not available T.T")
    console.print("[yellow]\nGoodbye!![/yellow]")
except KeyboardInterrupt:
    console.print("[yellow]\nGoodbye!![/yellow]")
        
