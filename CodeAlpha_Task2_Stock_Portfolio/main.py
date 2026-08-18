
import csv
import os
import sys

STOCK_PRICES = {
    "AAPL": 180.00,
    "TSLA": 250.00,
    "MSFT": 420.00,
    "GOOGL": 175.00,
    "AMZN": 190.00
}

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_FILE_PATH = os.path.join(BASE_DIR, "portfolio.csv")


def clear_screen():
    """Clears the terminal screen for a cleaner user experience."""
    os.system('cls' if os.name == 'nt' else 'clear')


def print_banner():
    """Prints a beautiful and professional ASCII banner for the application."""
    print("=" * 60)
    print("                  STOCK PORTFOLIO TRACKER                  ")
    print("=" * 60)
    print("  * Note: Stock prices are static sample values for demo *  ")
    print("  *       purposes and do NOT reflect real-time market data.*  ")
    print("=" * 60)


def show_available_stocks():
    """Displays the hardcoded database of available stocks and sample prices."""
    print("\n[ Available Stocks & Sample Prices ]")
    print("-" * 40)
    print(f"{'Stock Symbol':<15} | {'Sample Price':<15}")
    print("-" * 40)
    for symbol, price in STOCK_PRICES.items():
        print(f"{symbol:<15} | ${price:>13.2f}")
    print("-" * 40)


def calculate_total(portfolio):
    """
    Calculates the total value of the portfolio.
    
    Args:
        portfolio (dict): The portfolio mapping symbols to details.
        
    Returns:
        float: Total value of investments.
    """
    total = 0.0
    for details in portfolio.values():
        total += details['investment']
    return total


def view_portfolio(portfolio):
    """
    Displays the current portfolio in a clean, formatted table.
    
    Args:
        portfolio (dict): The portfolio data in-memory.
    """
    if not portfolio:
        print("\n[!] Your portfolio is currently empty.")
        return

    print("\n" + "-" * 60)
    print(f"{'Stock':<12} | {'Price':<12} | {'Quantity':<10} | {'Investment Value':<15}")
    print("-" * 60)
    
    for symbol, details in portfolio.items():
        price = details['price']
        qty = details['quantity']
        inv = details['investment']
        print(f"{symbol:<12} | ${price:>11.2f} | {qty:>10} | ${inv:>14.2f}")
        
    print("-" * 60)
    total_val = calculate_total(portfolio)
    print(f"{'TOTAL INVESTMENT:':<40} | ${total_val:>14.2f}")
    print("-" * 60)


def add_stock(portfolio):
    """
    Interactively adds or updates a stock quantity in the portfolio.
    Performs robust input validations.
    
    Args:
        portfolio (dict): The current active portfolio dictionary.
    """
    show_available_stocks()
    
    # 1. Symbol Input & Validation
    symbol = input("Enter stock symbol to add/update: ").strip().upper()
    if not symbol:
        print("\n[-] Error: Stock symbol cannot be empty.")
        return
        
    if symbol not in STOCK_PRICES:
        print(f"\n[-] Error: '{symbol}' is not available. Please choose from the list.")
        return
        
    # 2. Quantity Input & Validation
    qty_str = input(f"Enter quantity of shares for {symbol}: ").strip()
    if not qty_str:
        print("\n[-] Error: Quantity cannot be empty.")
        return
        
    try:
        quantity = int(qty_str)
    except ValueError:
        print("\n[-] Error: Quantity must be a valid whole number (no letters or decimals).")
        return
        
    if quantity <= 0:
        print("\n[-] Error: Quantity must be a positive number greater than zero.")
        return
        
    # 3. Add or update portfolio
    price = STOCK_PRICES[symbol]
    if symbol in portfolio:
        # Update existing stock: accumulate shares
        portfolio[symbol]['quantity'] += quantity
        portfolio[symbol]['investment'] = portfolio[symbol]['quantity'] * price
        print(f"\n[+] Updated {symbol}: Added {quantity} shares. New total: {portfolio[symbol]['quantity']} shares.")
    else:
        # Add new stock
        investment = price * quantity
        portfolio[symbol] = {
            'price': price,
            'quantity': quantity,
            'investment': investment
        }
        print(f"\n[+] Added {quantity} shares of {symbol} to your portfolio.")


def save_to_csv(portfolio, filename=CSV_FILE_PATH):
    """
    Saves the current portfolio data to a CSV file.
    
    Args:
        portfolio (dict): The active portfolio dictionary.
        filename (str): The destination file path.
    """
    if not portfolio:
        print("\n[-] Error: Cannot save an empty portfolio. Please add stocks first.")
        return False
        
    try:
        with open(filename, mode='w', newline='', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file)
            
            # Header Row
            writer.writerow(["Stock Symbol", "Price", "Quantity", "Investment Value"])
            
            # Data Rows
            for symbol, details in portfolio.items():
                writer.writerow([
                    symbol,
                    f"{details['price']:.2f}",
                    details['quantity'],
                    f"{details['investment']:.2f}"
                ])
            
            total_val = calculate_total(portfolio)
            writer.writerow(["TOTAL INVESTMENT", "", "", f"{total_val:.2f}"])
            
        print(f"\n[+] Portfolio successfully saved to: {filename}")
        return True
    except IOError as e:
        print(f"\n[-] Error: Failed to save portfolio. Disk error: {e}")
        return False


