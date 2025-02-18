import random
import string

# Lists of adjectives and nouns
adjectives = ["Cool", "Happy", "Crazy", "Brave", "Mighty", "Funky", "Swift", "Epic", "Wild", "Sneaky"]
nouns = ["Tiger", "Dragon", "Phoenix", "Knight", "Wizard", "Ninja", "Panther", "Falcon", "Gamer", "Shadow"]

# Function to generate a random username
def generate_username(include_numbers=True, include_special_chars=True, length=None):
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    username = adjective + noun

    if include_numbers:
        username += str(random.randint(10, 99))  # Append random numbers

    if include_special_chars:
        username += random.choice(string.punctuation)  # Append special character

    return username if length is None else username[:length]  # Return full username if no length is specified

# Function to save usernames to a file
def save_usernames(usernames, filename="usernames.txt"):
    try:
        with open(filename, "a") as file:
            for username in usernames:
                file.write(username + "\n")
        print(f"\n✅ Usernames successfully saved to {filename}")
    except Exception as e:
        print(f"\n⚠️ Error saving usernames: {e}")

# Improved function to handle user input with validation
def get_user_input(prompt, valid_responses=None, default=None, input_type=str):
    while True:
        user_input = input(prompt).strip().lower()
        
        if user_input == "":  # If the user presses Enter
            return default
        
        if valid_responses and user_input not in valid_responses:
            print("❌ Invalid choice. Please enter a valid option.")
            continue
        
        if input_type == int:
            if user_input.isdigit():
                return int(user_input)  # Convert only if it's a valid integer
            else:
                print("❌ Please enter a valid number.")
                continue
        
        return user_input  # Return as a string if no conversion is needed

# Main program loop
def main():
    print("\n🎉 Welcome to the Random Username Generator 🎉\n")
    
    num_usernames = get_user_input("How many usernames do you want to generate? ", input_type=int, default=5)
    include_numbers = get_user_input("Include numbers? (yes/no): ", valid_responses=["yes", "no"], default="yes") == "yes"
    include_special_chars = get_user_input("Include special characters? (yes/no): ", valid_responses=["yes", "no"], default="yes") == "yes"
    
    length_input = get_user_input("Enter desired username length (Press Enter for no limit): ", default=None)
    length = int(length_input) if length_input is not None and length_input.isdigit() else None

    # Generate usernames
    usernames = [generate_username(include_numbers, include_special_chars, length) for _ in range(num_usernames)]
    
    # Display usernames
    print("\n🔹 Generated Usernames 🔹")
    for username in usernames:
        print("👉", username)
    
    # Ask to save usernames
    save_option = get_user_input("\nDo you want to save these usernames? (yes/no): ", valid_responses=["yes", "no"], default="yes")
    if save_option == "yes":
        save_usernames(usernames)

    print("\n🚀 Thank you for using the Random Username Generator! 🚀\n")

# Run the script
if __name__ == "__main__":
    main()
