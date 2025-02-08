import re

def validate_credit_card(card_number):
    # Remove non-numeric characters
    card_number = re.sub(r'\D', '', card_number)

    # Luhn Algorithm Implementation
    def luhn_check(number):
        digits = [int(d) for d in number]
        checksum = 0
        is_second = False

        for digit in reversed(digits):
            if is_second:
                digit *= 2
                if digit > 9:
                    digit -= 9
            checksum += digit
            is_second = not is_second
        
        return checksum % 10 == 0

    return luhn_check(card_number)

# User Input
user_card = input("Enter your credit card number: ")
if validate_credit_card(user_card):
    print("✅ The credit card number is VALID!")
else:
    print("❌ The credit card number is INVALID!")


# just for test 
test_cards = [
    "4539 1488 0343 6467",  # Valid Visa
    "5500 0000 0000 0004",  # Valid MasterCard
    "3714 496353 98431",    # Valid AMEX
    "6011 0009 9013 9424",  # Valid Discover
    "3566 0020 2036 0505",  # Valid JCB
    "4539 1488 0343 6468",  # Invalid
    "5500 0000 0000 0005",  # Invalid
    "3714 496353 98432"     # Invalid
]