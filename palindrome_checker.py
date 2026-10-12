# Task 12: Palindrome Checker
# Name: M. Rohithanjan
# Track: Python Programming (Veda Technology Internship)


def clean_text(text):
    # Convert to lowercase and keep only letters and numbers
    text = text.lower()
    cleaned = ""
    for char in text:
        if char.isalnum():
            cleaned = cleaned + char
    return cleaned


def is_palindrome(text):
    # Reverse the text using string slicing and compare
    reversed_text = text[::-1]
    if text == reversed_text:
        return True
    else:
        return False


def check_one(text):
    # Handle empty input or input with only spaces
    if text.strip() == "":
        print("Notice: You entered an empty input. Please enter a word or sentence.")
        return

    cleaned = clean_text(text)

    # Handle input that only had punctuation symbols
    if cleaned == "":
        print("Original text :", text)
        print("Notice: No letters or numbers found after removing punctuation.")
        return

    reversed_text = cleaned[::-1]

    print("Original text :", text)
    print("Cleaned text  :", cleaned)
    print("Reversed text :", reversed_text)

    if is_palindrome(cleaned):
        print("Result        : Yes, it is a palindrome")
    else:
        print("Result        : No, it is not a palindrome")


def run_examples():
    valid_examples = [
        "madam",
        "Race Car",
        "A man a plan a canal Panama",
        "Was it a car or a cat I saw?",
        "12321"
    ]

    invalid_examples = [
        "hello",
        "Python",
        "Veda Technology",
        "12345"
    ]

    print("\n--- Valid Palindrome Examples ---")
    for item in valid_examples:
        print()
        check_one(item)

    print("\n--- Invalid Palindrome Examples ---")
    for item in invalid_examples:
        print()
        check_one(item)


def main():
    print("==================================================")
    print("  Palindrome Checker - Task 12 by M. Rohithanjan  ")
    print("==================================================")

    while True:
        print("\nMenu:")
        print("1. Check my own word or sentence")
        print("2. Run the built-in examples")
        print("3. Exit")

        choice = input("\nEnter your choice (1/2/3): ").strip()

        if choice == "1":
            text = input("Enter a word or sentence: ")
            print()
            check_one(text)
        elif choice == "2":
            run_examples()
        elif choice == "3":
            print("\nThank you for using the Palindrome Checker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
