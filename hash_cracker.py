import hashlib

def crack_md5(hash_to_crack, wordlist_file):
    try:
        with open(wordlist_file, 'r', errors='ignore') as file:
            for line in file:
                password = line.strip()
                if hashlib.md5(password.encode()).hexdigest() == hash_to_crack:
                    print(f"[+] Found: {password}")
                    return
        print("[-] Not found in wordlist")
    except FileNotFoundError:
        print("Wordlist not found")

hash_input = input("Enter MD5 hash: ")
wordlist = input("Enter wordlist path: ")
crack_md5(hash_input, wordlist)