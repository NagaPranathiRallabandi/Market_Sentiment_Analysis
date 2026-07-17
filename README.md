# Market Sentiment Analysis

## Project Overview
This project explores the relationship between trader performance and market sentiment, using historical data from Hyperliquid and the Bitcoin Fear and Greed Index. The goal is to uncover hidden patterns and deliver insights for smarter trading strategies.

## Dataset Description
- **Bitcoin Market Sentiment Dataset:** Contains daily Fear/Greed classifications.
- **Historical Trader Data (Hyperliquid):** Contains trader accounts, symbols, execution prices, trade sizes, sides, times, closed PnL, leverage, etc.

## Tools Used
- Python
- Pandas, NumPy
- Matplotlib, Seaborn
- Jupyter Notebooks

## Analysis Performed
- Data cleaning and preprocessing
- Merging historical trades with daily market sentiment
- Exploratory Data Analysis (EDA) covering trade frequencies, profit distributions, and leverage behavior
- Evaluating Buy vs Sell performance
- Profitability and volume analysis segmented by market sentiment (Fear vs Greed)

## Key Findings
*(To be populated after running the analysis notebook)*

## How to Run
1. Clone this repository.
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # On Windows (Git Bash): source venv/Scripts/activate
   # On Windows (CMD): venv\Scripts\activate
   # On Windows (PowerShell): .\venv\Scripts\Activate.ps1
   # On macOS/Linux: source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Download the datasets into the `data/` folder:
   - `historical_data.csv`
   - `fear_greed.csv`
5. Navigate to the `notebooks/` directory and start Jupyter:
   ```bash
   jupyter notebook
   ```
6. Open `analysis.ipynb` and run the cells.
