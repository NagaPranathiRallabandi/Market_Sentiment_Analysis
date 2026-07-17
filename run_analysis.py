import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

plt.style.use('ggplot')
pd.set_option('display.max_columns', None)

def run_pipeline():
    print("Loading datasets...")
    trades = pd.read_csv('data/historical_data.csv')
    sentiment = pd.read_csv('data/fear_greed_index.csv')
    
    print("Data shapes:")
    print(f"  Trades: {trades.shape}")
    print(f"  Sentiment: {sentiment.shape}")
    
    print("\nCleaning and processing dates...")
    trades['date'] = pd.to_datetime(trades['Timestamp IST'], dayfirst=True, errors='coerce').dt.date
    sentiment['date'] = pd.to_datetime(sentiment['date']).dt.date
    
    print("Merging datasets on date...")
    merged_df = pd.merge(trades, sentiment, on='date', how='left')
    print(f"  Merged dataset shape: {merged_df.shape}")
    
    print("\n--- Running 20 Exploratory Data Analysis (EDA) Steps ---")
    
    # 1. Trade count
    num_trades = merged_df.shape[0]
    print(f"1. Total Trades: {num_trades}")
    
    # 2. Trader count
    num_traders = merged_df['Account'].nunique()
    print(f"2. Total Unique Traders: {num_traders}")
    
    # 3. Unique Coins
    num_coins = merged_df['Coin'].nunique()
    print(f"3. Unique Coins: {num_coins}")
    
    # 4. Total Profit
    total_profit = merged_df['Closed PnL'].sum()
    print(f"4. Total Profit (USD): {total_profit:,.2f}")
    
    # 5. Average Profit
    avg_profit = merged_df['Closed PnL'].mean()
    print(f"5. Average Profit (USD): {avg_profit:,.2f}")
    
    # 6. Profit by Sentiment
    print("\n6. Total Profit by Sentiment Classification (USD):")
    profit_by_sentiment = merged_df.groupby('classification')['Closed PnL'].sum()
    print(profit_by_sentiment.map('{:,.2f}'.format))
    
    # 7. Average Profit by Sentiment
    print("\n7. Average Profit by Sentiment Classification (USD):")
    avg_profit_by_sentiment = merged_df.groupby('classification')['Closed PnL'].mean()
    print(avg_profit_by_sentiment.map('{:,.2f}'.format))
    
    # 8. Trades by Sentiment
    print("\n8. Number of Trades by Sentiment Classification:")
    trades_by_sentiment = merged_df['classification'].value_counts()
    print(trades_by_sentiment)
    
    # 9 & 10. Leverage
    leverage_col = [col for col in merged_df.columns if 'leverage' in col.lower()]
    if leverage_col:
        print(f"\n9. Average Leverage: {merged_df[leverage_col[0]].mean():.2f}x")
        print(f"10. Maximum Leverage: {merged_df[leverage_col[0]].max():.2f}x")
    else:
        print("\n9 & 10. Leverage column not present in the dataset (skipping).")
        
    # 11. Buy vs Sell Performance
    print("\n11. Buy vs Sell Performance (USD):")
    buy_sell_perf = merged_df.groupby('Side')['Closed PnL'].agg(['count', 'sum', 'mean'])
    print(buy_sell_perf)
    
    # 12. Profit by Coin
    print("\n12. Top 5 Most Profitable Coins (USD):")
    profit_by_coin = merged_df.groupby('Coin')['Closed PnL'].sum().sort_values(ascending=False)
    print(profit_by_coin.head(5).map('{:,.2f}'.format))
    print("\n12. Bottom 5 Least Profitable Coins (USD):")
    print(profit_by_coin.tail(5).map('{:,.2f}'.format))
    
    # 13. Top 10 Traders
    print("\n13. Top 10 Traders by Profit (USD):")
    top_traders = merged_df.groupby('Account')['Closed PnL'].sum().sort_values(ascending=False)
    print(top_traders.head(10).map('{:,.2f}'.format))
    
    # 14. Worst 10 Traders
    print("\n14. Worst 10 Traders by Profit (USD):")
    print(top_traders.tail(10).map('{:,.2f}'.format))
    
    # 15 & 16. Largest Wins and Losses
    idx_max = merged_df['Closed PnL'].idxmax()
    idx_min = merged_df['Closed PnL'].idxmin()
    print(f"\n15. Largest Winning Trade: Account {merged_df.loc[idx_max, 'Account']} on {merged_df.loc[idx_max, 'Coin']} PnL: ${merged_df.loc[idx_max, 'Closed PnL']:,.2f}")
    print(f"16. Largest Losing Trade: Account {merged_df.loc[idx_min, 'Account']} on {merged_df.loc[idx_min, 'Coin']} PnL: ${merged_df.loc[idx_min, 'Closed PnL']:,.2f}")
    
    # 17. Volume by Sentiment
    print("\n17. Trading Volume by Sentiment (USD):")
    vol_by_sentiment = merged_df.groupby('classification')['Size USD'].sum()
    print(vol_by_sentiment.map('{:,.2f}'.format))
    
    # 18. Average Position Size
    avg_pos_size = merged_df['Size USD'].mean()
    print(f"\n18. Average Position Size: ${avg_pos_size:,.2f}")
    
    # 19. Win Percentage
    win_trades = merged_df[merged_df['Closed PnL'] > 0]
    win_rate = (len(win_trades) / len(merged_df)) * 100
    print(f"\n19. Overall Winning Percentage: {win_rate:.2f}%")
    print("Win Rate by Sentiment:")
    for name, group in merged_df.groupby('classification'):
        group_win_rate = (len(group[group['Closed PnL'] > 0]) / len(group)) * 100
        print(f"  {name}: {group_win_rate:.2f}%")
        
    # 20. Profit Distribution Summary
    print("\n20. Profit Distribution Summary:")
    print(merged_df['Closed PnL'].describe())
    
    # Save Tables
    print("\nSaving tables to outputs/tables/...")
    os.makedirs('outputs/tables', exist_ok=True)
    profit_by_sentiment.to_csv('outputs/tables/profit_by_sentiment.csv')
    buy_sell_perf.to_csv('outputs/tables/buy_sell_performance.csv')
    profit_by_coin.to_csv('outputs/tables/profit_by_coin.csv')
    top_traders.to_csv('outputs/tables/top_traders.csv')
    
    # Generate Visualizations
    print("\nGenerating and saving visualizations to outputs/plots/...")
    os.makedirs('outputs/plots', exist_ok=True)
    
    # Graph 1
    plt.figure(figsize=(10,6))
    sns.barplot(x=profit_by_sentiment.index, y=profit_by_sentiment.values, palette='RdYlGn')
    plt.title('Total Profit by Sentiment (USD)')
    plt.ylabel('Total Profit')
    plt.xlabel('Market Sentiment')
    plt.tight_layout()
    plt.savefig('outputs/plots/fear_vs_greed_profit.png')
    plt.close()
    
    # Graph 2
    plt.figure(figsize=(10,6))
    sns.countplot(data=merged_df, x='classification', order=['Extreme Fear', 'Fear', 'Neutral', 'Greed', 'Extreme Greed'], palette='viridis')
    plt.title('Trade Count by Sentiment')
    plt.ylabel('Number of Trades')
    plt.xlabel('Market Sentiment')
    plt.tight_layout()
    plt.savefig('outputs/plots/trade_count.png')
    plt.close()
    
    # Graph 3
    plt.figure(figsize=(8,5))
    sns.barplot(data=merged_df, x='Side', y='Closed PnL', palette='Set2')
    plt.title('Average Profit by Trade Side')
    plt.ylabel('Average Closed PnL (USD)')
    plt.tight_layout()
    plt.savefig('outputs/plots/buy_vs_sell.png')
    plt.close()
    
    # Graph 4
    plt.figure(figsize=(12,6))
    sns.barplot(x=top_traders.head(10).values, y=top_traders.head(10).index, palette='Blues_r')
    plt.title('Top 10 Traders by Profit (USD)')
    plt.xlabel('Total Closed PnL (USD)')
    plt.ylabel('Account')
    plt.tight_layout()
    plt.savefig('outputs/plots/top_10_traders.png')
    plt.close()
    
    # Graph 5
    pnl_clean = merged_df['Closed PnL']
    q_low = pnl_clean.quantile(0.01)
    q_hi  = pnl_clean.quantile(0.99)
    filtered_pnl = pnl_clean[(pnl_clean > q_low) & (pnl_clean < q_hi)]
    plt.figure(figsize=(10,6))
    sns.histplot(filtered_pnl, bins=50, kde=True, color='purple')
    plt.title('Profit Distribution (Middle 98% of trades)')
    plt.xlabel('Closed PnL (USD)')
    plt.tight_layout()
    plt.savefig('outputs/plots/profit_distribution.png')
    plt.close()
    
    # Graph 6
    if leverage_col:
        plt.figure(figsize=(10,6))
        sns.histplot(merged_df[leverage_col[0]].dropna(), bins=30, kde=True, color='teal')
        plt.title('Leverage Distribution')
        plt.xlabel('Leverage')
        plt.tight_layout()
        plt.savefig('outputs/plots/leverage_distribution.png')
        plt.close()
    
    # Graph 7
    plt.figure(figsize=(10,8))
    numeric_cols = merged_df.select_dtypes(include=[np.number]).columns
    sns.heatmap(merged_df[numeric_cols].corr(), annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Correlation Heatmap')
    plt.tight_layout()
    plt.savefig('outputs/plots/correlation_heatmap.png')
    plt.close()
    
    # Graph 8
    plt.figure(figsize=(14,6))
    daily_profit = merged_df.groupby('date')['Closed PnL'].sum()
    daily_profit.plot(color='darkgreen')
    plt.title('Daily Profit Trend')
    plt.ylabel('Closed PnL (USD)')
    plt.xlabel('Date')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('outputs/plots/daily_profit_trend.png')
    plt.close()
    
    # Graph 9
    plt.figure(figsize=(10,6))
    top_coins = merged_df['Coin'].value_counts().head(10)
    sns.barplot(x=top_coins.values, y=top_coins.index, palette='rocket')
    plt.title('Top 10 Most Traded Coins (Trade Count)')
    plt.xlabel('Number of Trades')
    plt.ylabel('Coin')
    plt.tight_layout()
    plt.savefig('outputs/plots/most_traded_coins.png')
    plt.close()
    
    # Graph 10
    plt.figure(figsize=(10,6))
    avg_profit_coin = merged_df.groupby('Coin')['Closed PnL'].mean().sort_values(ascending=False).head(10)
    sns.barplot(x=avg_profit_coin.values, y=avg_profit_coin.index, palette='crest')
    plt.title('Top 10 Coins by Average Profit per Trade (USD)')
    plt.xlabel('Average Closed PnL (USD)')
    plt.ylabel('Coin')
    plt.tight_layout()
    plt.savefig('outputs/plots/avg_profit_per_coin.png')
    plt.close()
    
    print("Done! All analysis and plots have been generated and saved successfully.")

if __name__ == '__main__':
    run_pipeline()
