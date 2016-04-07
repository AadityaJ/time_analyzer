import sys
file='db_example_date_log.csv'
f=open(file)
cod=f.read()
file='dbs.sql'
h=open(file,'w')
sys.stdout=h 
i=0
cod=cod.split('\r')
for line in cod:
	if i==0:
		i=1
		continue
	else :
		lst=line.split(",")
		str="('"
		str+="', '".join(lst)
		str+="')"
		print "Insert into values",str
	
