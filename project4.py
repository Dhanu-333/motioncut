import random

def coin_toss():
    return random.choice(["Heads", "Tails"])

def multiple_tosses(n):
    heads = 0
    tails = 0
    
    for _ in range(n):
        result = coin_toss()
        print(result)
        if result == "Heads":
            heads += 1
        else:
            tails += 1
    
    print(f"\nTotal Heads: {heads} ({(heads/n)*100:.2f}%)")
    print(f"Total Tails: {tails} ({(tails/n)*100:.2f}%)")

def main():
    while True:
        try:
            flips = int(input("Enter the number of times you want to flip the coin: "))
            if flips <= 0:
                print("Please enter a positive number.")
                continue
            multiple_tosses(flips)
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue
        
        again = input("Do you want to toss again? (yes/no): ").strip().lower()
        if again != "yes":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
