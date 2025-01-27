# Subdomain_Status_Checker
This Python tool checks if subdomains are active or not.It is simple to use and can help identify reachable subdomains from a list.
# Features
  1) Identifies active subdomains based on their HTTP status codes.
  2) Outputs both active and inactive subdomains.
  3) Handles request timeouts and errors gracefully.

# Prerequisites
Ensure Python 3.x is installed on your system. You can download Python from python.org.

# Installation Steps

  1) Clone the Repository
  Open a terminal and run:

    git clone https://github.com/atmajkhatavkar404/subdomain-status-checker.git
    cd subdomain-status-checker

  2) Install the required Python library

    pip install requests

# Usage
  1) Prepare Your Subdomain List
  2) Run the Script:
   
    python subdomain_checker.py

  3)View Results
The script outputs active and inactive subdomains directly in the terminal. Active subdomains are also stored in the active_subdomains variable within the script.
