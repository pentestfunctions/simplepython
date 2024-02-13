
# Simple Python Toolkit 🛠️

A collection of utility functions to facilitate various operations such as file manipulation, text processing, network tasks, and more, readily usable for developers and penetration testers.

## Installation 📦

Clone this repository using git:

```
git clone https://github.com/pentestfunctions/simplepython
```
```
pip install -r requirements.txt
```

Then, you can import the toolkit in your Python script as follows:

```python
from simple_python import *
```

- You may also need:
  `pip install ciphey`
  OR
  `sudo apt install python3-ciphey`


## Available Functions:

```
clear_screen()
count_lines(filepath)
decode_string(target_string)
directory_scan_quick(target)
extract_domain(url)
fetch_web_page(url)
find_and_replace_in_file(filepath, find_str, replace_str)
find_local_resources(url)
get_current_date()
get_current_datetime()
get_current_time()
get_data_type(data)
get_domain_archive(domain)
get_function_info(function)
host_folder(target_port)
load_csv_and_print_column(csv_file)
load_file(filepath)
lowercase_input(input_string)
nmap_all(target)
nmap_disable_ping_all(target)
nmap_disable_ping_quick(target)
nmap_quick(target)
osint_username(username)
port_scanner(remoteServer)
print_all_functions()
print_all_in_list(list_data)
print_alternating_colors(input_string)
print_ascii_art(filename)
print_data_type(data)
print_divider(symbol='-')
print_fancy_menu(name='default name')
print_green(text)
print_lines(filepath)
print_red(text)
run_command(command)
search_string(input_data, search_term)
send_discord_webhook(webhook_url, content, username='Default Bot Name', avatar_url='https://i.imgur.com/8nLFCVP.png', embeds=None)
site_software(target)
take_screenshot_of_monitor(monitor_number)
uppercase_input(input_string)
urljoin(base, url, allow_fragments=True)
urlparse(url, scheme='', allow_fragments=True)
write_file(filepath, content)
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
