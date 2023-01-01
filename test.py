import httpx
import trio


async def main():
    as_client = httpx.AsyncClient()
    req = await as_client.get("https://google.com")
    print(req)
    req = await as_client.get("https://google.com", proxies="http://127.0.0.1:8080", verify=False)
    print(req)

    httpx.get

trio.run(main)