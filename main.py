import re


def check_domain_name(domain):
    pattern = re.compile(r'^[a-zA-Z\d-]{2,63}(?:\.[a-zA-Z\d-]{2,63}){0,5}$')
    return bool(re.match(pattern, domain))


input_string = "help.stankin.ru"
print(check_domain_name(input_string))
