from api_request import mock_data,fetch_data
import psycopg2

def connect_to_db():
    print("connecting to postgres")
    try:
        conn = psycopg2.connect(
            host = "db",
            port = 5432,
            dbname = "db",
            user = "db_user",
            password = "db_password"
        )
        print(conn)
        return conn
    except psycopg2.Error as e:
        print(f"connection failed due to {e}")
        raise


def table_create(conn):
    try:
        print("creating table in postgress...")
        cursor = conn.cursor()
        cursor.execute("""
        CREATE SCHEMA IF NOT EXISTS DEV;
        CREATE TABLE IF NOT EXISTS DEV.RAW_WEATHER_API (
        id SERIAL PRIMARY KEY,
        city TEXT,
        country TEXT,
        temperature Float,
        local_time TIMESTAMP,
        latitude FLOAT,
        longitude FLOAT,
        weather_descriptions TEXT,
        sunrise TIME,
        sunset TIME,
        wind_speed FLOAT,
        utc_offset TEXT,
        inserted_at TIMESTAMP default now()
        );
        """)
        conn.commit()
        print("table was created.")

    except psycopg2.Error as e:
        print (f"error occured while table creation {e}")
        raise


def insert_data(conn,data):
    try:
        print("inserting data in raw_weather_api table...")
        location = data["location"]
        current = data['current']
        astro = data["current"]["astro"]
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO DEV.RAW_WEATHER_API (
            city,
            country,
            temperature,
            local_time,
            latitude,
            longitude,
            weather_descriptions,
            sunrise,
            sunset,
            wind_speed,
            utc_offset,
            inserted_at
        ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,now())
        """,(
            location['name'],
            location['country'],
            current['temperature'],
            location['localtime'],
            location['lat'],
            location['lon'],
            current['weather_descriptions'],
            astro['sunrise'],
            astro['sunset'],
            current['wind_speed'],
            location['utc_offset']
        ))
        conn.commit()
        print("records are inserted successfully.")
    
    except psycopg2.Error as e:
        print(f"data load failed due to {e}")
        raise

def main():
    try:
        data = fetch_data()
        #data = mock_data()
        conn = connect_to_db()
        table_create(conn)
        insert_data(conn,data)

    except Exception as e:
        print(f"Execution failed due to {e}")
    
    finally:
        if "conn" in locals():
            conn.close()
            print("database connection closed")

