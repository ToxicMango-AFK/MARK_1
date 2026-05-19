{{ config(
    materialized='table',
    unique_key='id'
) }}

with source as (
    select * from
{{ source('dev' , 'raw_weather_api')}}
),

de_dup as (
    select * , row_number() over( partition by local_time order by inserted_at) as rn
    from source
)

select
    id,
    city,
    country,
    temperature,
    weather_descriptions,
    sunrise,
    sunset,
    wind_speed,
    local_time as weather_time_local,
    (inserted_at + (utc_offset || 'hours')::interval) as inserted_at_local,
    inserted_at
from de_dup
where rn = 1
