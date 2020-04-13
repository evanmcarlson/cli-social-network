# cli-social-network

The purpose of this repository was to gain experience parsing and storing data structures in files. It is a very simple implementation of a social network, with the information about users (including usernames and passwords) stored in a text file. This is obviously not a practical approach to coding a social network, but is sufficent for command line application to demonstrate array parsing and writing to files in python.

### getting started
To get started, download the repository and navigate to folder's working directory. Open a terminal and enter `python socialNetwork.py` to run the program.

### file structure
network.txt is a list of social network users seperted by a newline character. Each line is a list containing a username, password & two nested lists (statuses and friends). Lines are made up of comma seperated values in the following format:
`username, password, messages, message 1, ... message n, friends, friend 1, ... friend n,`
Note that "messages" and "friends" are string literals and are used to determine where their respective data begins in the network representation.

socialnetwork.py is the main file and executable program.

person.py is essentially a node in the social network representation containing parsed values from one line of the input file.
