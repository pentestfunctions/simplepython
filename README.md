
# Simple Python Toolkit 🛠️

A collection of utility functions to facilitate various operations such as file manipulation, text processing, network tasks, and more, readily usable for developers and penetration testers.

## Installation 📦

Clone this repository using git:

```
git clone https://github.com/pentestfunctions/simplepython
```

Then, you can import the toolkit in your Python script as follows:

```python
from simple_python import *
```

- You may also need:
  `pip install mss requests`
  `pip install ciphey`
  `sudo apt install python3-ciphey`


## Available Functions:

```
clear_screen
count_lines
decode_string
extract_domain
fetch_web_page
find_and_replace_in_file
get_current_date
get_current_datetime
get_current_time
get_data_type
get_domain_archive
get_function_info
load_file
lowercase_input
nmap_all
nmap_disable_ping_all
nmap_disable_ping_quick
nmap_quick
port_scanner
print_all_functions
print_alternating_colors
print_ascii_art
print_data_type
print_fancy_menu
print_green
print_lines
print_red
run_command
search_string
send_discord_webhook
site_software
take_screenshot_of_monitor
uppercase_input
write_file
```

## Features 🌟

- **File Operations**: Read, write, and modify files easily.
- **Text Processing**: Search, replace, and manipulate strings.
- **Network Utilities**: Fetch web pages, scan ports, and more.
- **Subprocess Management**: Run commands and processes.
- **Data Type Utilities**: Check and print data types with ease.
- **Date and Time**: Fetch current date, time, and datetime.
- **Miscellaneous**: Clear screen, take screenshots, etc.

## Usage Examples 📚

### Fetching Web Page Content

```python
content = fetch_web_page('https://www.example.com')
print(content)
```

### Port Scanning

```python
open_ports = port_scanner('example.com')
print(open_ports)
```

### Writing to a File

```python
write_file('/path/to/file.txt', 'Hello, World!')
```

## Contribution Guidelines 🤝

Contributions are welcome! If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcomed.

## Licensing ⚖️

The code in this project is licensed under MIT license. Please see the LICENSE file for more information.

---

For more information and updates, check out the [GitHub repository](https://github.com/pentestfunctions/simplepython).
