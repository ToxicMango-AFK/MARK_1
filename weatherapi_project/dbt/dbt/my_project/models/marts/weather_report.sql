{{ config(
    materialized='table',
    unique_key='id'
) }}


select
    city,
    country,
    temperature,
    weather_descriptions,
    sunrise,
    sunset,
    wind_speed,
    weather_time_local
    from
{{ ref('stg_weather_data')}}
