class script(object):
    START_TXT = """ðļð...ðļð... {} ð

ðĻ'ð ðŊðððūððŋðð ð ððð-ðĨððððūð ðĄðð ðļðð ðĒðšð ðīððū ðŽðū ð ð ð  ð ððð-ðŋððððūð ðð ðļððð ðĶðððð

ðĻðð ðĪðšðð ðģð ðīððū ðŽðū; ðĐððð ð ð―ð― ðŽðū ðģð ðļððð ðĶðððð ð ð ð ð―ððð, 
ðģððšðð ð ðð, ð ðððð ðŊððððð―ðū ðŽððððūð ðģððūððū...ðĪðĪŠ


â ïļðŽðððū ð§ðūðð ð§ðð /help


ð ðŊðððūððūð― ðŧð @im_goutham_josh
"""
    HELP_TXT = """
ððŧââïļ   ð§ðūððððð  {} ðĪ

â  ðð'ð ð­ðððū ðĒððððððžðšððūð―...ðĪ

â  ðēðūðšððžð ððððð ððððððū ððð―ðū
ðģððð ððūðððð― ððððð ðð ðšðð ðžððšð, ðĐððð ððððū <b>Bot Username</b> ðšðð― ðððūð ððūðšððū ðš ðððšðžðū ðšðð― ððūðšððžð ðšðð ðððððū ððð ððšðð...


â ð ððšðððšðŧððū ðĒððððšðð―ð
     
 /start - Check I'm Alive..
 /status - Bot Status
 /info - User info
 /alive - To check you are alive
 /ping - To get your ping
 /id - User id
 /stats - Db status  
 /broadcast - Broadcast (ðŪðððūð ðŪððð)

â ð­ððððžðū ð:-

âðĢððð ðēððšð ðŽðū...ðĪ

ð ðŊðððūððūð― ðŧð @AutoFilter-Bot
"""
    ABOUT_TXT = """
â ðĒððūðšððð : <a href='https://t.me/im_goutham_josh'>ðģððð ðŊðūðððð</a>
â ðŦðšððððšððū : ðŊððððð ðĨ 
â ðŦððŧððšðð : ðŊððððððšð ðšððððžðð ðĒ.ðĢðĐ.ðĢ 
â ðēðūðððūð : Contabo
â ðĢðšððšðŧðšððū : <a href='https://www.mongodb.com'>ðŽðððððĢðĄ ðĨððūðū ðģððūð</a>
â ðĄðððð― ðēððšððð : v1.0.1 [BeTa]
â Movie ðĶðððð : <a href='https://t.me/wudixh'>ðģðšð ð§ðūððū</a>"""
    SOURCE_TXT = """<b>NOTE:</b>
Special Thanks to EvaMaria and Professor-Bot for the codes 
<b>DEV:</b>

- <a href=https://t.me/im_goutham_josh>ãGOUTHAM S E Rã</a>
- Source -  https://github.com/GouthamSER/Filter-Bot"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and PiroAutoFilterBot will respond whenever a keyword is found the message

<b>NOTE:</b>
1. kuttubot should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
âĒ /filter - <code>add a filter in chat</code>
âĒ /filters - <code>list all the filters of a chat</code>
âĒ /del - <code>delete a specific filter in chat</code>
âĒ /delall - <code>delete the whole filters in a chat (chat owner only)</code>

<b>Adv Global Filter </b>
âĒ /gfilter - <code>áīáī áīáīáī ÉĒĘáīĘáīĘ ŌÉŠĘáīáīĘs</code>
âĒ /gfilters - <code>áīáī áī ÉŠáīáīĄ ĘÉŠsáī áīŌ áīĘĘ ÉĒĘáīĘáīĘ ŌÉŠĘáīáīĘs<code>
âĒ /delg - <code>áīáī áīáīĘáīáīáī áī sáīáīáīÉŠŌÉŠáī ÉĒĘáīĘáīĘ ŌÉŠĘáīáīĘ</code>
âĒ /delallg - <code>áīáī áīáīĘáīáīáī áīĘĘ ÉĒĘáīĘáīĘ ę°ÉŠĘáīáīĘęą</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- KuttuBot Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. KuttuBot supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/PiroAutoFilterBot)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
âĒ /connect  - <code>connect a particular chat to your PM</code>
âĒ /disconnect  - <code>disconnect from a chat</code>
âĒ /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of PiroAutoFilterBot

<b>Commands and Usage:</b>
âĒ /id - <code>get id of a specified user.</code>
âĒ /info  - <code>get information about a user.</code>
âĒ /imdb  - <code>get the film information from IMDb source.</code>
âĒ /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
âĒ /logs - <code>to get the rescent errors</code>
âĒ /stats - <code>to get status of files in db.</code>
âĒ /delete - <code>to delete a specific file from db.</code>
âĒ /users - <code>to get list of my users and ids.</code>
âĒ /chats - <code>to get list of the my chats and ids </code>
âĒ /leave  - <code>to leave from a chat.</code>
âĒ /disable  -  <code>do disable a chat.</code>
âĒ /ban  - <code>to ban a user.</code>
âĒ /unban  - <code>to unban a user.</code>
âĒ /channel - <code>to get list of total connected channels</code>
âĒ /broadcast - <code>to broadcast a message to all users</code>
âĒ /inkick - <code>command with required arguments and i will kick members from group.</code>
âĒ /instatus - <code>to check current status of chat member from group.</code>
âĒ /inkick within_month long_time_ago - <code>to kick users who are offline for more than 6-7 days.</code>
âĒ /inkick long_time_ago - <code>to kick members who are offline for more than a month and Deleted Accounts.</code>
âĒ /dkick - <code>to kick deleted accounts."""
    STATUS_TXT = """ðģðððšð ðĨðððūð: <code>{}</code>
ðģðððšð ðŽðūððŧðūðð: <code>{}</code>
ðģðððšð ðĒððšðð: <code>{}</code>
ðīððūð― ðēððððšððū: <code>{}</code>
 """
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
IDðŦ - <code>{}</code>
NameðĻðŋâðĪâðĻðŋ - {}
"""
