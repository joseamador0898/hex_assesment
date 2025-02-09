# Hex Assessment - Quantitative Trading and Development

## Overview

This first part of this project implements a WebSocket client to stream and maintain an order book from an exchange, specifically designed to meet the following requirements:

## Requirements

### 1. Orderbook Storage
- The order book stores the top 5 levels of bids and asks.
- **Data Structures**:
  - **Bids**: Stored in a **max heap** to efficiently track and retrieve the highest bid prices.
  - **Asks**: Stored in a **min heap** to efficiently track and retrieve the lowest ask prices.
- **Justification**: Heaps are chosen for their O(log N) time complexity for insertions and deletions, making them optimal for maintaining the top levels of the order book in real-time.

### 2. Data Structure Justification
- **Bids**: A **max heap** is used to efficiently track the highest prices at the top, allowing quick retrieval and update.
- **Asks**: A **min heap** is used to efficiently track the lowest prices at the top, ensuring fast access and modification.
- **Why Heaps?**: Heaps are ideal for real-time order book management due to their logarithmic time complexity (O(log N)) for insertions and deletions, ensuring that the top N price levels are maintained with minimal computational overhead.

### 3. Asynchronous Updates
- The WebSocket client uses **`asyncio`** to handle updates asynchronously.
- **Benefit**: This ensures that order book updates do not block the main application, maintaining responsiveness and efficiency in processing incoming data.

### 4. Fail-Safe Code Design
- The WebSocket connection is designed to **automatically attempt to reconnect** if the connection is lost.
- **Objective**: To ensure that the main application flow is not interrupted even if the exchange’s server goes down, providing a robust and resilient solution.

### 5. AWS Instance with Lowest Latency
- **Approach**: Deploy EC2 instances in various AWS regions and ping `api.binance.com` or `api.binance.us` to determine the region with the lowest latency.
- **Latency Results** (as per [python-binance GitHub issue #189](https://github.com/sammchardy/python-binance/issues/189)):
  - **Tokyo**: 0.01s
  - **Seoul**: 0.042s
  - **New Jersey**: 0.01s
  - **Los Angeles**: 0.125s
  - **Frankfurt**: 0.245s
  - **London**: 0.24s
  - **Singapore**: 0.095s
  - **Sydney**: 0.126s
- **Insight**: The lowest latency can be achieved in Tokyo and New Jersey, making them ideal locations for deploying AWS instances when connecting to Binance servers.

---

# Trading Strategy - Exploiting Inefficiencies between Perpetual and Calendar Futures

## Overview

This part of the project focuses on exploiting the inefficiencies between perpetual futures and calendar (dated) futures on Binance US. The goal is to develop a trading strategy based on the spread between the funding rate of perpetual futures and the implied funding rate of calendar futures.

## Requirements and Calculations

### 1. Funding Rate for Perpetual Future
The funding rate for a perpetual future is calculated based on the difference between the perpetual future's mark price and the underlying index price, adjusted for interest rates and premium index.

**Formula:**
- def calculate_funding_rate(mark_price, index_price, interest_rate, premium_index):
- return (mark_price - index_price) / index_price + interest_rate - premium_index

### 2. Implied Funding Rate for Calendar Future
- The implied funding rate (or implied interest rate) for a calendar future is calculated by comparing the future's price to the spot price and adjusting for the time to -maturity.

- Formula:
- def calculate_implied_rate(future_price, spot_price, time_to_maturity):
    -return (future_price / spot_price - 1) / time_to_maturity

### 3. Trading the Spread between Perpetual and Calendar Futures
- The trading strategy is based on the spread between the funding rate of the perpetual future and the implied rate of the calendar future. Trades are initiated when the -spread crosses a certain threshold:

- Long Perpetual, Short Calendar: If the funding rate is significantly lower than the implied rate.
- Short Perpetual, Long Calendar: If the funding rate is significantly higher than the implied rate.
- Spread Calculation Formula:
- def calculate_spread(funding_rate, implied_rate):
- return funding_rate - implied_rate
- Example Results from Analysis
- Funding Rate for BTC/USDT Perpetual Future: 0.05% (as an example based on historical data).
- Implied Funding Rate for BTC/USDT Calendar Future: 0.08% (as an example based on historical data).
- Trading Signal: A signal to go Long Perpetual and Short Calendar based on the spread of -0.03%.
