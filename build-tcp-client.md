##### As the title states.
FROM Linux Basics for Hackers:

Let's create a network connection in Python using the socket module. 
This is useful in a type of hacking exploit called banner grabbing. Applications present a banner when someone or something connects to it. Its like a greeting announcing what it is. Hackers use banner grabbing to find out crucial information about what application or service is running on a port. 
First we import the socket module so we can use its functions and tools. Here we are going to use the networking tools from the socket module to take care of interfacing a connection over the network for us. A socket provides a way for two computer nodes to communicate with each other.
Usually one is a server and one is a client.
Then we create a new object named `s`, instantiated from the `socket` class from the socket module. This way we can now use this object to perform other actions such as connecting and reading data.
We then use the `connect` method from the socket module to make a network connection to a special IP and port. Remember that methods are functions that are available for a particular object. The syntax is `object.method`. EG `socket.connect`. In this cabe I'm connecting to IP address 127.0.0.1 which is the IP address pointing back to localhost, the same machine this script is running on and port 22 which is the default SSH port. 
Then we use the receive method (`recv`) to read 1024 bytes of date from the socket and store them in a variable named `answer`, these 1024 bytes will contain the banner information. Then we print the contents of that variable to the screen with the `print()` function to see what data has been passed over the socket, allowing us to spy on it! On the final line we close the connection.

- `#!/usr/bin/python3`
- `import socket`
- `s = socket.socket()`
- `s.connect(("127.0.0.1", 22))`
- `answer = s.recv(1024)`
- `print(answer)`
- `s.close()`

Save this script as HackersAriseSSHBannerGrab.py and then change its permissions using the `chmod` command so that you can execute it.
Lets use this script to connect to another linux system on port 22. If SSH is running on that port we should be able to read the banner into our `answer` variable and print it to the screen.
We have just created a simple banner-grabbing Python script! We can use this script to find out what application, version and operating system are running at that IP address and port. This gives us key information that a hacker needs before attacking any system. This is essentially what shodan.io does for nearly every IP address on the planet and it catalogs and indexes this information for us to search.

We just created a TCP client that can make a connection to another TCP/ IP address and port and then spy on the information being transmitted. That socket can also be used to create a TCP listener, to listen to connections from outsiders to your server. Let's try doing that next.
 In the Python script below you'll create a socket on any port in your system that when someone connects to that socket, collects key information about the connectors system.
 Enter the script and save it as tcp_server.py. Make sure to give yourself permissions with `chmod`.
 
 - `#!/usr/bin/python3`
 
 - `import socket`
 
 - `TCP_IP = "192.168.181.190"`
 - `TCP_PORT = 6996`
 - `BUFFER_SIZE = 100`
 
 - `s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)`
 - `s.bind((TCP_IP, TCP_PORT))`
 - `s.listen(1)`
 
 - `conn, addr = s.accept()`
 - `print('Connection address: ', addr )`
 
 - `while True:`
  
     `data=conn.recv(BUFFER_SIZE)`
     `if not data:`
       `break`
     `print("Received data: ", data)`
     `conn.send(data) #echo`
   
   `conn.close()`
 
 
 
 
 
 
 
 
 
