# Given a dictionary of products and their prices, find the product with the highest price.

def most_expensive_product(products):
    return max(products.items(), key=lambda x:x[1])
products = {
    "Laptop" : 30000,
    "Tv" : 40000,
    "Mobile":20000,
    "Tablets":45000
}
products,price = most_expensive_product(products)
print(f"The most expensive product is'{products}' with price '{price}'")