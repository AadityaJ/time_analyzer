select emp_id,sum(hours_worked) as tot_hours,Experience,type_id 
from date_log natural join Employee 
group by emp_id;