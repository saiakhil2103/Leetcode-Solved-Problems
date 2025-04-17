-- Day and Cancellation Rate 

select 
request_at as Day,
round(
    sum(status != 'completed') / count(*),
    2
) as 'Cancellation Rate'
from Trips 
left join Users as Clients on Trips.client_id = Clients.users_id 
left join Users as Drivers on Trips.driver_id = Drivers.users_id 
where 
Clients.banned = 'No'
and Drivers.banned = 'No'
and request_at between '2013-10-01' and '2013-10-03'
group by Day;