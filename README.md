# Wikipedia table filtering service

This microservice builds upon the [Wikipedia table scraping service](https://github.com/jaredtconnor/cs361-table-scraper) by adding functionality to filter a Wikipedia table returned from the initial service. 

Following API endpoints are exposed:

- `GET /filter` - Filters the returned Wikipedia table based on the number of top N rows to return (i.e. - The page for [https://en.wikipedia.org/wiki/100_metres](https://en.wikipedia.org/wiki/100_metres) would be the `100_metres` slug)

## Parameters: 

1) `/filter/slug`: (required) - Endpoint of the specific Wikipedia page that contains the tables to parse
2) `/filter/slug/table_num`: (required) - The index of the table to pull from the page
3)  `/filter/slug/table_num/top_n`: (required) - The top N rows to return of the table requested

## Example: 
API request - GET - `http://wikipedia-table-scraper.herokuapp.com/filter/C_(programming_language)/1/`

Returns: 
```
{
    Year:{ 
            0: 1972,
            1: 1978, 
            2: 1989, 
    }, 
    C Standard: { 
        0: Birth, 
        1: K&R C, 
        2: ANSI C and ISO C, 
    }
```

## Building and running

1) Install dependencies: 
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2) Run app: 
``` 
python app.py
```

## License
MIT