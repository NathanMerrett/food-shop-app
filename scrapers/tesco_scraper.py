# import requests
# from bs4 import BeautifulSoup
# import time

# URL = "https://www.tesco.com/groceries/en-GB/shop/bakery/all"

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
# }

# response = requests.get(URL, headers=headers)

# soup = BeautifulSoup(response.content, 'html.parser')

# # Let's assume each product is in a div with class 'product-item'
# products = soup.find_all('div', class_='product-details--wrapper')

# for product in products:
#     # Extracting product name
#     product_name = product.find('h2', class_='product-title--title').text

#     # # Extracting product price
#     # product_price = product.find('span', class_='product-price').text

#     # # Extracting product description
#     # product_description = product.find('p', class_='product-description').text

#     print(f"Product Name: {product_name}")
#     # print(f"Price: {product_price}")
#     # print(f"Description: {product_description}\n")

