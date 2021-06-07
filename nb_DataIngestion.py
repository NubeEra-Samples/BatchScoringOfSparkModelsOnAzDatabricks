# Databricks notebook source
import socket
socket.setdefaulttimeout(90)

import glob
import os
import pandas as pd

import urllib
from datetime import datetime
from pyspark.sql import SparkSession

# COMMAND ----------

basedataurl="https://raw.githubusercontent.com/DeeptiChevvuri/Predictive-Maintenance-Modelling-Datasets/master/"

MACH_DATA='machines_data'
MAINT_DATA='maint_data'
ERROR_DATA='errors_data'
TELEMETRY_DATA='telemetry_data'
FAILURE_DATA='failures_data'

# COMMAND ----------

datafile="machines.csv"
url=basedataurl+datafile

if not os.path.isfile(datafile):
  urllib.request.urlretrieve(url,datafile)
  print("File Downloaded")
else:
  print("File Exists no need for download")

# COMMAND ----------

machines=pd.read_csv(datafile)

# COMMAND ----------

machines

# COMMAND ----------


