import asyncio

# Define an asynchronous iterator
class AsyncIterator():
    # Constructor ,define some state
    def __init__(self):
        self.counter = 0
    # Create an instance of the iterator
    def __aiter__(self):
        return self
    
    # Return the next awaitable
    async def __anext__(self):
        # Check for no further items
        if self.counter >= 10:
            raise StopAsyncIteration
        # Increment the counter
        self.counter += 1
        # Simulate work
        await asyncio.sleep(1)
        # Return the counter value
        return self.counter
    
# Main coroutine
async def main():
    # Loop over async iterator with async for loop
    async for item in AsyncIterator():
        print(item)
    
# Execute the asyncio program
asyncio.run(main())