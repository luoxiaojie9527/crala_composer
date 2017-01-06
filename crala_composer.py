#!/usr/bin/python  
# encoding=utf-8 
from pymongo import MongoClient
import threading
import subprocess
import os


#######################################################################################################################################
def find_nodes(nodes):
	flag = True
	while(flag):
		for i in range(len(nodes)):
			if pubs[i] <> "":
				cursor = db.nodes_collection.find({"sub":pubs[i]})
				for document in cursor:
					if document["_id"] not in _ids:
						nodes.append(document["node"])
						packages.append(document["package"])
						subs.append(document["sub"])
						pubs.append(document["pub"])
						_ids.append(document["_id"])
		
			if subs[i] <> "":
				cursor = db.nodes_collection.find({"pub":subs[i]})
				for document in cursor:
					if document["_id"] not in _ids:
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
	cursor = db.tasks.find({"task":task})
	for document in cursor:
		initial=document["node"]
	return initial
#####################################################################################################################################
def find_initial_node(initial):
	for i in range(len(initial)):
		cursor = db.nodes_collection.find({"node":initial[i]})
		for document in cursor:
			nodes.append(document["node"])
			packages.append(document["package"])
			subs.append(document["sub"])
			pubs.append(document["pub"])
			_ids.append(document["_id"])
	num.append(len(nodes))
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

	client = MongoClient()
	db = client.tasks
	initial=get_task("drawsquare_turtlesim")
	
	client = MongoClient()
	db = client.nodes_db
	find_initial_node(initial)
	find_nodes(nodes)

	print(str(len(nodes))+" nodes")

	for j in nodes:
		print(j)
	
	threads_run()
	
	print "all over"
################################################GAMEOVER####################################################################



	


