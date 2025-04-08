 
import requests
import os
from dotenv import load_dotenv

load_dotenv()

# def get_orders():
#     url = f"{os.getenv('ERP_BASE_URL')}/orders/v1/list"
#     headers = {
#         "Authorization": f"Bearer {os.getenv('ERP_OAUTH_TOKEN')}"
#     }
#     response = requests.get(url, headers=headers)
#     if response.status_code == 200:
#         return response.json()
#     else:
#         return {"error": "ERP API call failed"}


# Optional Mock Data (For Testing):
def get_orders():
    return [
        {"order_id": 1, "customer": "Reliance", "status": "shipped"},
        {"order_id": 2, "customer": "Infosys", "status": "pending"},
    ]
