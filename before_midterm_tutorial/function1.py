##A librarian wants to count how many books are in each category. The categories are represented by letters in a string, e.g. "aaabbc".
#👉 Write a function that returns a dictionary showing how many times each letter appears.
#Example: "aaabbc" → {'a': 3, 'b': 2, 'c': 1}

def book_counter(s):
    counts = {}
    for ch in s:
        counts[ch] = counts.get(ch, 0) + 1
    return counts

# Example
print(book_counter("aaabbc"))  # {'a': 3, 'b': 2, 'c': 1}



##A spy encodes messages by reversing the words and hiding them in a string.
#👉 Write a function that takes "hello world" and returns "olleh dlrow".
#Extra challenge: make it work for any sentence.

def decode_message(sentence):
    words = sentence.split()
    return " ".join(word[::-1] for word in words)

# Example
print(decode_message("hello world"))  # "olleh dlrow"


#An elevator starts at floor 0. You are given a list of moves: "U" means up one floor, "D" means down one floor.
#👉 Write a function that returns the final floor after all moves.
#Example: ["U", "U", "D", "U"] → 2

def final_floor(moves):
    floor = 0
    for move in moves:
        if move == "U":
            floor += 1
        elif move == "D":
            floor -= 1
    return floor
print(final_floor(["U", "U", "D", "U"]))

##A system wants to check if a password is strong. A password is strong if:
#It has at least 8 characters.
#It contains at least one uppercase letter, one lowercase letter, and one digit.
#👉 Write a function that returns True if the password is strong, otherwise False.
#Example: "Hello123" → True, "weak" → False.

def is_strong_password(password):
    if len(password) < 8:
        return False
    has_upper = any(ch.isupper() for ch in password)
    has_lower = any(ch.islower() for ch in password)
    has_digit = any(ch.isdigit() for ch in password)
    return has_upper and has_lower and has_digit

# Examples
print(is_strong_password("Hello123"))  # True
print(is_strong_password("weak"))      # False
print(is_strong_password("Alliaherika1213")) #True

#A mathematician wants to know if a number is prime.
#👉 Write a function that returns True if a number is prime, otherwise False.
#Example: 7 → True, 9 → False.

def prime_number(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

# Examples
print(prime_number(7))  # True
print(prime_number(9))  # False