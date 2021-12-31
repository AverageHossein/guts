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

Body:

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
GET /api/theater/<theaterId>

Url Param:
  theaterId: int
```

Get all Theaters with Pagination: 

```
GET /api/theater?page=1&per_page=10

Query Strings: 
  page
  per_page
```

Allocate theater seats with users:

```
POSt /api/theater/allocate

Body:

{
    "theater_id": 1,
    "groups": [
        {
            "section_id": 1,
            "group_rank": 1,
            "user_ids": [4, 2, 6]
        },
        {
            "group_rank": 2,
            "user_ids": [11, 12, 66]
        },
        
    ]
}

"section_id" is not required, if you provide "section_id" in a group means someone from that group has a preference to be in a specific section.

```

Get seat number by user Id:

```
GET /api/theater/seat/user/<userId>

Url Param:
  userId: int

```
