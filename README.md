# REST API With Flask & SQLAlchemy
>Products API using Python Flask, SQLAlchemy and Marshmallow

## Quick Start 
```sh
# Activate venv
$ source venv/bin/activate

# Install dependencies
$ pip install -r requirements.txt

# Create DB
$ python
>> from app import db
>> db.create_all()
>> exit()

# Run Server (http://localhst:5000)
python app.py
```

## Endpoints
* GET /product
* GET /product/:id
* POST /product
* PUT /product/:id
* DELETE /product/:id