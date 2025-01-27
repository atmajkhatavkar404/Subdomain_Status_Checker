import requests
import concurrent.futures

def check_subdomain(subdomain):
    """
    Check if a subdomain is active.
    """
    try:
        response = requests.get(f"http://{subdomain}", timeout=5)
        if response.status_code == 200:
            return subdomain, True
        return subdomain, False
    except requests.RequestException:
        return subdomain, False

def check_subdomains(subdomains):
    """
    Check a list of subdomains for activity.
    """
    active_subdomains = []

    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(check_subdomain, subdomains)
        for subdomain, is_active in results:
            if is_active:
                active_subdomains.append(subdomain)

    return active_subdomains

def main():
    """
    Main function to handle input and output.
    """
    input_file = input("Enter the filename containing subdomains: ")
    output_file = input("Enter the filename to save active subdomains: ")

    try:
        with open(input_file, 'r') as file:
            subdomains = [line.strip() for line in file.readlines()]

        print("Checking subdomains...")
        active_subdomains = check_subdomains(subdomains)

        with open(output_file, 'w') as file:
            file.writelines(f"{subdomain}\n" for subdomain in active_subdomains)

        print(f"Active subdomains saved to {output_file}.")
    except FileNotFoundError:
        print("Error: Input file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
