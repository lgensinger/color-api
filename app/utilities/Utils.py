"""General utility for rest service"""

from flask import request
from random import randint, uniform

##########################
# DUMMY cert authentication
##########################
class AuthenticationError(Exception):
    pass

def authenticate(request):
    """
    Authenticates user using SSL certificate. 
    Raises AuthenticationError on invalid user or invalid request.
    """
    
    header_data = {
        "host": request.headers.get("Host"),
        "ssl_verified": request.headers.get("X-SSL-Verified"),
        "ssl_dn": request.headers.get("X-SSL-DN"),
        "ssl_client": request.headers.get("X-SSL-Client-Cert")
    }
    
    # TODO SOMETHING TO AUTHENTICATE?
    if 1 > 0:
        # dunno what is available to return but ideally some sort of unique id or 
        # key we can use to fetch data from other sources 
        # (like use the key to get user-roles from a specified db for example)
        # the name is used here for simplicity and legibility throughout backend app/redis data
        return { "uid": "analyst" }
    
    else:
        
        AuthenticationError
        
##########################
# WORKSPACE functions - valid - need
##########################
def docs(redis_key):
    """
    Fetches all layout redis objects of a specified type.
    """
    
    # set up redis object
    r = Redis(configuration.REDIS_URI)
    
    # get keys
    keys = r.keys(redis_key)

    docs = []

    # loop through keys
    for key in keys:
        
        # convert bytes to dict
        doc = json.loads(r.get(key).decode())
        
        # add to list
        docs.append(doc)
        
    return docs

def pagination(doc_count, offset=None, limit=None):
    """
    Determines document pagination values through a document set.
    """
    
    l = limit if limit != None else doc_count
    o = offset if offset != None else 0
    
    # difference between what was asked for and what is available
    request_difference = doc_count - l + o if limit != None and offset != None and offset != 0 else doc_count if limit != doc_count else limit
    
    # determine true result
    request_count = request_difference if request_difference > -1 else doc_count 
    
    # determine if more content available
    more_to_load = True if doc_count - o - l > 0 else False
    
    return { "more": more_to_load, "count": request_count, "offset": o, "limit": l }

##########################
# DUMMY CONTENT
##########################