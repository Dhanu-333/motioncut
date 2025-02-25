def word_counter(text):
    """
    Counts the number of words in the given text.

    :param text: str - Input text from the user.
    :return: int - Number of words in the text.
    """
    words = text.split()  # Splitting text into words
    return len(words)

def main():
    """Handles user input, error checking, and output display."""
    text = input("Enter a sentence or paragraph: ").strip()

    if not text:  # Error handling for empty input
        print("Error: No text entered. Please enter a valid sentence.")
        return

    count = word_counter(text)
    print(f"Total word count: {count}")

# Run the program
if __name__ == "__main__":
    main()
