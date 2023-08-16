{{ NAME }} Route Design Recipe


1. Design the Route Signature
Include the HTTP method, the path, and any query or body parameters.

```
POST /ALBUMS
  title: string
  release_year: number (str)
  artist_id (str)
  GET /albums
```

2. Create Examples as Tests
Go through each route and write down one or more example responses.

Remember to try out different parameter values.

Include the status code and the response body.


```python
# Scenario 1

    #POST /albums 
    # title: "Blue Sky"
    # release_year: 2017
    # artist_id: 1
    # Expected Response (200 OK)

    """
    """ (no content)

    # GET /albums
    # Expected Response (200 OK)
    """
    Album(1, Diamond, 2017, 1)
    Album(2, Blue Sky, 2017, 1)
    """


# Scenario 2

    #POST /albums 
    # Expected Response (400 Bad request)

    """
    You need to submit a title, release_year, and artist_id
    """

    # GET /albums
    # Expected Response (200 OK)
    
    """
    Album(1, Diamond, 2017, 1)
    """
    
```




3. Test-drive the Route
After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.

Here's an example for you to start with:

"""
GET /home
  Expected response (200 OK):
  "This is my home page!"
"""
def test_get_home(web_client):
    response = web_client.get('/home')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'This is my home page!'

"""
POST /submit
  Parameters:
    name: Leo
    message: Hello world
  Expected response (200 OK):
  "Thanks Leo, you sent this message: "Hello world""
"""
def test_post_submit(web_client):
    response = web_client.post('/submit', data={'name': 'Leo', 'message': 'Hello world'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Thanks Leo, you sent this message: "Hello world"'