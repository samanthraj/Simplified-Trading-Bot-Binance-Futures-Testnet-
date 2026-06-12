from logging_config import logger
def side_validator(side:str):
    logger.info("side validation request")
    if side in ["BUY","SELL"]:
        logger.info(f"side is {side}")
        
        return True
    else:
        logger.error("side validation failed")
        raise ValueError("order type must be buy or sell")
def order_type_validator(type:str):
    
    if type in ["MARKET","LIMIT"]:
        return True
    else:
        raise ValueError("order type must be Market or Limit")
    
def validate_quantity(quantity:int):
    if quantity<0:
        raise ValueError("quantity must be higher than 0")

def validate_price(order_type:str, price:int):
    if order_type == "Limit" and price == None:
        return ValueError("price is required for limit orders")
    
    
                
        
    