import re

def extract_valid_ips(text):

    # Regular expression to match potential IPv4 addresses
    pattern = r'(?:\d{1,3}\.){3}\d{1,3}'
    
    # Find all matches of the pattern
    potential_ips = re.findall(pattern, text)
    
    # Filter out invalid IPs by ensuring each segment is between 0 and 255
    valid_ips = [ip for ip in potential_ips if all(0 <= int(part) <= 255 for part in ip.split('.'))]
    
    return valid_ips

# Input
text = "The server's IPs are 192.168.0.1, 10.0.0.255, and an invalid IP 999.999.999.999."
print(extract_valid_ips(text))
