# Engie API

Api for the Engie Excersise

## Preconditions:

- Python 3

## Clone the project

```
git clone https://github.com/GonzaloJCY/Engie_API.git
```

## Run local

### Create new test environment

```
python -m venv venv

source venv/bin/activate
```

### Install dependencies

```
pip install -r requirements.txt
```

### Run server

```
uvicorn app.main:app --reload
```

### Run test

```
pytest test/test.py
```
