import csv
import pandas as pd
from sqlalchemy import create_engine

# constants
from constants.server_keys import mysqlServer
from constants.scraping_keywords import scraping_keywords

engine_path = "mysql://{username}:{password}@{host}/{db_name}"

keys_template = {
    "username": mysqlServer.username,
    "password": mysqlServer.password,
    "host": mysqlServer.host,
    "db_name": mysqlServer.database,
}

engine = create_engine(
    engine_path.format(**keys_template)
)  # enter your password and database names here

keyword_cols = list(scraping_keywords)

cols = ["course_name", "lecturer"]

cols += keyword_cols

df = pd.read_csv(
    "scraper_data.csv",
    sep=",",
    quotechar='"',
    header=None,
    names=cols,
)  # Replace Excel_file_name with your excel sheet name
df.to_sql(
    "cs", con=engine, index=False, if_exists="append"
)  # Replace Table_name with your sql table name
