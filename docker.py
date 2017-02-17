#!/usr/bin/python
import commands

print "enter no. of datanodes and tasktrackers"
x=raw_input()
print "stay calm,it will take a while"
#to stop and remove existing containers
commands.getstatusoutput("docker stop $(docker ps -a)")
commands.getstatusoutput("docker rm $(docker ps -a)")


#for namenode
print commands.getstatusoutput("docker run -itd --name mynamenode docker2")[1]
print commands.getstatusoutput("docker exec mynamenode hostname -i")

#print commands.getstatusoutput("docker exec mynamenode cat /etc/hadoop/core-site.xml")
print commands.getstatusoutput("docker cp /root/Desktop/nn/hdfs-site.xml mynamenode:/etc/hadoop/")[1]
#print commands.getstatusoutput("docker exec mynamenode cat /etc/hadoop/hdfs-site.xml")

print commands.getstatusoutput("docker exec mynamenode service sshd start")[1]
print commands.getstatusoutput("docker exec mynamenode hadoop namenode -format")
print commands.getstatusoutput("docker exec mynamenode hadoop-daemon.sh start namenode")[1]
#for jobtracker
print commands.getstatusoutput("docker run -itd --name myjobtracker docker2")[1]
print commands.getstatusoutput("docker exec myjobtracker hostname -i")
print commands.getstatusoutput("docker exec myjobtracker service sshd start")[1]
print commands.getstatusoutput("docker exec myjobtracker hadoop-daemon.sh start jobtracker")[1]

y=int(x)
i=0
#for datanode and tasktracker
while i<y:
	f=i+1
	
	print f
	print commands.getstatusoutput("docker run -itd --name dn_tt"+(str(f))+" docker2")[1]
	print commands.getstatusoutput("docker cp /root/Desktop/dn/hdfs-site.xml dn_tt"+(str(f))+":/etc/hadoop/")[1]
	print commands.getstatusoutput("docker exec dn_tt"+(str(f))+" hadoop-daemon.sh start datanode")[1]
	print commands.getstatusoutput("docker exec dn_tt"+(str(f))+" hadoop-daemon.sh start tasktracker")[1]
	print commands.getstatusoutput(" docker exec dn_tt"+(str(f))+" /usr/java/jdk1.7.0_79/bin/jps")
	i=i+1

print commands.getstatusoutput(" docker exec mynamenode /usr/java/jdk1.7.0_79/bin/jps")
print "namenode is started at ip 172.17.0.2"
print commands.getstatusoutput(" docker exec myjobtracker /usr/java/jdk1.7.0_79/bin/jps")
print "jobtracker is started at ip 172.17.0.3"
print commands.getstatusoutput("docker exec mynamenode hadoop dfsadmin -report")
print "YOUR HADOOP CLUSTER IS READY TO USE"
#print "&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&"
#print commands.getstatusoutput(" docker exec myjobtracker hadoop job -list-active-trackers")
#print ta[0]
#print ta[1]

	

#tc=commands.getstatusoutput("docker exec namenode hadoop job -list-activetrackers")
#print tc[0]
#print tc[1]
#tb=commands.getstatusoutput("docker exec namenode hadoop dfsadmin -report")
#print tb[0]
#print tb[1]

	
