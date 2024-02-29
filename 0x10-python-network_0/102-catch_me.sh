#!/bin/bash
# Make a PUT request to 0.0.0.0:5000/catch_me with curl, sending the request data as a POST request
curl -sX PUT 0.0.0.0:5000/catch_me --data "user_id=98" -H "Origin: HolbertonSchool" --referer "You got me!"
