import re

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    ip_address = re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip)
    
    if ip_address:
        octets = [int(ip_address.group(i)) for i in range(1, 5)]
        
        if all(0 <= octet < 256 for octet in octets):
            return True
    return False

if __name__ == "__main__":
    main()

