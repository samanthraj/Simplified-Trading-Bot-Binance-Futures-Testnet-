from binance.client import Client


def create_client(api_key:str,api_secret:str)->Client:
    """ this creates and returns binance futures testnet client"""
    client = Client(
        
        api_key = api_key,
        api_secret = api_secret
        
        
    )
    client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"
    
    return client
    


    
