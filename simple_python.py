import os
import re
import sys
import mss
import socket
import requests
import platform
import subprocess
from datetime import datetime
import json
import inspect
from itertools import cycle
import tempfile
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
import time
import pandas as pd

def print_all_functions():
    """
    Prints all function names and their signatures defined in the current module to show how they might be used.
    """
    current_module = sys.modules[__name__]  # Get a reference to the current module
    functions = inspect.getmembers(current_module, inspect.isfunction)  # Retrieve all functions in the module
    print(f"Available Functions:\n")
    for name, func in functions:
        # Get the signature of the function
        signature = inspect.signature(func)
        print(f"{name}{signature}")

def get_function_info(function):
    """
    Get information regarding the usage of any function
    """
    try:
        # Check if the input is a string (function name) or a function object
        if isinstance(function, str):
            # If it's a string, retrieve the function object by name
            func = globals().get(function) or locals().get(function)
        elif inspect.isfunction(function):
            # If it's already a function object, use it directly
            func = function
        else:
            return "Error: Input must be a function name (str) or a function object."

        if func is None:
            return f"Error: Function '{function}' not found."

        # Get the documentation of the function
        docstring = inspect.getdoc(func)
        print(docstring)
        if docstring is None:
            return f"Documentation not available for function '{function}'."
        
        return docstring
    except TypeError:
        return f"Error: '{function}' is not a function."
    except Exception as e:
        return f"An unexpected error occurred: {e}"
    
