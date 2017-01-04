#!/usr/bin/python  
# encoding=utf-8 
from pymongo import MongoClient
import threading
import subprocess
import os

nodes = []
packages = []
subs = []
pubs = []
_ids = []
num = []
flag=1


client = MongoClient()
db = client.tasks
cursor = db.tasks.find({"task":"drawsquare_turtlesim"})
for document in cursor:
	initial = document["node"]

db = client.talker

cursor = db.talker.find({"node":initial})
for document in cursor:
	nodes.append(document["node"])
	packages.append(document["package"])
	subs.append(document["sub"])
	pubs.append(document["pub"])
	_ids.append(document["_id"])
num.append(len(nodes))

while(flag):
	for i in range(len(nodes)):
		if pubs[i] <> "":
			print(pubs[i])
			cursor = db.talker.find({"sub":pubs[i]})
			for document in cursor:
				if document["_id"] not in _ids:
					nodes.append(document["node"])
					packages.append(document["package"])
					subs.append(document["sub"])
					pubs.append(document["pub"])
					_ids.append(document["_id"])
		if subs[i] <> "":
			cursor = db.talker.find({"pub":subs[i]})
			for document in cursor:
				if document["_id"] not in _ids:
					nodes.append(document["node"])
					packages.append(document["package"])
					subs.append(document["sub"])
					pubs.append(document["pub"])
					_ids.append(document["_id"])

	num.append(len(nodes))
	print(num[-1])
	if num[-1]!=num[len(num)-2]:
		flag=1
	else:
		flag=0
	

print(str(len(nodes))+" nodes")

for j in nodes:
	print(j)


threads = []
threads.append(threading.Thread(target=subprocess.Popen(('roscore &'),shell=True)))
for i in range(len(nodes)):
	#threads.append(threading.Thread(target=os.system("ls")))
	threads.append(threading.Thread(target=subprocess.Popen(("rosrun"+" "+packages[i]+" "+nodes[i]+" &"),shell=True)))
os.system("rosrun rqt_graph rqt_graph")
if __name__ == '__main__':
	for t in threads:
	    t.setDaemon(True)
	    t.start()
	t.join()
	
	print "all over"




	


