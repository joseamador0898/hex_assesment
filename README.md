# Hex Assesment
Quant Dev
Requirements:
1.	Orderbook Storage (Requirement 1):
o	The order book stores the top 5 levels of bids and asks using max heap and min heap, respectively.
2.	Data Structure Justification (Requirement 2):
o	Bids: Stored in a max heap to efficiently track and retrieve the highest bid prices.
o	Asks: Stored in a min heap to efficiently track and retrieve the lowest ask prices.
o	Justification: Heaps are chosen for their O(log N) time complexity for insertions and deletions, which is optimal for maintaining the top levels of the order book in real-time.
3.	Asynchronous Updates (Requirement 3):
o	The WebSocket client uses asyncio to handle updates asynchronously, ensuring that order book updates do not block the main application.
4.	Fail-Safe Code Design (Requirement 4):
o	The WebSocket connection is designed to automatically attempt to reconnect if the connection is lost, ensuring that the main application flow is not interrupted even if the exchange’s server goes down.
5.	AWS Instance with Lowest Latency (Requirement 5):
o	Approach: To find the AWS instance with the lowest latency, deploy EC2 instances in various AWS regions and ping api.binance.com/ ping api.binance.us
For Binance, the results are as follows as per (https://github.com/sammchardy/python-binance/issues/189):
So you can get as low as 10ms including already the calculation from the server. It's not just ping.
•	Tokyo - 0.01s*
•	Seul - 0.042s*
•	New Jersey - 0.01s*
•	Los Angeles - 0.125s*
•	Frankfurt - 0.245s*
•	London - 0.24s*
•	Singapore - 0.095s*
•	Sydney - 0.126s*

