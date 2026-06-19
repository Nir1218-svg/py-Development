import time
import requests
import schedule
import smtplib
from email.message import EmailMessage
def scrape_temp():
    api_key="cur_live_h7laJNRxHYGkFcR4mnYEChqzOV6KG9QKMHfMpB03"
    api_url=f"https://api.currencyapi.com/v3/latest?apikey={api_key}&base_currency=USD&currencies=BDT"
    response=requests.get(api_url)
    data=response.json()
    print(response.status_code)
    bdt=data["data"]["BDT"]["value"]
    return bdt
