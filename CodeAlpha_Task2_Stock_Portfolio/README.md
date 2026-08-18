# CodeAlpha Task 2: Stock Portfolio Tracker

A professional, interactive console-based **Stock Portfolio Tracker** application built with Python. This project is developed as part of the **CodeAlpha Python Programming Internship**.

It allows users to manage their stock assets, view available listings, compute local investment holdings, persist data to a CSV database, and reload portfolios seamlessly.

> [!IMPORTANT]
> **Stock Price Notice**: This tracker uses **hardcoded/static demo stock prices** for demonstration and educational purposes. It does **not** retrieve real-time market prices from external web APIs.

---

## Features

- **Interactive Menu System**: A user-friendly 7-option console navigation system.
- **Stock Database Preview**: Lists symbols and static prices of available mock stocks.
- **Smart Portfolio Aggregation**: If a stock is added multiple times, the quantity is automatically accumulated.
- **Robust Input Validation**:
  - Rejects negative numbers, zero, or non-numeric inputs for share quantity.
  - Verifies that entered stock symbols are supported.
  - Handles missing CSV data files safely instead of crashing.
  - Validates menu selections.
- **Data Calculations**: Automatically computes the investment value per stock ($Price \times Quantity$) and sums the cumulative total portfolio value.
- **CSV Import/Export**: Saves active portfolios with total calculations to a CSV file and loads past records back into memory.
- **Clear Portfolio Utility**: Clears the active workspace, with confirmation prompts to prevent accidental data loss.

---

## Technologies Used

- **Python 3** (Only Core Standard Libraries)
  - `csv` — for structured data storage and reading
  - `os` — for console management and cross-platform compatibility
  - `sys` — for process flow termination
- **Data Structures**: Lists and dictionaries for memory storage and lookups.
- **Exception Handling**: Try-Except blocks for safe execution and error handling.

---

## Project Structure

```text
CodeAlpha_Task2_Stock_Portfolio/
│
├── main.py            # Primary application file containing all menu logic and functions.
├── portfolio.csv      # Local database storage generated dynamically on save.
├── README.md          # Comprehensive documentation (this file).
├── requirements.txt   # File declaring that only standard python libraries are required.
└── .gitignore         # File to ignore byte-cache compilation and user-local data files.
```

---

## How to Install and Run

### Prerequisites
Make sure you have [Python 3.x](https://www.python.org/) installed. You can check your version in the terminal:
```bash
python --version
```

### Installation
1. Clone or download this project folder.
2. Navigate to the project directory:
   ```bash
   cd CodeAlpha_Task2_Stock_Portfolio
   ```

### Execution
Run the program with:
```bash
python main.py
```

---

## How to Use

When the program runs, you will be presented with a menu:

1. **View Available Stocks**: Displays a table of mock tickers (AAPL, TSLA, MSFT, GOOGL, AMZN) and their static prices.
2. **Add Stock to Portfolio**: Allows you to enter a symbol and the number of shares to add to your holding.
3. **View Portfolio**: Renders a formatted tabular overview of your assets, their stock value, individual investments, and the cumulative total investment.
4. **Save Portfolio to CSV**: Exports your portfolio into `portfolio.csv`.
5. **Load Portfolio from CSV**: Imports a previously saved portfolio from `portfolio.csv` back into the system.
6. **Clear Portfolio**: Resets the active holdings in memory.
7. **Exit**: Gracefully exits the application.

---

## Example Output

### 1. View Available Stocks
```text
[ Available Stocks & Sample Prices ]
----------------------------------------
Stock Symbol    | Sample Price
----------------------------------------
AAPL            | $       180.00
TSLA            | $       250.00
MSFT            | $       420.00
GOOGL           | $       175.00
AMZN            | $       190.00
----------------------------------------
```

### 2. View Active Portfolio
```text
------------------------------------------------------------
Stock        | Price        | Quantity   | Investment Value
------------------------------------------------------------
AAPL         | $     180.00 |          5 | $        900.00
TSLA         | $     250.00 |          2 | $        500.00
------------------------------------------------------------
TOTAL INVESTMENT:                        | $       1400.00
------------------------------------------------------------
```

---

## CSV File Layout

When the portfolio is saved, the generated `portfolio.csv` file is formatted as follows:

```csv
Stock Symbol,Price,Quantity,Investment Value
AAPL,180.00,5,900.00
TSLA,250.00,2,500.00
TOTAL INVESTMENT,,,1400.00
```
*Note: The load routine is designed to ignore the `TOTAL INVESTMENT` row to prevent data corruption during reloading.*

---

## LinkedIn / Video Demo Script

Use this short, professional script to record your project demonstration video for LinkedIn or GitHub.

* **Intro (0:00 - 0:15)**:
  > *"Hello everyone! I am Gobinathan R. In this video, I am excited to showcase my latest project developed during my Python Programming Internship at CodeAlpha: a Stock Portfolio Tracker. Let's dive in!"*
* **Demonstrating Stock Prices & Input (0:15 - 0:45)**:
  > *"This program runs completely in the console. First, let's select Option 1 to view the available stocks and prices. As you can see, we have preloaded tickers with mock prices. Now, I will add a stock using Option 2. I'll enter AAPL and input a quantity of 5. Next, I'll add TSLA with a quantity of 2."*
* **Displaying & Saving Portfolio (0:45 - 1:15)**:
  > *"Let's select Option 3 to view our active portfolio. The tracker calculates individual values and provides a clean summary table showing our total investment of $1400. Next, I will export this portfolio to a CSV file using Option 4. The console confirms it is saved."*
* **Clearing & Loading Data (1:15 - 1:45)**:
  > *"To show that the load feature works, I will first clear our current portfolio using Option 6. When I view the portfolio now, it's empty. Now, I will select Option 5 to reload our saved portfolio.csv. The data is parsed, verified, and loaded right back in!"*
* **Outro (1:45 - 2:00)**:
  > *"This project displays key concepts like file I/O operations, error checking, list/dictionary lookups, and function-oriented design in Python. Thank you for watching, and feel free to check out the repository!"*

---

## Future Improvements

1. **Real-time Price Integration**: Incorporate the `yfinance` or Alpha Vantage API to pull live stock values instead of static prices.
2. **Interactive Visualizations**: Generate pie charts or line graphs of portfolio allocation using libraries like `matplotlib` or `seaborn`.
3. **Transaction History Log**: Maintain a log of purchase and sale histories with timestamps.
4. **Enhanced Data Store**: Upgrade the storage from a simple CSV file to an SQLite database for database relational tracking.

---

## Author

- **Gobinathan R**
- CodeAlpha Python Programming Intern
- Project Repository: [CodeAlpha_Task2_Stock_Portfolio](https://github.com/GobinathanR/CodeAlpha_Task2_Stock_Portfolio)
