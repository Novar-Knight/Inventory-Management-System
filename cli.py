import requests

BASE_URL = 'http://127.0.0.1:5000'

while True:
    print("""
        1.View All Inventory
        2.View Product by ID
        3.Add Product Manually
        4.Update Product
        5.Delete Product
        6.Search API
        7.Exit
        """)
    choice = input('Select Option: ')

    if choice == '1':
        print(requests.get(f'{BASE_URL}/inventory').json())

    elif choice == '2':
        item_id = input('ID: ')
        print(requests.get(f'{BASE_URL}/inventory/{item_id}').json())

    elif choice == '3':
        data = {
            'product_name': input('Name: '),
            'brands': input('Brand: '),
            'ingredients_text': input('Ingredients: '),
            'price': float(input('Price: ')),
            'stock': int(input('Stock: '))
        }
        print(requests.post(f'{BASE_URL}/inventory', json=data).json())

    elif choice == '4':
        item_id = input('ID: ')
        field = input('Field(price/stock): ')
        value = input('Value: ')
        if field == 'price':
            value = float(value)
        else:
            value = int(value)
        print(requests.patch(f'{BASE_URL}/inventory/{item_id}', json={field: value}).json())

    elif choice == '5':
        item_id = input('ID: ')
        print(requests.delete(f'{BASE_URL}/inventory/{item_id}').json())

    elif choice == '6':
        name = input('Product name: ')
        print(requests.get(f'{BASE_URL}/search/{name}').json())

    elif choice == '7':
        break