def load_file(filepath):
    """
    Load the contents of a file.

    Args:
    - filepath (str): The path to the file to load.

    Returns:
    - str: The contents of the file.

    Example Usage:
    - load_file('path/to/file.txt')
    """
    try:
        with open(filepath, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
    except IOError as e:
        print(f"Error: Could not read file '{filepath}': {e}")
    except Exception as e:
        print(f"An unexpected error occurred while loading file '{filepath}': {e}")

def write_file(filepath, content):
    """
    Write contents to a file.

    Args:
    - filepath (str): The path to the file to write to.
    - content (str): The content to write to the file.

    Example Usage:
    - write_file(filepath='/home/user/hello.txt', content="Hello World!")
    """
    try:
        with open(filepath, 'w') as file:
            file.write(content)
    except IOError as e:
        print(f"Error: Could not write to file '{filepath}': {e}")
    except Exception as e:
        print(f"An unexpected error occurred while writing to file '{filepath}': {e}")

def print_lines(filepath):
    """
    Print each line of a file.

    Args:
    - filepath (str): The path to the file to print lines from.

    Example Usage:
    - print_lines('/path/to/file.txt')
    """
    try:
        with open(filepath, 'r') as file:
            for line in file:
                print(line, end='')
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
    except IOError as e:
        print(f"Error: Could not read file '{filepath}': {e}")
    except Exception as e:
        print(f"An unexpected error occurred while printing lines from file '{filepath}': {e}")

def count_lines(filepath):
    """
    Return a line count of the file.

    Args:
    - filepath (str): The path to the file to count lines from.

    Returns:
    - int: The number of lines in the file.

    Example Usage:
    - count_lines('/path/to/file.txt')
    """
    try:
        with open(filepath, 'r') as file:
            return sum(1 for line in file)
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
    except IOError as e:
        print(f"Error: Could not read file '{filepath}': {e}")
    except Exception as e:
        print(f"An unexpected error occurred while counting lines from file '{filepath}': {e}")

def find_and_replace_in_file(filepath, find_str, replace_str):
    """
    Replaces a word with the desired word in a file.

    Args:
    - filepath (str): The path to the file to perform find and replace operation on.
    - find_str (str): The word to find.
    - replace_str (str): The word to replace the found word with.

    Example Usage:
    - find_and_replace_in_file(filepath='/home/user/example.txt', find_str='old_word', replace_str='new_word')
    """
    try:
        with open(filepath, 'r') as file:
            content = file.read()
        modified_content = content.replace(find_str, replace_str)
        with open(filepath, 'w') as file:
            file.write(modified_content)
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
    except IOError as e:
        print(f"Error: Could not read/write file '{filepath}': {e}")
    except Exception as e:
        print(f"An unexpected error occurred while performing find and replace in file '{filepath}': {e}")

def print_green(text):
    """
    Prints the given text in green color on the terminal.

    Args:
    - text (str): The text to print in green color.

    Example Usage:
    - print_green("This text will be printed in green.")
    """
    try:
        if isinstance(text, str):
            print("\033[92m" + text + "\033[0m")
        else:
            raise ValueError("Input must be a string.")
    except Exception as e:
        print(f"An error occurred while printing green text: {e}")

def print_red(text):
    """
    Prints the given text in red color on the terminal.

    Args:
    - text (str): The text to print in red color.

    Example Usage:
    - print_red("This text will be printed in red.")
    """
    try:
        if isinstance(text, str):
            print("\033[91m" + text + "\033[0m")
        else:
            raise ValueError("Input must be a string.")
    except Exception as e:
        print(f"An error occurred while printing red text: {e}")

def run_command(command):
    """
    Runs a command as a subprocess and prints the results live.

    Args:
    - command (str): The command to run.

    Returns:
    - tuple: A tuple containing the stdout and stderr data as strings.

    Example Usage:
    - run_command("ls -l")
    """
    # Ensure the command is in the format subprocess expects
    if isinstance(command, str):
        command = command.split()
    
    stdout_data = ""
    stderr_data = ""
    
    try:
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        for line in process.stdout:
            print(line, end='')
            stdout_data += line
        for line in process.stderr:
            print(line, end='')
            stderr_data += line
        process.wait()
    except FileNotFoundError:
        print(f"Error: Command not found or executable. {' '.join(command)}")
    except Exception as e:
        print(f"An unexpected error occurred:\nCommand: {' '.join(command)}\n{str(e)}")

    return stdout_data, stderr_data

def lowercase_input(input_string):
    """
    Lowercases the input string.

    Args:
    - input_string (str): The input string to be lowercased.

    Returns:
    - str: The lowercased input string.

    Example Usage:
    - lowercase_input("Hello World")  # Output: 'hello world'
    """
    return input_string.lower()

def uppercase_input(input_string):
    """
    Uppercases the input string.

    Args:
    - input_string (str): The input string to be uppercased.

    Returns:
    - str: The uppercased input string.

    Example Usage:
    - uppercase_input("Hello World")  # Output: 'HELLO WORLD'
    """
    return input_string.upper()

def get_data_type(data):
    """
    Gets the type of the input data.

    Args:
    - data: The input data whose type needs to be determined.

    Returns:
    - str: A string representing the type of the input data.

    Example Usage:
    - get_data_type(42)  # Output: "<class 'int'>"
    """
    return str(type(data))

def print_data_type(data):
    """
    Prints the input data with appropriate formatting based on its type.

    Args:
    - data: The input data to be printed.

    Example Usage:
    - print_data_type("Hello")  # Output: 'Hello'
    """
    if isinstance(data, str):
        print("'" + data + "'")
    elif isinstance(data, (int, float, complex)):
        print(data)
    elif isinstance(data, (list, tuple)):
        print("[", end="")
        for i, item in enumerate(data):
            print_data_type(item)
            if i < len(data) - 1:
                print(", ", end="")
        print("]")
    elif isinstance(data, dict):
        print("{")
        for key, value in data.items():
            print(f"    {key}: ", end="")
            print_data_type(value)
            if key != list(data.keys())[-1]:
                print(",")
        print("}")
    else:
        print(data)

def clear_screen():
    """
    Clears the screen based on operating system.

    Example Usage:
    - clear_screen()
    """
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def fetch_web_page(url):
    """
    Fetches the content of a web page.

    Args:
    - url (str): The URL of the web page to fetch.

    Returns:
    - str: The content of the web page, or an error message if the request failed.

    Example Usage:
    - content = fetch_web_page("https://www.example.com")
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        return f"An error occurred: {e}"
    
def port_scanner(remoteServer):
    """
    Scans ports of a remote host and prints the open ones.

    Args:
    - remoteServer (str): The remote host to scan.

    Returns:
    - list: A list of open ports.

    Example Usage:
    - open_ports = port_scanner("example.com")
    """
    subprocess.call('cls', shell=True)
    open_ports = []

    try:
        remoteServerIP = socket.gethostbyname(remoteServer)

        print("-" * 60)
        print("Please wait, scanning 1024 ports on remote host", remoteServerIP)
        print("-" * 60)

        t1 = datetime.now()

        for port in range(1, 1025):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((remoteServerIP, port))
            if result == 0:
                print("Port {}: Open".format(port))
                open_ports.append(port)
            sock.close()

    except KeyboardInterrupt:
        print("You pressed Ctrl+C")
        sys.exit()

    except socket.gaierror:
        print('Hostname could not be resolved. Exiting')
        sys.exit()

    except socket.error:
        print("Couldn't connect to server")
        sys.exit()

    t2 = datetime.now()
    total = t2 - t1
    print('Scanning Completed in: ', total)
    
    return open_ports

def take_screenshot_of_monitor(monitor_number):
    """
    Takes a screenshot of the specified monitor.

    Args:
    - monitor_number (int): The index of the monitor to take a screenshot of.

    Returns:
    - str: The filename of the saved screenshot.

    Example Usage:
    - filename = take_screenshot_of_monitor(0)
    """
    # Get the available monitors
    monitors = mss.mss().monitors

    # Check if there are available monitors
    if not monitors:
        raise ValueError("No monitors found")

    # Check if the specified monitor number is valid
    if monitor_number < 0 or monitor_number >= len(monitors):
        raise ValueError("Invalid monitor number")

    # Get the bounding box of the specified monitor
    monitor = monitors[monitor_number]
    left, top, width, height = monitor["left"], monitor["top"], monitor["width"], monitor["height"]

    # Take a screenshot of the specified monitor
    with mss.mss() as sct:
        screenshot = sct.grab({"left": left, "top": top, "width": width, "height": height})

    # Save the screenshot to a file
    filename = f"screenshot_monitor_{monitor_number}.png"
    mss.tools.to_png(screenshot.rgb, screenshot.size, output=filename)

    return filename

def get_current_datetime():
    """
    Get the current date and time.

    Returns:
    - datetime: Current date and time.

    Example Usage:
    - current_datetime = get_current_datetime()
    """
    return datetime.now()

def get_current_time():
    """
    Get the current time.

    Returns:
    - str: Current time in the format HH:MM:SS.

    Example Usage:
    - current_time = get_current_time()
    """
    return datetime.now().strftime("%H:%M:%S")

def get_current_date():
    """
    Get the current date.

    Returns:
    - str: Current date in the format YYYY-MM-DD.

    Example Usage:
    - current_date = get_current_date()
    """
    return datetime.now().strftime("%Y-%m-%d")

def print_alternating_colors(input_string):
    """
    Print each variable in the input string with alternating colors using ANSI escape codes.

    Args:
    - input_string (str): The input string containing variables separated by spaces.

    Example Usage:
    - print_alternating_colors("This is a test")  # Output: This is a test with alternating colors
    """
    # Split the input string into individual components
    components = input_string.split()

    for i, component in enumerate(components):
        # Alternate between green and red based on odd/even index
        color_code = "\033[92m" if i % 2 == 0 else "\033[91m"
        reset_code = "\033[0m"
        print(f"{color_code}{component}{reset_code}", end=" ")

def search_string(input_data, search_term):
    """
    Search for a string within the input data.

    Args:
    - input_data (str): The input data to search within.
    - search_term (str): The string to search for.

    Returns:
    - bool: True if the search term is found, False otherwise.

    Example Usage:
    - found = search_string("This is a test", "test")  # Output: True
    """
    return search_term in input_data

def print_fancy_menu(name="default name"):
    """
    Print a fancy menu with the provided name or a default name if none is provided,
    enhanced with ANSI colors and styles, and including the current date.

    Args:
    - name (str, optional): The name to include in the menu. Defaults to 'default name'.

    Example Usage:
    - print_fancy_menu("My Fancy Menu")
    """
    # ANSI escape codes for colors and styles
    HEADER_COLOR = "\033[95m"  # Light magenta for headers
    NAME_COLOR = "\033[96m"    # Cyan for the name
    DATE_COLOR = "\033[93m"    # Yellow for the date
    BORDER_COLOR = "\033[92m"  # Green for borders
    RESET_STYLE = "\033[0m"    # Reset to default terminal color

    # Dynamic elements
    current_date = datetime.now().strftime("%Y-%m-%d")
    border_line = f"{BORDER_COLOR}{'*' * 50}{RESET_STYLE}"
    header_footer = f"{HEADER_COLOR}{'=' * 50}{RESET_STYLE}"

    # Print the fancy menu
    print(header_footer)
    print(border_line)
    print(f"{NAME_COLOR}{' ' * ((50 - len(name)) // 2)}{name}{RESET_STYLE}")
    print(border_line)
    print(f"{DATE_COLOR}{'Date: ' + current_date}{' ' * (50 - len('Date: ' + current_date) - 1)}{RESET_STYLE}")
    print(header_footer)

def print_ascii_art(filename):
    """
    Print ASCII art from a file.

    Args:
    - filename (str): The name of the file containing the ASCII art.

    Example Usage:
    - print_ascii_art("ascii_art.txt")
    """
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            print(contents)
    except FileNotFoundError:
        print(f"The file '{filename}' does not exist.")

def extract_domain(url):
    """
    Extract the domain from a URL.

    Args:
    - url (str): The URL to extract the domain from.

    Returns:
    - str: The extracted domain.

    Example Usage:
    - domain = extract_domain("https://www.example.com")
    """
    # Regular expression pattern to match domain
    pattern = r'(?:https?://)?(?:www\.)?([^/]+)'
    # Find domain using regular expression
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    else:
        return None

def get_domain_archive(domain):
    """
    Get the archived versions of a domain from the Wayback Machine.

    Args:
    - domain (str): The domain to search for.

    Returns:
    - str: The XML response containing archived versions of the domain, or None if an error occurs.

    Example Usage:
    - archive_data = get_domain_archive("https://www.example.com")
    """
    # Strip the domain to keep only the SLD and TLD
    pattern = r'(?:https?://)?(?:www\.)?([^/]+)'
    match = re.search(pattern, domain)
    if match:
        api_url = f"https://web.archive.org/cdx/search/cdx?url=*.{match.group(1)}&output=xml&fl=original&collapse=urlkey"
        try:
            response = requests.get(api_url)
            response.raise_for_status()

            return response.text
        except requests.RequestException as e:
            # Handle any errors that occur during the request
            print(f"An error occurred: {e}")
            return None
    else:
        print(f"Domain format was unable to be parsed {domain}")

def send_discord_webhook(webhook_url, content, username="Default Bot Name", avatar_url="https://i.imgur.com/8nLFCVP.png", embeds=None):
    """
    Send a message to a Discord webhook.

    Args:
    - webhook_url (str): The full URL of the Discord webhook.
    - content (str): The message content.
    - username (str, optional): Custom username for the webhook message. Default is "Default Bot Name".
    - avatar_url (str, optional): URL of the avatar to use for the webhook message. Default is "https://i.imgur.com/8nLFCVP.png".
    - embeds (list, optional): A list of embed objects to include in the message. If None, no embeds will be included.

    Example Usage:
    - send_discord_webhook("https://discord.com/api/webhooks/123456789/abcdefg", "Hello, world!")
    - Get your webhook URL from the integrations tab on a discord server you own.
    """
    # Prepare the request payload
    payload = {
        "content": content,
        "username": username,
        "avatar_url": avatar_url
    }

    # Only add embeds to payload if they are provided
    if embeds is not None:
        payload["embeds"] = embeds

    headers = {
        "Content-Type": "application/json"
    }

    # Send the request to the Discord webhook URL
    response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)

    if response.status_code == 204:
        print("Message sent successfully.")
    else:
        print(f"Failed to send message. Status code: {response.status_code}, Response: {response.text}")

def nmap_quick(target):
    """
    Quick standard portscan on 80/443
    """
    try:
        if platform.system() == "Windows":
            # If the OS is Windows, try use WSL to run the nmap command
            command = ["wsl", "nmap", "-sV", "-sC", "-p", "80,443", target]
        else:
            # For other operating systems, use the nmap command directly
            command = ["nmap", "-sV", "-sC", "-p", "80,443", target]

        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

        for line in process.stdout:
            print(line, end='')

        process.communicate()  # Wait for the process to finish
        if process.returncode != 0:
            print(f"nmap_quick failed with return code {process.returncode}")
    except FileNotFoundError:
        print("nmap command not found. Please make sure nmap is installed.")
    except Exception as e:
        print(f"An error occurred: {e}")

def nmap_disable_ping_quick(target):
    """
    Quick NMAP port scan with ping disabled
    """
    try:
        if platform.system() == "Windows":
            # If the OS is Windows, try use WSL to run the nmap command
            command = ["wsl", "nmap", "-sV", "-sC", "-p", "80,443", "-Pn", target]
        else:
            # For other operating systems, use the nmap command directly
            command = ["nmap", "-sV", "-sC", "-p", "80,443", "-Pn", target]

        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

        for line in process.stdout:
            print(line, end='')

        process.communicate()  # Wait for the process to finish
        if process.returncode != 0:
            print(f"nmap_disable_ping_quick failed with return code {process.returncode}")
    except FileNotFoundError:
        print("nmap command not found. Please make sure nmap is installed.")
    except Exception as e:
        print(f"An error occurred: {e}")

def nmap_all(target):
    """
    Runs a portscan using Nmap with intense methods
    """
    try:
        if platform.system() == "Windows":
            # If the OS is Windows, try use WSL to run the nmap command
            command = ["wsl", "nmap", "-sV", "-sC", "-p-", target]
        else:
            # For other operating systems, use the nmap command directly
            command = ["nmap", "-sV", "-sC", "-p-", target]

        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

        for line in process.stdout:
            print(line, end='')

        process.communicate()  # Wait for the process to finish
        if process.returncode != 0:
            print(f"nmap_all failed with return code {process.returncode}")
    except FileNotFoundError:
        print("nmap command not found. Please make sure nmap is installed.")
    except Exception as e:
        print(f"An error occurred: {e}")

def nmap_disable_ping_all(target):
    """
    Run a nmap port scan with ping disable
    """
    try:
        if platform.system() == "Windows":
            # If the OS is Windows, try use WSL to run the nmap command
            command = ["wsl", "nmap", "-sV", "-sC", "-p-", "-Pn", target]
        else:
            # For other operating systems, use the nmap command directly
            command = ["nmap", "-sV", "-sC", "-p-", "-Pn", target]

        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

        for line in process.stdout:
            print(line, end='')

        process.communicate()  # Wait for the process to finish
        if process.returncode != 0:
            print(f"nmap_disable_ping_all failed with return code {process.returncode}")
    except FileNotFoundError:
        print("nmap command not found. Please make sure nmap is installed.")
    except Exception as e:
        print(f"An error occurred: {e}")

def site_software(target):
    """
    Find site software using whatweb and HTTPx
    """
    try:
        if platform.system() == "Windows":
            # If the OS is Windows, try use WSL to run the nmap command
            command = ["wsl", "whatweb", target]
        else:
            command = ["whatweb", target]
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        
        print(f"Whatweb Output:")
        print(50 * "=")
        for line in process.stdout:
            print(line, end='')

        process.communicate()  # Wait for the process to finish
        if process.returncode != 0:
            print(f"site_software failed with return code {process.returncode}")
    except FileNotFoundError:
        print("whatweb command not found. Please make sure whatweb is installed.")
    except Exception as e:
        print(f"An error occurred: {e}")
    try:
        if platform.system() == "Windows":
            # If the OS is Windows, try use WSL to run the nmap command
            command = ["wsl", "httpx", "-u", target, "-title", "-tech-detect", "-status-code", "-cl", "-ct", "-location", "-rt", "-lc", "-wc", "-server", "-method", "-ip", "-cname", "-cdn", "-probe", "-silent"]
        else:
            command = ["httpx", "-u", target, "-title", "-tech-detect", "-status-code", "-cl", "-ct", "-location", "-rt", "-lc", "-wc", "-server", "-method", "-ip", "-cname", "-cdn", "-probe", "-silent"]
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        
        print(f"\n\nHttpx Output:")
        print_divider('=')

        for line in process.stdout:
            print(line, end='')

        process.communicate()  # Wait for the process to finish
        if process.returncode != 0:
            print(f"site_software failed with return code {process.returncode}")
    except FileNotFoundError:
        print("httpx command not found. Please make sure httpx is installed.")
    except Exception as e:
        print(f"An error occurred: {e}")

def decode_string(target_string):
    """
    Use cipher to decode string/cipher
    """
    try:
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file_path = temp_file.name
        
        if platform.system() == "Windows":
            command = ["wsl", "ciphey", "-t", target_string, "-q", ">", temp_file_path]
        else:
            command = ["ciphey", "-t", target_string, "-q", ">", temp_file_path]
        
        # Use shell=True to handle redirection, and command as a single string
        process = subprocess.run(' '.join(command), shell=True, text=True, check=False)
        
        # Read the result from the file
        with open(temp_file_path, 'r') as file:
            output = file.read().strip()
        
        if process.returncode == 0 and output:
            print(f"Most likely result: {output}")
        else:
            print(f"decode_string failed with return code {process.returncode}")
        
        # Clean up the temporary file
        os.remove(temp_file_path)

    except FileNotFoundError:
        print("ciphey command not found. Please make sure ciphey is installed.")
    except Exception as e:
        print(f"An error occurred: {e}")

def host_folder(target_port):
    """
    Host a simple http.server on the chosen port.
    """
    try:
        if platform.system() == "Windows":
            # If the OS is Windows, try using WSL to run the nmap command
            command = ["wsl", "sudo", "python", "-m", "http.server", str(target_port)]
        else:
            command = ["sudo", "python", "-m", "http.server", str(target_port)]
        
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        
        print(f"Folder hosting Output:")
        print_divider('=')

        # Capture output until the process finishes
        for line in process.stdout:
            print(line, end='')
        
        # Wait for the process to finish
        process.communicate()

        if process.returncode != 0:
            print(f"host_folder failed with return code {process.returncode}")

    except Exception as e:
        print(f"An error occurred: {e}")

def find_local_resources(url):
    """
    Fetches a webpage and identifies a wide range of local resources.

    This includes scripts, stylesheets, icons, manifests, and other potential resources
    specified in <link> and <meta> tags that might reference local resources.

    :param url: URL of the webpage to fetch.
    :return: A list of URLs for locally hosted resources.
    """
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Initialize an empty list to store the URLs of local resources
        local_resources = []

        # Define the domain of the original URL
        domain = urlparse(url).netloc

        # Process <script> tags with src attributes
        for script in soup.find_all('script', src=True):
            src = script['src']
            absolute_src = urljoin(url, src)
            if urlparse(absolute_src).netloc == domain:
                local_resources.append(absolute_src)

        # Process <link> tags with href attributes for various types of resources
        for link in soup.find_all('link', href=True):
            href = link['href']
            absolute_href = urljoin(url, href)
            if urlparse(absolute_href).netloc == domain:
                local_resources.append(absolute_href)

        # Additional processing for <meta> tags or other tags could be added here

        return local_resources
    except requests.RequestException as e:
        print(f"Error fetching the page: {e}")
        return []
    
def print_all_in_list(list_data):
    """
    Prints all results in a variable/list which with alternating colors
    """
    colors = ['\033[31m', '\033[34m']  # ANSI escape codes for red and blue
    current_color_index = 0
    print(f"\nAll data in the list:")
    print_divider('-')
    for result in list_data:
        print(colors[current_color_index] + result + '\033[0m')  # Reset color after printing
        current_color_index = (current_color_index + 1) % 2  # Toggle between 0 and 1 for red and blue
    print_divider('-')

def directory_scan_quick(target):
    """
    Runs a directory scan against the target
    """
    try:
        if platform.system() == "Windows":
            # If the OS is Windows, try use WSL to run the nmap command
            command = ["wsl", "dirsearch", "-u", target, "-q"]
        else:
            # For other operating systems, use the nmap command directly
            command = ["dirsearch", "-u", target, "-q"]
    
        print_divider('x')
        print(f"Running dirsearch against {target}")
        print_divider('x')
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

        for line in process.stdout:
            print(line, end='')

        process.communicate()  # Wait for the process to finish
        if process.returncode != 0:
            print(f"directory_scan_quick failed with return code {process.returncode}")
    except FileNotFoundError:
        print("dirsearch command not found. Please make sure dirsearch is installed.")
    except Exception as e:
        print(f"An error occurred: {e}")

def print_divider(symbol="-"):
    """
    Prints a divider
    """
    print(50 * f"{symbol}")

def osint_username(username):
    """
    Open a million tabs to OSINT a username
    """
    try:
        urls = requests.get("https://raw.githubusercontent.com/pentestfunctions/WindowsLazyOsint/main/Usernames.txt").text.splitlines()
        username_list = [url.replace("$username", username) for url in urls]
        for url in username_list:
            time.sleep(1.1)
            os.system(f"start {url}")
    except Exception as e:
        print("Error occurred:", e)

def load_csv_and_print_column(csv_file):
    """
    Loads a CSV file and allows you to choose which columns to print out.
    """
    # Load the CSV file
    df = pd.read_csv(csv_file)
    
    # Print the options for the user
    print("Options:")
    for i, col in enumerate(df.columns, start=1):  # Start enumeration from 1
        print(f"{i}. {col}")
    
    # Ask the user for input
    choice = input("Choose a column by entering its number: ")
    
    # Check if the input is valid
    try:
        choice = int(choice)
        if choice < 1 or choice > len(df.columns):
            print("Invalid choice!")
            return
    except ValueError:
        print("Invalid choice! Please enter a number.")
        return
    clear_screen()
    # Print the selected column without index and with consistent spacing
    selected_column = df.columns[choice - 1]
    print(f"Selected column: {selected_column}")
    column_data = df[selected_column].astype(str)  # Convert to string to use str.ljust()
    max_length = column_data.str.len().max()  # Find the length of the longest string
    print(column_data.apply(lambda x: x.ljust(max_length)).to_string(index=False))
