import os, sys
import add_account
from asyncio import sleep
from pyrogram import Client, filters
from rich.console import Console
import API
import config

console = Console()

app = Client(

add_account.name,
API.api_id,
API.api_hash

)
with app:
        me = app.get_me()

menu = console.input(f'''[bold]

     [bold black]FUNCTIONS[white]

use account >> {me.first_name}

[1] — echo messages
[2] — message send
[3] — leave chat
[4] — get all chat participants
[5] — change name / bio
[6] — send poll
[7] — set username
[8] — number of users
[9] — join chat
[10] — change photo
[11] — flood
[12] — create a channel
[13] — send photo
[14] — number of dialogues
[15] — number of messages
[16] — create a group
[17] — help
#> ''')

if menu == "1":
  @app.on_message(filters.me)
  def echo_messages(
      client, message
      ):
     message.reply(message.text)
     console.print(f'[bold whute][{me.first_name}] [bold purple]Reply message[bold white]: {message.text}')

elif menu == "2":
     user = console.input(
     "[bold purple]user [bold white]> "
     )
     message = console.input(
     "[bold purple]message [bold white]> "
     )
     with app:
             app.send_message(
                user, message
             )
             console.print(f"[bold white][{me.first_name}] [bold purple]message[bold white]: {message}")

elif menu == "3":
     chat = console.input(
     "[bold purple]chat [white]> "
     )
     with app:
             app.leave_chat(chat)
             console.print(f"[bold white][{me.first_name}] [bold purple]you left the chat [bold white]> [bold white]{chat}")


elif menu == "4":
    with app:
            for member in app.get_chat_members(config.chat_id):
                print(str(member))

elif menu == "5":
     name = console.input(
     "[bold purple]name [white]> "
     )
     bio = console.input(
     "[bold purple]bio [white]> "
     )
     last_name = console.input(
     "[bold purple]last name [white]> "
     )
     with app:
             app.update_profile(
             first_name=name,
             bio=bio
             )
             app.update_profile(
             last_name=last_name
             )
             console.print(
             "[bold green][+] change"
             )

elif menu == "6":
     chat = console.input(
     "[bold purple]chat [white]> "
     )
     question = console.input(
     "[bold purple]question [white]> "
     )
     answer_1 = console.input(
     "[bold purple]answer 1 [white]> "
     )
     answer_2 = console.input(
     "[bold purple]answer 2 [white]> "
     )
     answer_3 = console.input(
     "[bold purple]answer 3 [white]> "
     )
     with app:
             app.send_poll(
             chat,
             question,
             [answer_1,
              answer_2,
              answer_3
             ])

             console.print(
             "[bold green][+] send poll"
             )

elif menu == "7":
     username = console.input(
     "[bold purple]username [white]> "
     )
     with app:
             app.update_username(username)
             console.print("[bold green][+] set username")

elif menu == "8":
     with app:
             count = app.get_chat_members_count(config.chat_id)
             console.print(f"[bold red]chat id: [white]{config.chat_id}\n[bold purple]count[bold white]: {count}")

elif menu == "9":
     with app:
          username = console.input(
          "[bold purple]username to chat [white]> "
           )
          app.join_chat(username)
          console.print(
          '[green][+] [white]joined account'
          )

elif menu == "10":
     with app:
          app.set_profile_photo(photo="photo.jpg")
          console.print(
          "[bold green][+] [white]change"
          )

elif menu == "11":
     spam_text = console.input(
     "[bold purple]flood text [bold white]> "
     )

     trigger = console.input(
     "[bold purple]trigger [bold white]> "
     )

     console.print(f'[bold green][~] send to chat [bold white]".{trigger} count(0)"')
     @app.on_message(filters.command(f'{trigger}', prefixes='.') & filters.me)
     async def flood_chat_pm(_, message):
           await message.delete()
           cmd = message.text.split()
           for i in range(int(cmd[1])):
               await message.reply_text(spam_text)
               await sleep(config.delay)
               console.print(f'[bold white][{me.first_name}] [green]send: [white]{spam_text}')

elif menu == "12":
     channel_name = str(console.input(
        "[bold purple]channel name [white]> "
        )
     )

     description = console.input(
     "[bold purple]description channel [white]> "
     )

     with app:
          app.create_channel(

          channel_name,
          description

          )

          console.print(
          "[bold green][+] [white]channel created"
          )

elif menu == "13":
     chat = console.input(
     "[bold purple]username chat [white]> "
     )
     with app:
          app.send_photo(chat, "photo.jpg")
          console.print(
          "[bold green][+] [white]photo sent"
          )

elif menu == "14":
     with app:
          count = app.get_dialogs_count()
          console.print(f"[bold purple]count dialogs: [white]{count}")

elif menu == "15":
     with app:
          count = app.get_history_count(config.chat_id)
          console.print(f"[bold purple]messages: [white]{count}")

elif menu == "16":
     with app:
          group_name = console.input(
          "[bold purple]group name [white]> "
          )

          user_id = int(console.input(
             "[bold purple]enter user id to invite him to the group [white]> "
              )
          )

          group = app.create_group(group_name, user_id)
          console.print(
          "[bold green][+] [white]group created"
          )

elif menu == "17":
     with app:
          app.send_message(
          "me", "👋 Привет, нужна помощь?\nпрочитай README.md!\n📕 Канал: @squad_cvm где выходят частые обновления юзербота"
          )
          app.join_chat("@squad_cvm")
          console.print(
          "[bold green][+] [white]check your favorites"
          )

app.run()