def load_from_csv(filename=CSV_FILE_PATH):
    """
    Loads portfolio data from a CSV file.
    Handles FileNotFoundError and format corruption safely.
    
    Args:
        filename (str): The file path to load data from.
        
    Returns:
        dict: The loaded portfolio, or None if the load failed or file doesn't exist.
    """
    if not os.path.exists(filename):
        print(f"\n[-] Information: No saved portfolio file found at '{os.path.basename(filename)}'.")
        return None
        
    loaded_portfolio = {}
    try:
        with open(filename, mode='r', newline='', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            
            # Read and validate header
            try:
                header = next(reader)
            except StopIteration:
                print("\n[-] Error: The portfolio file is completely empty.")
                return None
                
            expected_headers = ["Stock Symbol", "Price", "Quantity", "Investment Value"]
            # Clean and normalize header strings for comparison
            header_clean = [h.strip() for h in header]
            if not header_clean or header_clean[0] != "Stock Symbol":
                print("\n[-] Error: Invalid portfolio file structure. Header mismatch.")
                return None
                
            for row in reader:
                # Strip spaces from columns
                row = [col.strip() for col in row]
                if not row:
                    continue  # skip empty lines
                    
                symbol = row[0]
                
                # Check for the summary total row
                if symbol == "TOTAL INVESTMENT" or symbol == "TOTAL" or not symbol:
                    continue
                    
                # We expect 4 columns for stock rows
                if len(row) < 4:
                    continue
                    
                try:
                    # Validate and parse numerical fields
                    price = float(row[1])
                    quantity = int(row[2])
                    
                    # Recalculate investment locally to verify consistency
                    investment = price * quantity
                    
                    if quantity <= 0 or price <= 0:
                        continue # ignore invalid record
                        
                    loaded_portfolio[symbol] = {
                        'price': price,
                        'quantity': quantity,
                        'investment': investment
                    }
                except ValueError:
                    # Ignore row if it contains parsing errors
                    continue
                    
        if loaded_portfolio:
            print(f"\n[+] Portfolio loaded successfully from: {filename}")
            return loaded_portfolio
        else:
            print("\n[-] Warning: No valid stock records were found in the CSV file.")
            return None
            
    except (IOError, PermissionError) as e:
        print(f"\n[-] Error: Failed to read portfolio. File access error: {e}")
        return None


def clear_portfolio(portfolio):
    """
    Clears all stocks from the in-memory portfolio.
    
    Args:
        portfolio (dict): The active portfolio dictionary.
    """
    if not portfolio:
        print("\n[!] Portfolio is already empty.")
        return
        
    confirm = input("Are you sure you want to clear your entire portfolio? (y/n): ").strip().lower()
    if confirm == 'y':
        portfolio.clear()
        print("\n[+] Portfolio cleared successfully.")
    else:
        print("\n[!] Clear operation cancelled.")


def main():
    """Main program execution loop displaying the menu system."""
    portfolio = {}
    
    while True:
        print_banner()
        print(" 1. View Available Stocks")
        print(" 2. Add/Update Stock in Portfolio")
        print(" 3. View Active Portfolio")
        print(" 4. Save Portfolio to CSV")
        print(" 5. Load Portfolio from CSV")
        print(" 6. Clear Portfolio")
        print(" 7. Exit")
        print("=" * 60)
        
        choice = input("Enter your choice (1-7): ").strip()
        
        if choice == '1':
            clear_screen()
            print_banner()
            show_available_stocks()
            input("\nPress Enter to return to menu...")
            clear_screen()
            
        elif choice == '2':
            clear_screen()
            print_banner()
            add_stock(portfolio)
            input("\nPress Enter to return to menu...")
            clear_screen()
            
        elif choice == '3':
            clear_screen()
            print_banner()
            view_portfolio(portfolio)
            input("\nPress Enter to return to menu...")
            clear_screen()
            
        elif choice == '4':
            clear_screen()
            print_banner()
            save_to_csv(portfolio)
            input("\nPress Enter to return to menu...")
            clear_screen()
            
        elif choice == '5':
            clear_screen()
            print_banner()
            loaded = load_from_csv()
            if loaded is not None:
                portfolio = loaded
                view_portfolio(portfolio)
            input("\nPress Enter to return to menu...")
            clear_screen()
            
        elif choice == '6':
            clear_screen()
            print_banner()
            clear_portfolio(portfolio)
            input("\nPress Enter to return to menu...")
            clear_screen()
            
        elif choice == '7':
            print("\nThank you for using Stock Portfolio Tracker. Goodbye!\n")
            sys.exit(0)
            
        else:
            print("\n[-] Error: Invalid selection. Please enter a number between 1 and 7.")
            input("\nPress Enter to try again...")
            clear_screen()


if __name__ == "__main__":
    try:
        clear_screen()
        main()
    except KeyboardInterrupt:
        print("\n\n[!] Program interrupted by user. Exiting...")
        sys.exit(0)
