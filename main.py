import re


def check_domain_name(input_string):
    pattern = re.compile(r'^[a-zA-Z0-9-]{2,63}(?:\.[a-zA-Z0-9-]{2,63}){0,5}$')
    return bool(re.match(pattern, input_string))


input_string = "help.stankin.ru"
print(check_domain_name(input_string))
