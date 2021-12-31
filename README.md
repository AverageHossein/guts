# How To Run This?

I have dockerized the project, you can simply run the project by the command below: 

```
docker-compose up -d
```

P.S: Make sure that you don't have any other apps listening on ports <code>5432</code> and <code>8000</code>

# API Documentation 

Check models and schemas, the data structure, API validations, references and relations are pretty much clear there. here we cover the endpoints with sample.

Create a Section:

```
POST /api/theater/section

Body:

{"name": "Tail Seats"}

```

Get all sections with pagination:

```
GET /api/theater/section?page=1&per_page=10

Query Strings: 
  page
  per_page
```

Create a theater: 

```
POST /api/theater

{
    "name": "Berlin Opera Hall",
    "seats": [
        {
            "section_id": 1,
            "rank": 1,
            "row_number": 1,
            "seat_number": 1
        },
        {
            "section_id": 1,
            "rank": 2,
            "row_number": 1,
            "seat_number": 2
        },
        {
            "section_id": 1,
            "rank": 3,
            "row_number": 1,
            "seat_number": 3
        },
        {
            "section_id": 1,
            "rank": 4,
            "row_number": 1,
            "seat_number": 4
        },
        {
            "section_id": 1,
            "rank": 5,
            "row_number": 1,
            "seat_number": 5
        },
        {
            "section_id": 1,
            "rank": 6,
            "row_number": 2,
            "seat_number": 6
        },
        {
            "section_id": 1,
            "rank": 7,
            "row_number": 2,
            "seat_number": 7
        },
        {
            "section_id": 1,
            "rank": 8,
            "row_number": 2,
            "seat_number": 8
        },
        {
            "section_id": 1,
            "rank": 9,
            "row_number": 2,
            "seat_number": 9
        },
        {
            "section_id": 1,
            "rank": 10,
            "row_number": 2,
            "seat_number": 10
        }
    ]
}

```

Get one theater with Id:

```
GET /api/theater/<theater Id>
```

Get all Theaters with Pagination: 

```
GET /api/theater?page=1&per_page=10
```

