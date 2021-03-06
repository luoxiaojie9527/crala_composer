#!/usr/bin/python  
# encoding=utf-8 
from pymongo import MongoClient
import threading
import subprocess
import os
import json


#######################################################################################################################################
def find_nodes(nodes):
	flag = True
	while(flag):
		for i in range(len(nodes)):
			if pubs[0] and pubs[i]:
				cursor = db.nodes_collection.find_one({"sub":pubs[i]})
#				for document in cursor:
				if cursor:
					document = cursor
					if document["_id"] not in _ids and document["sub"] not in subs and document["pub"] not in pubs:
						nodes.append(document["node"])
						packages.append(document["package"])
						subs.append(document["sub"])
						pubs.append(document["pub"])
						_ids.append(document["_id"])
		
			if subs[0] and subs[i]:
				cursor = db.nodes_collection.find_one({"pub":subs[i]})
#				for document in cursor:
				if cursor:
					document = cursor
					if document["_id"] not in _ids and document["sub"] not in subs and document["pub"] not in pubs:
						nodes.append(document["node"])
						packages.append(document["package"])
						subs.append(document["sub"])
						pubs.append(document["pub"])
						_ids.append(document["_id"])
		num.append(len(nodes))
		if num[-1]!=num[len(num)-2]:
			flag=True
		else:
			flag=False

#####################################################################################################################################
def get_task(task):
	cursor = db.tasks.find_one({"task":task})
#	for document in cursor:
	document = cursor
	initial=document["node"]
	return initial
#####################################################################################################################################
def find_initial_node(initial):
	for i in range(len(initial)):
		cursor = db.nodes_collection.find_one({"node":initial[i]})
#		for document in cursor:
		if cursor:
			document = cursor
			nodes.append(document["node"])
			packages.append(document["package"])
			subs.append(document["sub"])
			pubs.append(document["pub"])
			_ids.append(document["_id"])
	num.append(len(nodes))
	print(num[-1])

#####################################################################################################################################


	
#####################################################################################################################################
def threads_run():
	threads = []
	threads.append(threading.Thread(target=subprocess.Popen(('roscore '),shell=True)))
	for i in range(len(nodes)):
		threads.append(threading.Thread(target=subprocess.Popen(("rosrun"+" "+packages[i]+" "+nodes[i]+" "),shell=True)))
	
	for t in threads:
		t.setDaemon(True)
		t.start()
	os.system("rosrun rqt_graph rqt_graph")
	t.join()
#####################################################################################################################################	

if __name__ == '__main__':
	nodes = []
	packages = []
	subs = []
	pubs = []
	_ids = []
	num = []
        tasklist = []
       
	client = MongoClient()
	db = client.tasks
        taskcollection = db.tasks.find()
        for i in taskcollection:
            tasklist.append(i["task"])
        tasklist = json.dumps(tasklist)
        print(tasklist)
            
        task = raw_input("Please input the task in the following list : \n")
        print(task)
	initial = get_task(task)
	print(initial)

	client = MongoClient()
	db = client.nodes_db
	find_initial_node(initial)
	print(nodes)

	find_nodes(nodes)
	print(nodes)

	print(str(len(nodes)) + " nodes")

	for j in nodes:
		print(j)

	threads_run()
        os.system("pkill roscore")

	print "all over"
################################################GAME OVER############################################################################



	


