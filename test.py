import re
from collections import defaultdict
import os

def remove_ansi_escape(text):
    ansi_escape = re.compile(r'\x1b\[[0-9;]*m')
    return ansi_escape.sub('', text)

def sort_urls_by_status(input_file):
    status_files = defaultdict(list)
    
    with open(input_file, 'r', encoding='utf-8') as file:
        for line in file:
            cleaned_line = remove_ansi_escape(line)
            match = re.match(r'(https?://\S+)\s+.*?\[(\d{3})\]', cleaned_line)
            if match:
                url, status = match.groups()
                status_files[status].append(url)
    
    for status, urls in status_files.items():
        with open(f'{status}.-ibm.com.txt', 'w', encoding='utf-8') as f:
            f.write('\n'.join(urls))
    
    print("URLs sorted successfully by status codes.")

# Example usage
sort_urls_by_status('httpx-ibmcloud.com.txt')