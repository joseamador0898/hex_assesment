import asyncio
import websockets
import json
import heapq

class OrderBook:
    def __init__(self, levels=5):
        self.levels = levels
        # Max heap for bids to efficiently track the highest prices at the top
        self.bids = []
        # Min heap for asks to efficiently track the lowest prices at the top
        self.asks = []

    def update(self, data):
        # Update bids
        for entry in data['b']:
            price, quantity = float(entry[0]), float(entry[1])
            if quantity == 0:
                # Remove the bid if quantity is 0
                self.bids = [(p, q) for p, q in self.bids if p != -price]
                heapq.heapify(self.bids)
            else:
                # Push the bid into max heap (negate price for max heap behavior)
                heapq.heappush(self.bids, (-price, quantity))
                # Keep only the top N (levels) bids
                if len(self.bids) > self.levels:
                    heapq.heappop(self.bids)

        # Update asks
        for entry in data['a']:
            price, quantity = float(entry[0]), float(entry[1])
            if quantity == 0:
                # Remove the ask if quantity is 0
                self.asks = [(p, q) for p, q in self.asks if p != price]
                heapq.heapify(self.asks)
            else:
                # Push the ask into min heap
                heapq.heappush(self.asks, (price, quantity))
                # Keep only the top N (levels) asks
                if len(self.asks) > self.levels:
                    heapq.heappop(self.asks)

    def display(self):
        print("Bids:")
        # Display bids sorted in descending order
        for price, quantity in sorted(self.bids, reverse=True):
            print(f"Price: {-price}, Quantity: {quantity}")
        print("Asks:")
        # Display asks sorted in ascending order
        for price, quantity in sorted(self.asks):
            print(f"Price: {price}, Quantity: {quantity}")

async def handle_orderbook(orderbook, uri):
    async for websocket in websockets.connect(uri):
        try:
            async for message in websocket:
                data = json.loads(message)
                orderbook.update(data)
                orderbook.display()
        except websockets.ConnectionClosed:
            print("Connection closed. Reconnecting...")
            continue

async def main():
    uri = "wss://stream.binance.us:9443/ws/btcusdt@depth"  # Binance.US WebSocket URI
    orderbook = OrderBook(levels=5)
    await handle_orderbook(orderbook, uri)

if __name__ == "__main__":
    asyncio.run(main())
