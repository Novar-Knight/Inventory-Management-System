from app import app

# Create test client
client = app.test_client()

# TEST: Get all inventory
def test_get_inventory():
    response = client.get('/inventory')
    assert response.status_code == 200

# TEST: Get single item
def test_get_single_item():
    response = client.get('/inventory/1')
    assert response.status_code == 200

# TEST: Add new item (POST)
def test_add_item():
    response = client.post('/inventory', json={
        "product_name": "Bread",
        "brands": "TestBrand",
        "ingredients_text": "Flour, Water",
        "price": 100,
        "stock": 5
    })
    assert response.status_code == 201

# TEST: Update item (PATCH)
def test_update_item():
    response = client.patch('/inventory/1', json={
        "price": 999
    })
    assert response.status_code == 200

# TEST: Delete item
def test_delete_item():
    response = client.delete('/inventory/1')
    assert response.status_code == 200

# TEST: External API search route
def test_search_api():
    response = client.get('/search/milk')
    assert response.status_code in [200, 404]