# Task 12 - Palindrome Checker

Submitted by: M. Rohithanjan | Python Programming Track | Veda Technology

## What it does
This is a simple command-line Python program that checks if a given word, number, or sentence reads the same forward and backward (a palindrome). Before comparing, it normalizes the text by converting everything to lowercase and removing spaces and punctuation marks.

## Features
- Interactive menu that runs in a loop until you choose to exit.
- Normalizes input using `.lower()` and `.isalnum()` inside a simple `for` loop.
- Reverses the cleaned text using Python string slicing (`[::-1]`).
- Shows the original text, cleaned text, reversed text, and final result.
- Includes built-in valid and invalid palindrome test cases.
- Handles edge cases like empty inputs, spaces-only inputs, and punctuation-only inputs without crashing.

## How to run
1. Make sure Python 3 is installed on your computer.
2. Open a terminal inside the project folder (`Task-12-Palindrome-Checker`).
3. Run the script using:
   ```bash
   python palindrome_checker.py
   ```

## Valid and Invalid Palindrome Examples

**Valid Palindromes:**
- `madam`
- `Race Car`
- `A man a plan a canal Panama`
- `Was it a car or a cat I saw?`
- `12321`

**Invalid Palindromes:**
- `hello`
- `Python`
- `Veda Technology`
- `12345`

## Sample Output

```text
==================================================
  Palindrome Checker - Task 12 by M. Rohithanjan  
==================================================

Menu:
1. Check my own word or sentence
2. Run the built-in examples
3. Exit

Enter your choice (1/2/3): 2

--- Valid Palindrome Examples ---

Original text : madam
Cleaned text  : madam
Reversed text : madam
Result        : Yes, it is a palindrome

Original text : Race Car
Cleaned text  : racecar
Reversed text : racecar
Result        : Yes, it is a palindrome

Original text : A man a plan a canal Panama
Cleaned text  : amanaplanacanalpanama
Reversed text : amanaplanacanalpanama
Result        : Yes, it is a palindrome

Original text : Was it a car or a cat I saw?
Cleaned text  : wasitacaroracatisaw
Reversed text : wasitacaroracatisaw
Result        : Yes, it is a palindrome

Original text : 12321
Cleaned text  : 12321
Reversed text : 12321
Result        : Yes, it is a palindrome

--- Invalid Palindrome Examples ---

Original text : hello
Cleaned text  : hello
Reversed text : olleh
Result        : No, it is not a palindrome

Original text : Python
Cleaned text  : python
Reversed text : nohtyp
Result        : No, it is not a palindrome

Original text : Veda Technology
Cleaned text  : vedatechnology
Reversed text : ygolonhcetadev
Result        : No, it is not a palindrome

Original text : 12345
Cleaned text  : 12345
Reversed text : 54321
Result        : No, it is not a palindrome

Menu:
1. Check my own word or sentence
2. Run the built-in examples
3. Exit

Enter your choice (1/2/3): 1
Enter a word or sentence:    

Notice: You entered an empty input. Please enter a word or sentence.

Menu:
1. Check my own word or sentence
2. Run the built-in examples
3. Exit

Enter your choice (1/2/3): 1
Enter a word or sentence: Malayalam

Original text : Malayalam
Cleaned text  : malayalam
Reversed text : malayalam
Result        : Yes, it is a palindrome

Menu:
1. Check my own word or sentence
2. Run the built-in examples
3. Exit

Enter your choice (1/2/3): 1
Enter a word or sentence: Internship

Original text : Internship
Cleaned text  : internship
Reversed text : pihsnretni
Result        : No, it is not a palindrome

Menu:
1. Check my own word or sentence
2. Run the built-in examples
3. Exit

Enter your choice (1/2/3): 3

Thank you for using the Palindrome Checker. Goodbye!
```

## What I learned
- How to normalize user input using `.lower()` and filter out spaces and punctuation with `.isalnum()`.
- How to reverse strings quickly using slicing (`text[::-1]`).
- Why handling edge cases like blank spaces or punctuation-only strings is important so the program does not give misleading results.
- How to organize code into small, reusable functions with a clean menu loop.

## Interview Questions

**1. What is string slicing?**  
String slicing is a way to extract a portion (substring) of a string in Python using index positions in the format `string[start:stop:step]`. For example, `"python"[0:3]` returns `"pyt"`.

**2. How can you reverse a string in Python?**  
The easiest way is using string slicing with a step of `-1`, like `text[::-1]`, which reads the string from the end to the beginning. You can also reverse a string using `"".join(reversed(text))` or by looping through characters and adding each one to the front of a new string.

**3. Are strings mutable in Python?**  
No, strings are **immutable** in Python. Once a string is created, you cannot change its individual characters in place. Operations like `.lower()` or slicing always create and return a brand-new string.
