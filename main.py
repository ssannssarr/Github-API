import func as gh
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
    


WELCOME_TEXT = """
Welcome to SaanS Github query terminal app.
For command list type "/help"
^_^
"""
HELP_TEXT = """
|---------------------------------------------------------------|
| /qry : This cmd will open a user detail grabbing function     |
| /help    : To open this help text                             |
| /exit    : To exit this py app                                |
|---------------------------------------------------------------|
"""

print(WELCOME_TEXT)

usr_in = ""
try:
    while usr_in != "/exit":
        usr_in = input(">> ").strip().lower()
        if usr_in == "/help":
            print(HELP_TEXT)
        elif usr_in == "/qry":
            gh.usr_info()
        elif usr_in != "/exit":
            print("I think that cmd is not available T.T")
    print("\nGoodbye!!")
except KeyboardInterrupt:
    print("\nGoodbye!!")
        
