##### As the title states.
FROM Linux Basics for Hackers:

Let's create a network connection in Python using the socket module. 
This is useful in a type of hacking exploit called banner grabbing. Applications present a banner when someone or something connects to it. Its like a greeting announcing what it is. Hackers use banner grabbing to find out crucial information about what application or service is running on a port. 

- `#!/usr/bin/python3` #We declare that we want the script to run with the Python interpreter

- `import socket` #we import the socket module so we can use its networking capabilities to open a connection over the network for us. A socket provides a way for two computers to communicate over the network.`
- `s = socket.socket()` #create a new object named 's' from the socket class in the socket module. this new object can perform actions such as connecting a reading data
- `s.connect(("127.0.0.1", 22))` #use the `connect` method from the socket module to make a network connection to the localhost IP and SSH port.
- `answer = s.recv(1024)` #use the receive method (`recv`) to read 1024 bytes of data from the socket and store them in a variable named `answer`, these 1024 bytes will contain the banner information. 
- `print(answer)` # print the contents of that variable to the screen with the `print()` function to see what data has been passed over the socket, allowing us to spy on it!
- `s.close()` #close the connection

Save this script as HackersAriseSSHBannerGrab.py and then change its permissions using the `chmod` command so that you can execute it.
Lets use this script to connect to another linux system on port 22. If SSH is running on that port we should be able to read the banner into our `answer` variable and print it to the screen.
We have just created a simple banner-grabbing Python script! We can use this script to find out what application, version and operating system are running at that IP address and port. This gives us key information that a hacker needs before attacking any system. This is essentially what shodan.io does for nearly every IP address on the planet and it catalogs and indexes this information for us to search.

We just created a TCP client that can make a connection to another TCP/ IP address and port and then spy on the information being transmitted. That socket can also be used to create a TCP listener, to listen to connections from outsiders to your server. Let's try doing that next.
 In the Python script below you'll create a socket on any port in your system that when someone connects to that socket, collects key information about the connectors system.
 Enter the script and save it as tcp_server.py. Make sure to give yourself permissions with `chmod`.
 
 - `#!/usr/bin/python3` #We declare that we want the script to run with the Python interpreter
 
 - `import socket` #we import the socket module as before so we can use its capabilities
 
 - `TCP_IP = "192.168.181.190"` #define a variable to hold the IP address
 - `TCP_PORT = 6996` #define a variable to hold the port number
 - `BUFFER_SIZE = 100` #define a variable to hold the buffer size of the data we are capturing from the connected system
 
 - `s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)` #define the socket
 - `s.bind((TCP_IP, TCP_PORT))` #bind the socket to the IP address and port using the variables created above
 - `s.listen(1)` #tell the socket to listen using the listen() method from the socket library
 
 - `conn, addr = s.accept()` #capture IP address and port of the connecting system using the socket library's accept() method
 - `print('Connection address: ', addr )` #print the information captured above to the screen
 
 - `while True:`
  
     `data=conn.recv(BUFFER_SIZE)` #put data from the connecting system into a buffer
     `if not data:`
       `break`
     `print("Received data: ", data)` #print said data
     `conn.send(data) #echo`
   
   `conn.close()` #close the connection
 
 
 
 
 
 
 
 
 
