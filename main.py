import requests
import time
import os
from dotenv import load_dotenv
from tabulate import tabulate
from colorama import *

init(autoreset=True)

load_dotenv()
tokens_str = os.getenv("TOKEN")
tokens = [t.strip() for t in tokens_str.split(',') if t.strip()]

url = "https://auth.ddai.network/modelResponse"
headers_template = {
    "Accept": "application/json, text/plain, */*",
    "Referer": "https://auth.ddai.network/",
    "Sec-Ch-Ua": '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"Windows"',
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    all_accounts_data = []
    for i, token in enumerate(tokens):
        headers = headers_template.copy()
        headers["Authorization"] = f"Bearer {token}"

        try:
            response = requests.get(url, headers=headers)
            data = response.json()

            throughput = data.get("data", {}).get("throughput", "N/A")
            status = data.get("status", "N/A")
            error = data.get("error", {})

            status_colored = Fore.GREEN + status if status == "success" else Fore.RED + status
            error_colored = Fore.RED + str(error) if error else Fore.GREEN + "{}"

            all_accounts_data.append([
                f"Account {i+1} - Time", time.strftime("%Y-%m-%d %H:%M:%S"),
                f"Account {i+1} - Status", status_colored,
                f"Account {i+1} - Throughput", throughput,
                f"Account {i+1} - Error", error_colored
            ])

        except Exception as e:
            all_accounts_data.append([
                f"Account {i+1} - Time", time.strftime("%Y-%m-%d %H:%M:%S"),
                f"Account {i+1} - Status", Fore.RED + "Error",
                f"Account {i+1} - Throughput", "N/A",
                f"Account {i+1} - Error", Fore.RED + f"{e}"
            ])
            print(Fore.RED + f"Error for Account {i+1}: {e}")

    clear_screen()
    
    flattened_data = []
    for account_data in all_accounts_data:
        for j in range(0, len(account_data), 2):
            flattened_data.append([account_data[j], account_data[j+1]])

    print(tabulate(flattened_data, headers=["Field", "Value"], tablefmt="grid"))

    time.sleep(1)