import re


def check_domain_name(domain):
    pattern = re.compile(r'^[a-zA-Z\d-]{2,63}(?:\.[a-zA-Z\d-]{2,63}){0,5}$')
    return bool(re.match(pattern, domain))


print("Do you want to type in your own domain or check work on default string? [y/n] Type in 'quit' for leave")
answer = input()
while answer not in ("quit", "close", "q", "break", "cl", "c"):
    if answer in ("no", "n", "net"):
        input_string = "help.stankin.ru"
        print(input_string)
        print(check_domain_name(input_string))
    elif answer in ("yes", "y", "ye", "da"):
        print("Please type in your domain")
        input_string = input()
        print(check_domain_name(input_string))
    else:
        print("Answer can be only yes/ye/y/da, no/n/net and quit/close/q/break/cl/c\nTry write the correct variant!")
    print("Do you want to type in your own domain or check work on default string? [y/n] Type in 'quit' for leave")
    if answer in ("no", "n", "net", "yes", "y", "ye", "da"):
        answer = input()
