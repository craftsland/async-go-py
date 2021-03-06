"""
Asynchronous requests using `requests` with `run_in_executor` of `asyncio`
"""

import asyncio

import requests


async def main():
    futures = [
        loop.run_in_executor(
            None,
            requests.get,
            'http://example.com'
        )
        for i in range(1000)
    ]
    return await asyncio.gather(*futures)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    _ = loop.run_until_complete(main())
