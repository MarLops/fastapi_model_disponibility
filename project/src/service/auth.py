import configparser
import logging
import os

import secrets



CONFIG = configparser.ConfigParser(os.environ)
CONFIG.read("settings.ini")
CONFIGES = CONFIG['user']

def authetification_user(username: bytes, password: bytes):
    global CONFIGES
    correct_username_bytes = CONFIGES.get("username").encode() 
    correct_password_bytes = CONFIGES.get("password").encode() 
    is_correct_username = secrets.compare_digest(
        username, correct_username_bytes
    )
    
    is_correct_password = secrets.compare_digest(
        password, correct_password_bytes
    )
    return (is_correct_username and is_correct_password)