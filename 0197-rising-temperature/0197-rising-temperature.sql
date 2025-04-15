-- select w1.id 
-- from Weather w1
-- join Weather w2
-- on datediff(w1.recordDate, w2.recordDate)=1
-- where w1.temperature > w2.temperature;

with PreviousWeatherData as 
(
    select 
        id,
        recordDate,
        temperature,
        lag(temperature, 1) over (order by recordDate) as previousTemp,
        lag(recordDate, 1) over (order by recordDate) as previousDate
    from Weather
)
select id from PreviousWeatherData
where temperature > previousTemp
and recordDate = date_add(previousDate, interval 1 day);