# AutoMoto
Python code for API tests.

This is very simple example of the requests Python library usage. I've fetched AutoHero webpage requests through the browser's developer tools and prepared few api requests. 

Despite I do not needed any cookies for authentication (security issue?) I've decided to pass them to my session object with the first request (getPage).
Filter and sort operations are both send via single payload (operationsPayload).
iterate_API method will ensure if data are sorted/filtered properly.

# Running the script
To run this code simply open terminal window, switch to the directory with file and execute following command:

python Automation_API_approach.py // py Automation_API_approach.py

Alternativelly execute attached batch file.
