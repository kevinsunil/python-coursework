import requests
from bs4 import BeautifulSoup
import re
from pprint import pprint
import lxml
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
    "Accept-Language":"en-IN,en;q=0.9,ko-KR;q=0.8,ko;q=0.7,en-GB;q=0.6,en-US;q=0.5",

}
response = requests.get(url="https://www.amazon.in/Samsung-Internal-Solid-State-MZ-V7S500BW/dp/B07MFBLN7K/ref=pd_ci_mcx_mh_mcx_views_0?pd_rd_w=IzjrT&content-id=amzn1.sym.7938e11a-362b-421f-bd30-8dd8d3c4b65f&pf_rd_p=7938e11a-362b-421f-bd30-8dd8d3c4b65f&pf_rd_r=GAMZSYW0MD87T87HWWPW&pd_rd_wg=A4Wex&pd_rd_r=d1c737d9-64aa-4266-962c-0a430ab8014a&pd_rd_i=B07MFBLN7K",headers=headers)
soup = BeautifulSoup(response.text, 'lxml')
price = soup.find(name="span",class_="a-price-whole")
price = re.sub(",","",price.getText())
price = price[:-1]
price = int(price)
if price <= 4849:
    print("price is low go buy the device now")
