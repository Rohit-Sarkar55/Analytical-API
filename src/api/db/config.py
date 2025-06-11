#pip install python-decouple

from decouple import config as decouple_config


# DATABASE_URL= decouple_config("DATABASE_URL",default="")
DATABASE_URL="postgresql+psycopg://time-user:time-pw@db_service:5432/timescaledb"
DB_TIMEZONE = decouple_config("DB_TIMEZONE", default="UTC")
