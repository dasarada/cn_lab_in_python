import xmlrpclib
proxy = xmlrpclib.ServerProxy("http://localhost:8000/")
k=input("enter number:")
if k%2==0:
	ans="even"
else:
	ans="odd"
print str(k)+" is "+ans
