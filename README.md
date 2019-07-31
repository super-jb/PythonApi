# Orders API  

## Dependencies  
* Python 3   
* Docker (make sure you have docker setup and running locally)  
* Flask  
* Shelve  

## Resources  
https://hub.docker.com/_/python  
https://docs.python.org/3/library/shelve.html  
https://palletsprojects.com/p/flask/  
https://flask.palletsprojects.com/en/1.1.x/patterns/sqlite3/  
https://flask-restful.readthedocs.io/en/latest/  

## Commands  
docker-compose build (builds solution in docker)
docker-compose up (runs solution in docker, endpoints available running locally)
* after invoking a POST request, orders.db will be created locally  

## API  

**Definition**  
`GET /orders`  
localhost:5000/api/orders  
**Response**  
- `200 OK` on success  
```json
[
  {
    "id": 1,
    "quantity": 2,
    "productName": "pen"
  },
  {
    "id": 2,
    "quantity": 3,
    "productName": "tape"
  },
  {
    "id": 3,
    "quantity": 1,
    "productName": "glue"
  }
]
```  

**Definition**  
`GET /orders{id}`  
localhost:5000/api/orders/1  
**Response**  
- `200 OK` on success  
- `404 Not Found` if order doesn't exist  
```json
{
  "id": 1,
  "quantity": 2,
  "productName": "pen"
}
```
  
**Definition**  
- `201 OK` on success  
- `409 Conflict` when id already exists  
`POST /orders`  
localhost:5000/api/orders  
**Body**  
```json 
{
  "quantity": 2,
  "productName": "pen"
}
```  
**Response**  
```json
{
  "id": 1,
  "quantity": 2,
  "productName": "pen"
}
```
  
**Definition**  
`DELETE /orders{id}`  
localhost:5000/api/orders/1  
**Response**  
- `204 No Content` on success  
- `404 Not Found` if order doesn't exist  
```json
{
  "id": 1,
  "quantity": 2,
  "productName": "pen"
}
```  