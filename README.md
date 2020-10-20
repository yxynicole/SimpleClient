# SimpleClient
#### 5700CS_PJ1
## Approach
This client program intends to solve all mathematical expressions from a server.
Before the Q&A session starts, they need sockets to establish a connection between them. 
I divided this project into three parts and finished them one after another. 
The first part encompasses aspects of sockets. The second part focuses on parsing arguments from the command line. 
The third part is about integrating the first and the second part. 
### Socket and Connection
On the client-side, the steps involved in having a conversation are:
1. Create a socket
2. Connect to the server via the socket
	- The location of the server: 
		- host name 
		- Port: 27995 
3. Send and receive message 
	1. Client greets
		- Hello + ID 
	2. Client receives message
		- Checks keyword in the message 
	3. Client responses based on the keyword 
		- STATUS—> solve the question —>go back to step 2. (Loop)
		- BYE —> save the secret flag key—>hang up (no loop)
		-  No STATUS and BYE—> hang up (no loop) 	
### Command-Line Arguments
The client program needs to get data from the common line and put a specific meaning into the data,  such as IP address, port number, NEU ID, etc., so *argparse module* is used to parse command-line options and arguments.  
1. Create a parser 
2. Add arguments to the parser 
	- Positional arguments 
		- hostname
			neuID
	- Optional arguments 
		- -p, #default 27995 
			-s'-, #s->use an SSL encrypted #socket connection
			 
			
3. Parse arguments 
4. Pass parsed arguments to the socket 
### Miscellaneous
- Combine sending and receiving message into one function
- Solve math expressions by using eval() function
- Save the secrete flag
- Close socket
-  chmod +x client2
### Errors
- socket recv() takes at least one arguments
