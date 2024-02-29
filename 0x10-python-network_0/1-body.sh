#!/bin/bash
# Script that takes in a URL, sends a request to that URL, and displays the body of the response.
# Display only body of a 200 status code response

curl -sL "$1"