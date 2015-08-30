# search-api
An API for fetching results in JSON format from search engines.

### Related project
[py-web-search](https://github.com/rohithpr/py-web-search)

### Base URL

`http://search-api.herokuapp.com/`

### Endpoints

1. Search: `/search`
2. News: `/news`

### Arguments

1. Query: q (required)
2. Num: num (default - 10)
3. Start: start (default - 0)
4. Recent: recent (default - None)
5. Search Engine: engine (default - randomly selects one)

### Examples

`http://search-api.herokuapp.com/search?q=hello&num=1&engine=bing`  
`http://search-api.herokuapp.com/news?q=hello&recent=h&start=100`

### Data returned

See [py-web-search](https://github.com/rohithpr/py-web-search#usage) for details on the data returned

Additional fields:  
`result['error']`: True if there has been any error, False if success

#### NOTE: There is a random delay of 3-10 seconds, when there is no error, to prevent making too many requests which may result in the service being blocked.
