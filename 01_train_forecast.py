# Databricks notebook source
dbutils.widgets.text("catalog", "ang_nara_catalog") 
dbutils.widgets.text("database", "MOH")
dbutils.widgets.text("volume_storage", "MOH")

# COMMAND ----------

forecast_volume = (dbutils.widgets.get("catalog") + 
                    "." + dbutils.widgets.get("database") +
                    "." + dbutils.widgets.get("volume_storage"))

forecast_volume_output = ( "/Volumes/" + 
                     dbutils.widgets.get("catalog") +
                     "/" + dbutils.widgets.get("database") +
                     "/" + dbutils.widgets.get("volume_storage") )


# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE CATALOG IF NOT EXISTS ${catalog};
# MAGIC USE CATALOG ${catalog};
# MAGIC CREATE DATABASE IF NOT EXISTS ${database};
# MAGIC USE ${database};
# MAGIC CREATE VOLUME IF NOT EXISTS ${forecast_volume};

# COMMAND ----------


