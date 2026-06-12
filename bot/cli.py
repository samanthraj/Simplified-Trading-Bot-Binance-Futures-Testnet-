from logging_config import logger
from client import create_client
from orders import place_order
from validators import side_validator,order_type_validator,validate_quantity,validate_price
import argparse
import os
from dotenv import load_dotenv
load_dotenv()

def main():
    parser = argparse.ArgumentParser(
        description = "python trading bot cli"
        
    )
  
    parser.add_argument("--symbol")
    parser.add_argument("--side")
    parser.add_argument("--type")
    parser.add_argument("--quantity",required=True,
        type=float)
    parser.add_argument("--price")
    
    args = parser.parse_args()
   
    
    

    
    
    try:
        side_validator(args.side)
        order_type_validator(args.type)
        validate_quantity(args.quantity)
        validate_price(args.type,args.price)
        
        client = create_client(os.getenv("binance_test_api"),os.getenv("binance_test_secret"))
        response = place_order(client,args.symbol,args.side,args.type,args.quantity,args.price)
        print()
   
        if args.price:
            print(f"Price: {args.price}")

        print("\nOrder Response")

        print(
            f"Order ID: "
            f"{response.get('orderId')}"
        )

        print(
            f"Status: "
            f"{response.get('status')}"
        )

        print(
            f"Executed Qty: "
            f"{response.get('executedQty')}"
        )

        print("\nOrder Successful")     
        
        
    except Exception as e:    
        print(f'order failed:{e}')
if __name__ == "__main__":
  
    main()
            
    
    