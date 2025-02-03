# Fun With Fruits project Backend

The backend part of Fun With Fruits is developed with [FastAPI](https://fastapi.tiangolo.com/).

## Models

The project uses SQLAlchemy to define the database models. The main model in this project is the `Fruit` model, which represents a fruit entity with attributes such as `id`, `name` and `color`.

## Endpoints

The API provides the following endpoints to interact with the `Fruit` model:

- **`GET /fruits`**: Retrieve a list of all fruits.
- **`GET /fruits/{fruit_id}`**: Retrieve a specific fruit by its ID.
- **`POST /fruits`**: Create a new fruit.
- **`PUT /fruits/{fruit_id}`**: Update an existing fruit by its ID.
- **`DELETE /fruits/{fruit_id}`**: Delete a fruit by its ID.

### Example Requests

- **GET /fruits**

  ```sh
  curl -X 'GET' \
    'http://127.0.0.1:8000/fruits' \
    -H 'accept: application/json'
  ```

- **GET /fruits/{fruit_id}**

  ```sh
  curl -X 'GET' \
    'http://127.0.0.1:8000/fruits/1' \
    -H 'accept: application/json'
  ```

- **POST /fruits**

  ```sh
  curl -X 'POST' \
    'http://127.0.0.1:8000/fruits' \
    -H 'accept: application/json' \
    -H 'Content-Type: application/json' \
    -d '{
    "name": "Apple",
    "color": "Red",
  }'
  ```

- **PUT /fruits/{fruit_id}**

  ```sh
  curl -X 'PUT' \
    'http://127.0.0.1:8000/fruits/1' \
    -H 'accept: application/json' \
    -H 'Content-Type: application/json' \
    -d '{
    "color": "Green",
  }'
  ```

- **DELETE /fruits/{fruit_id}**

  ```sh
  curl -X 'DELETE' \
    'http://127.0.0.1:8000/fruits/1' \
    -H 'accept: application/json'
  ```

## Running the Project

To run the project, use the following command:

```sh
uvicorn src.main:app --reload
```

This will start the FastAPI server, and you can access the API documentation at `http://127.0.0.1:8000/docs` (Swagger) or `http://127.0.0.1:8000/redoc` (ReDoc).
