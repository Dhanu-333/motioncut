def reverse_characters(text):
    return text[::-1]

def reverse_words(text):
    return ' '.join(text.split()[::-1])

def save_to_file(text):
    with open("reversed_output.txt", "w") as file:
        file.write(text)
    print("✅ Reversed text saved to 'reversed_output.txt'.")

def main():
    while True:
        print("\n✨ Text Reverser Menu ✨")
        print("1. Reverse Characters")
        print("2. Reverse Word Order")
        print("3. Exit")
        
        choice = input("Choose an option (1-3): ")
        
        if choice == '1' or choice == '2':
            user_input = input("Enter your text: ").strip()
            if not user_input:
                print("⚠️ Please enter some text!")
                continue

            if choice == '1':
                result = reverse_characters(user_input)
            else:
                result = reverse_words(user_input)

            print(f"🔁 Reversed Result: {result}")
            
            save = input("Do you want to save this to a file? (y/n): ").lower()
            if save == 'y':
                save_to_file(result)

        elif choice == '3':
            print("👋 Exiting... Thanks for using Text Reverser!")
            break
        else:
            print("❌ Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
