"""This is not intended to be ran as a module, please don't run it as a module"""
from urllib.parse import urlparse


def __is_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False


def __write_config(url):
    js_file = open("./rokuControl.js", "r")
    content = js_file.readlines()
    js_file.close()
    js_file = open("./rokuControl.js", "w")
    content[0] = """let roku_ip = '"""+url+"""'\n"""
    js_file.writelines(content)
    js_file.close()


if __name__ == "__main__":
    VALID = False
    while not VALID:
        URI = input(
            "Enter the URL of your roku including protocol or q to quit:\t").lower()
        if URI == "q":
            exit()
        VALID = __is_url(URI)
    __write_config(URI)
