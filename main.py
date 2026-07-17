
def main():
    print("=== FINANCIAL LEDGER SYSTEM ===")
    total = 0.0

    while True:
        user_input = input("\nEnter expense (or 'done' to finish): ")
        
        if user_input.lower() == 'done':
            break
        
        try:
            expense = float(user_input)
            
            # Simple business rule guard: stop negative numbers if you want
            if expense < 0:
                print("Invalid amount. Expenses cannot be negative.")
                continue
                
            total += expense
            print(f"Subtotal Updated: ₹{total:.2f}")
            
        except ValueError:
            print("Poka-Yoke Alert: Invalid input. Please enter a numerical value.")

    print("\n==================================")
    print(f"FINAL AUDIT SUMMARY | Total Spent: ${total:.2f}")
    print("==================================")


if __name__ == "__main__":
    main()