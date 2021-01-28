#!/usr/bin/env python3

import os
import json
import secret
from http.cookies import SimpleCookie

#print system environment variables without environment variables added by cgi
'''Question 1
FROM: GeeksforGeeks
URL:https://www.geeksforgeeks.org/python-os-environ-object/
os.environ is a mapping object that represents the user's environment variables
return a dictionary having user's environmental varaible as key and their values as value
'''

#print("Content-Type: text/plain")
#print()
#print(os.environ)

#print("Content-Type: application/json")
#print()
#print(json.dumps(dict(os.environ), indent=2))

#query = os.environ["QUERY_STRING"]
#print("Content-Type: text/html")
#print()
#print(f"<p>{query}</p>")

