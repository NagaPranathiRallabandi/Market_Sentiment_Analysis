# Quantitative Analysis Report: Trader Performance and Market Sentiment

**Author:** Naga Pranathi Rallabandi  
**Date:** July 2026  
**Subject:** Exploratory Data Analysis (EDA) on Hyperliquid Trader Performance and Bitcoin Fear & Greed Index  

---

## 1. Executive Summary

This report presents a quantitative behavioral analysis exploring how market sentiment (measured by the Bitcoin Fear and Greed Index) impacts the execution efficiency, volume, and profitability of traders. 

By analyzing **211,224 trades** executed across **32 unique accounts** on Hyperliquid and merging them with daily sentiment classifications, we uncover several key insights:
1. **Fear is the Accumulation Engine:** The highest total trading volume ($483.3M) and second-highest total profits ($3.36M) occur during **Fear** regimes.
2. **Extreme Greed is Highly Efficient but Fleeting:** Trades during **Extreme Greed** exhibit the highest win rate (46.49%) and highest average profit per trade ($67.89).
3. **The "Greed Trap":** When the market is in standard **Greed**, trader win rates decline to 38.48%, and average profit falls compared to Fear regimes. This suggests retail overtrading and FOMO buying.
4. **Shorting Dominance:** Sell-side executions generated **$6.59M** in profits (Average: $60.71/trade), compared to **$3.71M** for buy-side executions (Average: $36.10/trade).
5. **Speculative Losses:** Blue-chip assets (BTC, ETH, SOL, HYPE) accounted for the majority of gains, while speculative meme coins (e.g., TRUMP, FARTCOIN) caused catastrophic losses.

---

## 2. Project Objective

The goal of this analysis is to evaluate if sentiment-based indicators can serve as actionable guidelines for risk management. Specifically, we seek to:
* Determine which market sentiment conditions yield the highest absolute and average trader profitability.
* Analyze transaction volume distribution and win rates across different sentiment regimes.
* Contrast the performance of long (Buy) vs. short (Sell) executions.
* Highlight the top-performing and worst-performing assets.

---

## 3. Dataset Characteristics

The analysis utilizes two core datasets spanning the 2018–2026 period:

1. **Hyperliquid Trader Dataset:** 
   * **Size:** 211,224 rows, 16 columns.
   * **Metrics:** Account Address, Coin (Symbol), Side (BUY/SELL), Closed PnL (realized profit/loss), Size USD, and Timestamp IST.
2. **Bitcoin Fear & Greed Index:**
   * **Size:** 2,644 rows, 4 columns.
   * **Metrics:** Date, Value (0–100), Classification (Extreme Fear, Fear, Neutral, Greed, Extreme Greed).

*Data Cleaning:* Trade timestamps were parsed from the string-based `Timestamp IST` using a Day-First parser (`DD-MM-YYYY`) and converted to daily dates to ensure seamless merging with the daily sentiment index.

---

## 4. Key Performance Indicators (KPIs)

Below is an overview of the global trading performance metrics:

| Metric | Value |
| :--- | :--- |
| **Total Trades** | 211,224 |
| **Unique Traders (Accounts)** | 32 |
| **Unique Assets Traded** | 246 |
| **Total Profit Generated** | $10,296,958.94 |
| **Average Profit per Trade** | $48.75 |
| **Overall Winning Percentage** | 41.13% |
| **Average Position Size** | $5,639.45 |

---

## 5. Sentiment-Based Performance Breakdown

### 5.1 Profitability and Volume by Sentiment
Integrating the daily Fear & Greed index reveals how traders perform across different market cycles:

| Sentiment | Trade Count | Total Profit (USD) | Average Profit (USD) | Win Rate (%) | Trading Volume (USD) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Extreme Fear** | 21,400 | $739,110.25 | $34.54 | 37.06% | $114,484,261.44 |
| **Fear** | 61,837 | $3,357,155.44 | $54.29 | 42.08% | $483,324,789.79 |
| **Neutral** | 37,686 | $1,292,920.68 | $34.31 | 39.70% | $180,242,063.08 |
| **Greed** | 50,303 | $2,150,129.27 | $42.74 | 38.48% | $288,582,494.72 |
| **Extreme Greed** | 39,992 | $2,715,171.31 | $67.89 | 46.49% | $124,465,164.57 |

#### Key Sentiment Insights:
* **The Fear Volume Peak:** Traders transact the most heavily during **Fear** conditions, posting 61,837 trades and $483M in volume. This indicates strong accumulation behavior or high positioning adjustments when prices drop.
* **The Greed Slump:** When the market shifts from Fear to **Greed**, the win rate drops significantly (42.08% $\rightarrow$ 38.48%) and average profit drops to $42.74. This represents the classic "Greed Trap," where traders Chase rallies and exit late.
* **Extreme Greed Windfall:** **Extreme Greed** delivers the highest average trade profitability ($67.89) and win rate (46.49%), suggesting momentum traders capturing clean trends, though volume ($124.5M) is much lower than in Fear.

