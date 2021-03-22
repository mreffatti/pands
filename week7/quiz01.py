with open("test-a.txt") as f:
 data = f.read()
 print (data)

 #If the file doesnt exist we will get an error: FileNotFoundError: [Errno 2] No such file or directory: 'test-a.txt'