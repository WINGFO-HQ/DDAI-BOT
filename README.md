# DDAI Network

This project provides a simple Python script to monitor the throughput and status of the DDAI Network. It periodically fetches data from the DDAI API and displays it in a clear, tabulated format in the console. The script supports monitoring multiple accounts by using multiple API tokens.

## Features

* **Real-time Monitoring**: Continuously fetches and displays throughput and status.
* **Multi-Account Support**: Monitor the status of multiple DDAI accounts using different API tokens.
* **Colorful Output**: Utilizes `colorama` for easy-to-read status indicators (green for success, red for errors).
* **Clear Display**: Presents data in a well-formatted table using `tabulate`.
* **Error Handling**: Catches and displays any errors encountered during API requests.

## Requirements

To run this script, you need the following Python packages:

* `requests`
* `tabulate`
* `colorama`
* `python-dotenv`

You can install them using pip:

```bash
pip install -r requirements.txt
```

## Setup

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/WINGFO-HQ/DDAI-BOT.git
    cd DDAI-BOT
    ```

2.  **Register for a DDAI Network Account (if you don't have one):**
    You can register via this link: [https://app.ddai.network/](https://app.ddai.network/register?ref=57fgZQXJ)

3.  **Get Your API Token(s):**
    After logging into your DDAI Network account, you can obtain your API token(s) by following these steps:
    * Open your browser's developer tools (usually by right-clicking on the page and selecting "Inspect" or by pressing `F12`).
    * Navigate to the "Network" tab.
    * Refresh the page or perform an action that triggers an API request (e.g., check your dashboard).
    * Look for a request that has `auth` in its header (you might need to filter requests or look for `modelResponse` if available).
    * Click on that request, go to the "Headers" tab, and find the `Authorization` header.
    * Copy the token part (it usually starts with `Bearer ` followed by a long string of characters). This is your API token.

4.  **Edit `.env` file:**
    In the root directory of the project, Edit file named `.env`. This file will store your DDAI API tokens securely.

    Add your API tokens to the `.env` file, separated by commas. Each token corresponds to a different DDAI account you wish to monitor.

    ```dotenv
    TOKEN="your_token_1, your_token_2, your_token_3"
    ```
    Replace `your_token_1`, `your_token_2`, etc., with your actual DDAI API tokens.

## Usage

Run the `main.py` script from your terminal:

```bash
python main.py
```

The script will clear the console and display a table showing the current time, status, throughput, and any errors for each configured account. This display will update every second.

## Troubleshooting

* **`Error: 401 Client Error: Unauthorized for url:`**: This usually means your `TOKEN` in the `.env` file is incorrect or expired. Please verify your tokens.
* **`Error: [ConnectionError]`**: This indicates a problem with network connectivity. Check your internet connection.
* **"N/A" for Throughput**: If throughput shows "N/A", it means the API response did not contain throughput data in the expected format.
* **Script not updating**: Ensure `time.sleep(1)` is not commented out and that there are no unhandled exceptions stopping the loop.