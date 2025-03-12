import socket

def get_ip_address(website_url):
    try:
        ip_address = socket.gethostbyname(website_url)
        return ip_address
    except socket.gaierror:
        return None

# List of three websites to check
websites = ['www.google.com', 'www.python.org', 'www.facebook.com']

for website in websites:
    ip = get_ip_address(website)
    if ip:
        print(f"The IP address of {website} is {ip}")
    else:
        print(f"Unable to get the IP address for {website}")
