Hex Assessment - Quantitative Development
Overview
This project implements a WebSocket client to stream and maintain an order book from an exchange, specifically designed to meet the following requirements:

Requirements
1. Orderbook Storage
The order book stores the top 5 levels of bids and asks.
Data Structures:
Bids: Stored in a max heap to efficiently track and retrieve the highest bid prices.
Asks: Stored in a min heap to efficiently track and retrieve the lowest ask prices.
Justification: Heaps are chosen for their O(log N) time complexity for insertions and deletions, making them optimal for maintaining the top levels of the order book in real-time.
2. Data Structure Justification
Bids: A max heap is used to efficiently track the highest prices at the top, allowing quick retrieval and update.
Asks: A min heap is used to efficiently track the lowest prices at the top, ensuring fast access and modification.
Why Heaps?: Heaps are ideal for real-time order book management due to their logarithmic time complexity (O(log N)) for insertions and deletions, ensuring that the top N price levels are maintained with minimal computational overhead.
3. Asynchronous Updates
The WebSocket client uses asyncio to handle updates asynchronously.
Benefit: This ensures that order book updates do not block the main application, maintaining responsiveness and efficiency in processing incoming data.
4. Fail-Safe Code Design
The WebSocket connection is designed to automatically attempt to reconnect if the connection is lost.
Objective: To ensure that the main application flow is not interrupted even if the exchange’s server goes down, providing a robust and resilient solution.
5. AWS Instance with Lowest Latency
Approach: Deploy EC2 instances in various AWS regions and ping api.binance.com or api.binance.us to determine the region with the lowest latency.
Latency Results (as per python-binance GitHub issue #189):
Tokyo: 0.01s
Seoul: 0.042s
New Jersey: 0.01s
Los Angeles: 0.125s
Frankfurt: 0.245s
London: 0.24s
Singapore: 0.095s
Sydney: 0.126s
Insight: The lowest latency can be achieved in Tokyo and New Jersey, making them ideal locations for deploying AWS instances when connecting to Binance servers.
