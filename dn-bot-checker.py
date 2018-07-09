import datetime
import urllib

domain_name = "williamfeumbah.com"

''' We check if the domain is available on name.com'''

#We open a connection and give our query
connection = urllib.urlopen("https://www.name.com/domain/search/"+domain_name)
output = connection.read()
print(output)
connection.close()

# We check wether the answer of our query
if "Your domain is available!" in output:
	print("The domain "+domain_name+" is available!")
else:
	print("The domain "+domain_name+" is not available!")



