import roku_control

COMMAND_LIST = [
    {"name":"list","desc":"List all channels"},
    {"name":"select","desc":"Select a channel by index"},
    {"name":"input","desc":"Send a button press"},
    {"name":"type","desc":"Enter text into a search box"},
    {"name":"quit","desc":"Exit the program"}
]


def __list_apps():
    APPS = roku_control.get_channels()
    index = 1
    print("Ch #\t| Channel Name")
    for app in APPS:
        print(index, "\t|", app["name"])
        index += 1


def __type_string():
    string = input("Enter String:\t")
    for char in string:
        if char == " ":
            char = "%20"
        roku_control.send_keypress("Lit_"+char)

def __keypress():
    KEY = input("Enter a key:\t").lower()
    if KEY in roku_control.KEYS:
        roku_control.send_keypress(KEY)

def __select_app():
    APP_SELECT = input("Enter a Ch#:\t")
    try:
        SELECT_INDEX = int(APP_SELECT)
        APPS = roku_control.get_channels()
        print("Switching to:\t", APPS[SELECT_INDEX-1]["name"])
        roku_control.launch_app(APPS[SELECT_INDEX-1]["id"])
    except ValueError:
        print("Ch# invalid.")
    except IndexError:
        print("Ch# not a valid index")
def __quit():
    print("Good Bye")
def __help():
    print("Command Name\t|","Description")
    for command in COMMAND_LIST:
        print(command["name"]+"\t\t|",command["desc"])
MENU = {
    "list": __list_apps,
    "ls": __list_apps,
    "sel": __select_app,
    "select": __select_app,
    "type":__type_string,
    "help":__help,
    "type":__type_string,
    "inp":__keypress,
    "input":__keypress
}

def __show_menu():
    global COMMAND_LIST
    ##print(COMMAND_LIST)
    print("Enter a command:\t",end="")
    selection = input().lower()
    if selection == "q" or selection == "quit":
            raise KeyboardInterrupt
    elif selection in MENU:
        MENU[selection]()
    else:
        print("Invalid command")

if __name__ == "__main__":
    while True:
        try:
            __show_menu()
        except KeyboardInterrupt:
            __quit()
            break
#__list_apps()
#__select_app()
#__type_string("archer vice")
