#Functions displaying hours, amount customers name and total
def amount_due(hours, hourly_rate):
    """Calculates the base cost before any tax or discount."""
    return hours * hourly_rate


def final_amount(base_amount, tax_rate=0.15):
    """Calculates the total payment including tax (default 15% VAT)."""
    tax = base_amount * tax_rate
    return base_amount + tax


def display_name(customer_name):
    """Formats and displays the customer's name on the receipt."""
    print("\n--- JOHN FITNESS CENTRE ---")
    print(f"Customer Name: {customer_name.strip().title()}")


def process_payment(total_due):
    """Handles payment input and calculates any change owed."""
    while True:
        try:
            cash_paid = float(input(f"Total to pay is R{total_due:.2f}. Enter amount paid: R"))
            if cash_paid >= total_due:
                change = cash_paid - total_due
                print(f"Payment accepted! Change due: R{change:.2f}")
                print("Thank you for training with us!")
                break
            else:
                shortfall = total_due - cash_paid
                print(f"Insufficient amount. Please pay at least R{shortfall:.2f} more.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def main():
    HOURLY_RATE = 50.00  # R50 per hour

    # Get customer details
    name = input("Enter customer name: ")
    hours = float(input("Enter number of hours used: "))

    # Perform calculations using the functions
    subtotal = amount_due(hours, HOURLY_RATE)
    total = final_amount(subtotal)

    # Display receipt and process payment
    display_name(name)
    print(f"Hours Used:    {hours}")
    print(f"Hourly Rate:   R{HOURLY_RATE:.2f}")
    print(f"Subtotal:      R{subtotal:.2f}")
    print(f"Final Amount:  R{total:.2f} (incl. 15% VAT)")
    print("---------------------------")
    
    process_payment(total)


if __name__ == "__main__":
    main()
