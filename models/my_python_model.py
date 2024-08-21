import pandas as pd
import numpy as np

def model(dbt, session):
    dbt.config(materialized="table")

    return session.sql("selet 'hello' as message")
