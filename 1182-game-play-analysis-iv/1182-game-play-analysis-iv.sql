with first_login as (
    select player_id, min(event_date) as first_date
    from activity
    group by player_id
), 
second_login as (
    select a.player_id
    from activity a 
    inner join first_login f
    on a.player_id = f.player_id and a.event_date = date_add(f.first_date, interval 1 day)
)
select round(count(distinct s.player_id) / count(distinct f.player_id), 2) as fraction
from first_login f
left join second_login s 
on f.player_id = s.player_id;