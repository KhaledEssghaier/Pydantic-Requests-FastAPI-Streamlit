# Pydantic Project

This project contains three main components demonstrating different Python frameworks and libraries:

## 1. Streamlit Application (`main.py`)

A data visualization and interactive application built with Streamlit. Features include:
- Input for favorite movies with display
- Interactive button with click response
- Display of formatted markdown text with colors and emojis
- Reading and displaying data from a CSV file (`movies.csv`)
- Random data charts (bar chart and line chart)
- Mortgage repayments calculator with inputs for home value, deposit, interest rate, and loan term
- Calculation and display of monthly repayments, total repayments, total interest, and payment schedule chart

### Running the Streamlit App

Make sure you have Streamlit installed:

```bash
pip install streamlit pandas numpy
```

Run the app with:

```bash
streamlit run main.py
```

Ensure the file `movies.csv` is present in the same directory for the data display feature.

---

## 2. FastAPI Application (`FastAPI.py`)

A simple REST API built with FastAPI to manage items. Features include:
- Root endpoint returning a hello world message
- Create new items with POST `/items`
- Retrieve an item by ID with GET `/items/{item_id}`
- List items with GET `/items`

### Running the FastAPI App

Make sure you have FastAPI and Uvicorn installed:

```bash
pip install fastapi uvicorn
```

Run the app with:

```bash
uvicorn FastAPI:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

---

## 3. Pydantic Model Example (`Pydantic.py`)

Demonstrates usage of Pydantic for data validation and serialization:
- Defines a `User` model with fields `name`, `email` (validated as email), and `account_id` (validated to be positive)
- Shows example validation error handling
- Shows conversion between model instances and JSON/dictionaries

### Running the Pydantic Example

Make sure you have Pydantic installed:

```bash
pip install pydantic
```

Run the script with:

```bash
python Pydantic.py
```

---

## Dependencies

- streamlit
- pandas
- numpy
- fastapi
- uvicorn
- pydantic

Install all dependencies with:

```bash
pip install streamlit pandas numpy fastapi uvicorn pydantic
```

---

## Notes

- The Streamlit app expects a `movies.csv` file in the same directory for displaying movie data.
- The FastAPI app uses an in-memory list to store items; data will be lost on server restart.
