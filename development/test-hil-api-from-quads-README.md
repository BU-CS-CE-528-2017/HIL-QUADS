Minimally exteneded the quads cli to be able to use the HIL API.
Currently implemented to only allow 'GET' requests, but could be
easily configured to allow more. This was just meant to be a very
simple demonstration of how the HIL RESTful API can be accessed by
another application, and could be a good starting off point when
attempting to connect the QUADS application to HIL at a much deeper
level.

In order to run, haas server should be running locally, on port 5000.
The add_switches script can be used to add a sample data set of switches.
Then the GET /switches API call can be tested from QUADS. (Note: this extension
to quads.py can be used to make any HIL api GET request - just using switches
here as an example).

Directions:

1) Copy replace quads/bin/quads.py with the quads.py from this directory, and add add_switches.sh to your hil directory

    $ cp HIL-QUADS/development/quads.py your/path/to/quads/bin/quads.py
    $ cp HIL-QUADS/development/add_switches.sh your/path/to/hil/

2) From the hil directory, start the haas server

    $ cd your/path/to/hil
    $ virtualenv .venv
    $ source .venv/bin/activate
    $ pip install -e .
    $ haas serve 5000

3) From a new terminal, add some objects to HIL so quads can request info about them

    $ cd your/path/to/hil
    $ source .venv/bin/activate
    $ pip install -e .
    $ ./add_switches.sh

4) From a new terminal, in your quads directory, run bin/quads.py with the new hil api command line options
(This uses the requests library (you might have to pip install requests) to open a connection with the haas server
and request data info using the hil REST api)

    $ cd your/path/to/quads/
    $ bin/quads.py --hil-api-action GET --hil-api-call /switches

5) If this does not work, complain to @saacg on slack about his poorly written directions
