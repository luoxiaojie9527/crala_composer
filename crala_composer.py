import os
from pymongo import MongoClient

nodes = []
packages = []
subs = []
pubs = []
_ids = []

client = MongoClient()
db = client.talker

cursor = db.talker.find({"node":"listener"})
for document in cursor:
	nodes.append(document["node"])
	packages.append(document["package"])
	subs.append(document["sub"])
	pubs.append(document["pub"])
	_ids.append(document["_id"])

for i in range(len(nodes)):
	cursor = db.talker.find({"sub":pubs[i]})
	for document in cursor:
		if document["_id"] not in _ids:
			nodes.append(document["node"])
			packages.append(document["package"])
			subs.append(document["sub"])
			pubs.append(document["pub"])
			_ids.append(document["_id"])

	cursor = db.talker.find({"pub":subs[i]})
	for document in cursor:
		if document["_id"] not in _ids:
			nodes.append(document["node"])
			packages.append(document["package"])
			subs.append(document["sub"])
			pubs.append(document["pub"])
			_ids.append(document["_id"])
for i in range(len(nodes)):
	cursor = db.talker.find({"sub":pubs[i]})
	for document in cursor:
		if document["_id"] not in _ids:
			nodes.append(document["node"])
			packages.append(document["package"])
			subs.append(document["sub"])
			pubs.append(document["pub"])
			_ids.append(document["_id"])

	cursor = db.talker.find({"pub":subs[i]})
	for document in cursor:
		if document["_id"] not in _ids:
			nodes.append(document["node"])
			packages.append(document["package"])
			subs.append(document["sub"])
			pubs.append(document["pub"])
			_ids.append(document["_id"])

print(str(len(nodes))+" nodes")

for j in nodes:
	print(j)

#os.system('roscore &')
#for i in range(len(nodes)):
#	os.system('rosrun'+' '+packages[i]+' '+nodes[i]+' &')


