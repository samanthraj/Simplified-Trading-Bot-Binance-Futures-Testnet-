from logging_config import logger

def place_order(
client,
symbol,
side,
type,
quantity,
price
):
    
    try:
        logger.info(f'new order of  {quantity} {symbol}  at {price} {side}is requested ')
        if type == "MARKET":
                    response = client.futures_create_order(
                        side = side,
                        type = "MARKET",
                        quantity = quantity,
                        symbol = symbol,
                        
                    )
        elif type == "Limit":
            response = client.futures_create_order(
                        side = side,
                        type = "LIMIT",
                        symbol = symbol,
                        quantity = quantity,
                        price = price,
                        timeInForce = "GTC"
                        
                        
                    )
            
            
        else:
            raise ValueError(
                f"unsupported order type:{type}"
            )    
        logger.info(
            f"order is executed"
        )                
        return response 
                      
    except Exception as e:
        logger.error(f'order failed:{e}')
        
        raise
                   
                        
                     
        
        
    
    
       