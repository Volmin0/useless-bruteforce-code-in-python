import itertools

def brute_force(password):
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    attempts = 0

    for length in range(1, 9):  # Adjust the length as needed
        for attempt in itertools.product(characters, repeat=length):
            current_attempt = ''.join(attempt)
            attempts += 1

            if current_attempt == password:
                print(f"Password found: {current_attempt} (Attempts: {attempts})")
                return

    print("Password not found.")

# Example usage:
target_password = "Secret123"
brute_force(target_password)
