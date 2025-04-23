# from aiohttp import ClientSession
#
# class HTTPClient:
#     def __init__(self, base_url:str, api_key:str):
#         self._session = ClientSession(
#             base_url=base_url,
#             headers={
#                 'X-CMC_PRO_API_KEY': api_key
#             }
#         )
# #class CMCHTTPClient(HTTPClient):
#     async def get_listings(self):
#         async with self._session.get('') as resp:
#             result = await resp.json()
#             return result['data']
#
#     async def get_currency(self, currency_id: int):
#         async with self._session.get('') as resp:
#             result = await resp.json()
#             return result['data']
#
