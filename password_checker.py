import re

def check_password_strength(password):
    # Define the criteria for a strong password
    length_criteria = len(password) >= 8
    lowercase_criteria = re.search(r'[a-z]', password)
    uppercase_criteria = re.search(r'[A-Z]', password)
    digit_criteria = re.search(r'\d', password)
    special_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password)

    # Calculate the strength score
    strength_criteria = [length_criteria, lowercase_criteria, uppercase_criteria, digit_criteria, special_criteria]
    score = sum(bool(criteria) for criteria in strength_criteria)

    # Provide feedback based on the score
    if score == 5:
        strength = 'Strong'
    elif score >= 3:
        strength = 'Medium'
    else:
        strength = 'Weak'

    # Feedback message
    feedback = f"Password Strength: {strength}\n"
    feedback += "Criteria Met:\n"
    feedback += f"Length (>= 8): {'✓' if length_criteria else '✗'}\n"
    feedback += f"Lowercase Letter: {'✓' if lowercase_criteria else '✗'}\n"
    feedback += f"Uppercase Letter: {'✓' if uppercase_criteria else '✗'}\n"
    feedback += f"Digit: {'✓' if digit_criteria else '✗'}\n"
    feedback += f"Special Character: {'✓' if special_criteria else '✗'}\n"

    return feedback

# Test the function
if __name__ == "__main__":
    password = input("Enter a password to check its strength: ")
    print(check_password_strength(password))