---

## 6. Execution and Asset Analysis

### 6.1 Buy vs. Sell Performance
Analyzing the execution side shows that short/exit positions (Sells) are significantly more profitable on average than long entries (Buys):

* **BUY (Longs/Entries):** 102,696 trades | Total Profit: **$3,707,811.29** | Average Profit: **$36.10**
* **SELL (Shorts/Exits):** 108,528 trades | Total Profit: **$6,589,147.65** | Average Profit: **$60.71**

*Insight:* Sell executions yielded nearly **double** the average profit of buy executions. This implies these traders are highly proficient at shorting volatile drops or executing structured, profitable exit scales during market distributions.

---

### 6.2 Asset Performance (Top vs. Bottom Coins)
Out of 246 coins traded, blue-chip assets and native protocols generated the highest absolute profits, while speculative meme coins were highly destructive to capital.

#### Top 5 Most Profitable Coins:
1. **@107 (Native Protocol/Token):** $2,783,912.92
2. **HYPE:** $1,948,484.60
3. **SOL:** $1,639,555.93
4. **ETH:** $1,319,978.84
5. **BTC:** $868,044.73

#### Bottom 5 Least Profitable Coins:
1. **TRUMP (PolitiFi Meme):** -$364,824.91
2. **FARTCOIN (Speculative Meme):** -$100,687.21
3. **ADA:** -$28,113.46
4. **IO:** -$21,893.91
5. **PAXG (Tokenized Gold):** -$18,688.87

*Insight:* High-beta meme coins like `TRUMP` and `FARTCOIN` represented significant losses. On the other hand, core network tokens (`ETH`, `SOL`, `BTC`) and native project assets (`HYPE`, `@107`) provided steady, substantial gains.

---

### 6.3 Trader Performance Volatility
The 32 accounts analyzed displayed massive performance disparity:
* **Top Trader:** `0xb1231a4a2dd02f2276fa3c5e2a2f3436e6bfed23` generated **$2,143,382.60** in cumulative profits.
* **Worst Trader:** `0x8170715b3b381dffb7062c0298972d4727a0a63b` lost **-$167,621.12** in cumulative profits.

#### Outlier Case Study:
Interestingly, account `0x083384f897ee0f19899168e3b1bec365f52a9012` held both:
* **The Largest Winning Trade:** **+$135,329.09** on ETH.
* **The Largest Losing Trade:** **-$117,990.10** on ETH.

This demonstrates that high-volume market makers/size-traders operate with large position sizes, resulting in high PnL variance.

---

## 7. Visualizations

The generated visualizations are saved in the `outputs/plots/` directory for reference:

1. **Total Profit by Sentiment** (`outputs/plots/fear_vs_greed_profit.png`): Illustrates the distribution of profits across market sentiments, clearly showing that Fear and Extreme Greed dominate total gains.
2. **Trade Count by Sentiment** (`outputs/plots/trade_count.png`): Visualizes trade frequency, illustrating the peak during Fear.
3. **Average Profit by Side** (`outputs/plots/buy_vs_sell.png`): Displays the superior efficiency of Sell-side orders compared to Buy-side orders.
4. **Profit Distribution** (`outputs/plots/profit_distribution.png`): A histogram mapping the middle 98% of trade PnLs, showing a heavily clustered normal distribution centered slightly above zero, with long tails.
5. **Most Traded Coins** (`outputs/plots/most_traded_coins.png`): Illustrates which assets occupy the highest trade count.
6. **Average Profit per Coin** (`outputs/plots/avg_profit_per_coin.png`): Highlights the top-performing coins by average trade return.
7. **Daily Profit Trend** (`outputs/plots/daily_profit_trend.png`): A historical timeline of cumulative daily PnL showing overall portfolio growth.

---

## 8. Conclusions & Actionable Strategies

Based on the empirical evidence, we define three core strategic recommendations for trade and risk managers:

1. **The "Greed" Deleveraging Protocol:**
   * *Observation:* Standard "Greed" regimes show a noticeable drop in win rate (38.48%) and lower average profits.
   * *Action:* Reduce default leverage by 30-50% during standard Greed days to guard against sudden reversals, as retail FOMO often peaks here.
2. **Capitalize on Fear Accumulation:**
   * *Observation:* Fear days show the highest trading frequency (61k+ trades) and solid average profits ($54.29).
   * *Action:* Allocate larger capital limits for buy-limit order grids during Fear cycles. Fear represents the safest period for passive spot/long accumulation.
3. **Meme Coin Restriction Policy:**
   * *Observation:* Speculative meme coins like `TRUMP` and `FARTCOIN` were primary profit drains.
   * *Action:* Place strict trading limits or ban speculative assets (e.g. non-utility meme coins) from high-capital accounts. Focus trading operations primarily on high-liquidity blue-chips (BTC, ETH, SOL) and native protocols.
