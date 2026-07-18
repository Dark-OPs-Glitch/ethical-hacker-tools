import re

password = input("Enter password to check: ")

# Check different rules
length = len(password) >= 8
upper = re.search(r"[A-Z]", password)
lower = re.search(r"[a-z]", password)
digit = re.search(r"[0-9]", password)
special = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

# Calculate score
score = sum([length, bool(upper), bool(lower), bool(digit), bool(special)])

print("\n--- Password Analysis ---")
print(f"Length 8+ characters : {'✓' if length else '✗'}")
print(f"Has Uppercase A-Z    : {'✓' if upper else '✗'}")
print(f"Has Lowercase a-z    : {'✓' if lower else '✗'}")
print(f"Has Number 0-9       : {'✓' if digit else '✗'}")
print(f"Has Special !@#      : {'✓' if special else '✗'}")

print("\n--- Result ---")
if score <= 2:
    print("WEAK Password - Easy to crack")
elif score <= 4:
    print("MEDIUM Password - Could be stronger")
else:
    print("STRONG Password - Good job!")