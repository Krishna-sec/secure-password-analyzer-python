import re

# -----------------------------------------
# Password Strength Checker Function
# -----------------------------------------
def check_password_strength(password):

    score = 0
    suggestions = []

    # Check length
    if len(password) >= 12:
        score += 3
    elif len(password) >= 8:
        score += 2
        suggestions.append("Use 12+ characters for a stronger password.")
    else:
        score += 1
        suggestions.append("Password is too short. Use at least 8 characters.")

    # Check uppercase, lowercase, digits, symbols
    upper = bool(re.search(r"[A-Z]", password))
    lower = bool(re.search(r"[a-z]", password))
    digit = bool(re.search(r"[0-9]", password))
    symbol = bool(re.search(r"[^A-Za-z0-9]", password))

    classes = upper + lower + digit + symbol

    if classes == 4:
        score += 3
    elif classes == 3:
        score += 2
        suggestions.append("Add more variety: include uppercase, lowercase, digits, and symbols.")
    elif classes == 2:
        score += 1
        suggestions.append("Add more character types (e.g., digits or symbols).")
    else:
        suggestions.append("Password should contain uppercase, lowercase, digits, and symbols.")

    # Check repeated characters
    if re.search(r"(.)\\1\\1", password):
        score -= 1
        suggestions.append("Avoid repeating the same character 3+ times.")

    # Check sequences
    if "1234" in password or "abcd" in password.lower():
        score -= 1
        suggestions.append("Avoid simple sequences like '1234' or 'abcd'.")

    # Common weak passwords
    weak_list = ["password", "123456", "qwerty", "admin", "letmein"]
    if password.lower() in weak_list:
        score -= 3
        suggestions.append("This is a very common weak password. Avoid using it.")

    # Final score boundaries
    if score < 0:
        score = 0
    elif score > 10:
        score = 10

    # Label strength
    if score >= 8:
        label = "Strong"
    elif score >= 5:
        label = "Medium"
    else:
        label = "Weak"

    return score, label, suggestions


# -----------------------------------------
# Main Program (Runs in Terminal)
# -----------------------------------------
print("🔐 PASSWORD STRENGTH CHECKER 🔐")
password = input("Enter a password to check: ")

score, label, suggestions = check_password_strength(password)

print("\n=================================")
print(f"Password Strength: {label} ({score}/10)")
print("=================================\n")

print("Suggestions to improve your password:")
for s in suggestions:
    print(f"- {s}")

print("\nDone ✔")
