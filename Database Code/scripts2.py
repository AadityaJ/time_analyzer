import sys
import random
file='db_example_date_log.sql'
f=open(file,'w')
sys.stdout=f 
i=0
for inde in range(1006,1016):
	for i in range(1,21):
	    if i+6==9 or i+6==10 or i+6==16 or i+6==17 or i+6==23 or i+6==24:
	        continue
	    strng= "Insert into date_log values ('"+str(inde)+"','2016/04/"+str((i+6))+"','"+str(random.randint(5,13))+"');"
	    print strng
