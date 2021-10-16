from bs4 import BeautifulSoup 
import requests 
import csv
import pandas as pd

Product_Title = [] # Create a list to store the descriptions
price = []
# ratings = []
imgLink = []
productId = []
# Test=[]


pages = list(range(1,286))

for page in pages:
  req = requests.get("https://www.peridomicilio.com/abarrotes/page-{}/?sort_by=position&sort_order=asc&layout=short_list".format(page)).text  # URL of the website which you want to scrape
  #content = req.content # Get the content
  soup = BeautifulSoup(req,'html.parser')
  # print(soup.prettify())
  title = soup.find_all(class_='product-title')
  # print(len(title))
  for i in range(len(title)):
      Product_Title.append(title[i].text)
  # print(len(title))   
  # print(Product_Title)

  prices=soup.find_all(class_='ty-price')
  # print(len(prices))
  for i in range(len(prices)):
    price.append(prices[i].text)
  # print(price)

  # test = soup.find_all(class_='ty-price')
  # print(len(test))
  # for i in range(len(test)):
  #   Test.append(test[i].text)
  # print(Test)

  id = soup.find_all(class_='ty-control-group ty-sku-item cm-hidden-wrapper')
  # print(len(id))
  for i in range(len(id)):
    a=id[i].text.replace('\n',"")
    b=a.replace('Cod.artículo:',"")
    productId.append(b)
  # print(productId)

  img = soup.find_all(class_='ty-pict cm-image')
  for imgsrc in img:
    imgnew= imgsrc['src']
    imgLink.append(imgnew)
  # print(imgLink)

list_of_tuples = list(zip(Product_Title, productId,price,imgLink,Product_Title))

df = pd.DataFrame(list_of_tuples,
                  columns = ['Product Title', 'Product ID', 'Price', 'Image Link', 'Product Description'])


df.to_csv('Grocerries.csv')