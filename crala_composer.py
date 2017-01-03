import os
from pymongo import MongoClient

nodes = []
packages = []
subs = []
pubs = []

client = MongoClient()
db = client.talker

cursor = db.talker.find({"node":"talker"})
for document in cursor:
	nodes.append(document["node"])
	packages.append(document["package"])
	subs.append(document["sub"])
	pubs.append(document["pub"])
i=0
for i in range(len(nodes)):
	cursor = db.talker.find({"sub":pubs[i]})
	for document in cursor:
		nodes.append(document["node"])
		packages.append(document["package"])
		subs.append(document["sub"])
		pubs.append(document["pub"])
for j in nodes:
	print(j)

#os.system('roscore &')
#for i in range(len(nodes)):
#	os.system('rosrun'+' '+packages[i]+' '+nodes[i]+' &')


