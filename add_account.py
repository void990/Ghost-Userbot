import os,sys
from pyrogram import Client
from rich.console import Console
import API

console = Console()

add = console.input('''
           [bold black]SESSIONS [bold white]

[1] — add account / use saved account
[2] — delete session's
#> ''')

if add == "1":
   name = str(console.input(
       "[bold purple]name sessions [white]> "
       )
   )

   app = Client(
      name,
      API.api_id,
      API.api_hash,
   )

   with app:
           me = app.get_me()
           console.print(f'[green][+] added: [bold white][{me.first_name}]')

elif add == "2":
     delete = console.input(
     "[bold red]are you sure you want to delete? [bold white](y/n)> "
     )

     if delete == "y":
        sess_name = console.input(
        "[bold purple]session name [bold white]> "
        )
        try:
           os.system(f'rm -rf {sess_name}.session')
           os.system(f'rm -rf {sess_name}.session-journal')
           console.print(f'[bold red][-] delete: [bold white]{sess_name}')

        except Exception as error:
               console.print(f'[bold red]ERROR: [white]{error}')

     elif delete == "n":
         sys.exit()

