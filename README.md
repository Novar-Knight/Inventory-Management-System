# Inventory-Management-System(Flask + OpenFoodFacts API)

# 1 .FEATURES
> Full CRUD operations (Create, Read, Update, Delete)
> External API integration (OpenFoodFacts)
> Import products from external API into local inventory
> CLI interface for easy interaction
> Mock database using Python list
> Error handling for invalid requests

# 2 .PROJECT STRUCTURE

```bash
├── app.py
├── cli.py
├── Pipfile
├── Pipfile.lock
├── __pycache__
│   ├── app.cpython-312.pyc
│   └── test_app.cpython-312-pytest-9.0.3.pyc
├── README.md
├── requirements.txt
└── test_app.py
```

# 3 .INSTALLATIONS & SETUP

# a.CLONE THE REPOSITORY

```bash
git clone https://github.com/Novar-Knight/Inventory-Management-System.git
cd inventory-project
```

# b.Create virtual environment
```bash
pipenv shell
```

# c.Install packages 
```bash
pipenv install flask request pytest
```

# d.Run The Application

🔹Start Flask server;
```bash
python app.py
```

# e. Run CLI application

🔹Open a new terminal:
```bash
python cli.py

```
# 4.API Endpoints
🔹 Inventory Routes

 GET /inventory/Get all items   
 GET /inventory/<id> / Get single item
 POST /inventory/ Add new item    
 PATCH  /inventory/<id>/ Update item     
 DELETE /inventory/<id> Delete item     

🔹 External API Routes
 GET/search/<name>/Search product in OpenFoodFacts 
 POST/import/<name>/ Import product into inventory 

# 5 .CLI Features
🔹CLI allows users to:

```bash
1. View All
2. View One
3. Add Item
4. Update Item
5. Delete Item
6. Search API
7. Import from API
8. Exit
```
🔹 External API Used
.  OpenFoodFacts API
.  Used to fetch real product data like:
    . Product name
    . Brand
    . Ingredients


# 6 .Technologies Used

```bash
Python
Flask
Requests
Pytest
OpenFoodFacts API
```