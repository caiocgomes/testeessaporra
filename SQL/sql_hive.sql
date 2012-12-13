CREATE EXTERNAL TABLE vehicle_ccr_cotia_sp2
(vehicle STRING)
STORED AS TEXTFILE
LOCATION 's3://maplink/vehicle_ccr_cotia2/';

INSERT OVERWRITE TABLE vehicle_ccr_cotia_sp2
select A.vehicle from speedsns A inner join dynamaps_cotia_sp B on A.dynamap = B.dynamap  
group by A.vehicle
;


select * from speedsns A inner join vehicle_ccr_cotia_sp2 B on A.vehicle = B.vehicle 



select * from speedsns A inner join vehicle_ccr_cotia_sp B on A.vehicle = B.vehicle 

CREATE EXTERNAL TABLE vehicles_passed_cotia_sp
(dynamap string,vehicle string,speed string,hour string,minute string)
STORED AS TEXTFILE
LOCATION 's3://maplink/vehicle_passed_cotia/';


INSERT OVERWRITE TABLE vehicles_passed_cotia_sp
select A.dynamap,A.vehicle,A.speed,A.hour,A.minute
from speedsns A inner join vehicle_ccr_cotia_sp B on A.vehicle = B.vehicle






# select the end point for the vehicle
select min(A.dynamap) from (select dynamap,vehicle,hour*60+minute as t from vehicles_passed_cotia_sp) A inner join 
minmax B 
on A.t = B.tmax and A.vehicle = B.vehicle group by A.vehicle;



