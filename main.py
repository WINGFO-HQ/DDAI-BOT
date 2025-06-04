import requests
import time
import os
from dotenv import load_dotenv
from tabulate import tabulate
from colorama import *

init(autoreset=True)

load_dotenv()
token = os.getenv("TOKEN")

url = "https://auth.ddai.network/modelResponse"
headers = {
    "Accept": "application/json, text/plain, */*",
    "Authorization": f"Bearer {token}",
    "Referer": "https://auth.ddai.network/",
    "Sec-Ch-Ua": '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"Windows"',
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    try:
        response = requests.get(url, headers=headers)
        data = response.json()

        throughput = data.get("data", {}).get("throughput", "N/A")
        status = data.get("status", "N/A")
        error = data.get("error", {})

        status_colored = Fore.GREEN + status if status == "success" else Fore.RED + status
        error_colored = Fore.RED + str(error) if error else Fore.GREEN + "{}"

        table = [
            ["Time", time.strftime("%Y-%m-%d %H:%M:%S")],
            ["Status", status_colored],
            ["Throughput", throughput],
            ["Error", error_colored]
        ]

        clear_screen()
        print(tabulate(table, headers=["Field", "Value"], tablefmt="grid"))

    except Exception as e:
        print(Fore.RED + f"Error: {e}")

    time.sleep(1)
