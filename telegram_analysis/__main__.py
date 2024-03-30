# coding: utf-8

"""
Main script for the telegram_analysis package.
"""

# Imports
import argparse
import logging
import requests
import json
import os
from dotenv import dotenv_values


# Load environment variables
env = dotenv_values(".env")


# Logging setup
logging.basicConfig(
    filename="telegram_analysis.log",
    filemode="a",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


def main():
    """
    Main function for the telegram_analysis package.

    Returns
    -------
    None
    """

    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Analyze Telegram chat data.")
    # parser.add_argument("--version", action="version", version="%(prog)s " + __version__)
    # parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose logging")
    # parser.add_argument("-i", "--input", required=True, help="Input file (JSON format)")
    # parser.add_argument("-o", "--output", help="Output file (CSV format)")
    # parser.add_argument("-t", "--top", type=int, help="Number of top users to display")
    # parser.add_argument("-p", "--plot", action="store_true", help="Plot the results")
    args = parser.parse_args()

    bot_token = env["TELEGRAM_BOT_TOKEN"]

    api_url = f"https://api.telegram.org/bot{bot_token}/getUpdates"

    response = requests.get(api_url)
    print(response.status_code)

    print(response.json())



if __name__ == "__main__":
    main()