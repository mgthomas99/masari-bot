import configparser

config = configparser.ConfigParser()
config.read("config.ini")

discord = config["Discord"]
service = config["Service"]
masari = config["Masari"]
