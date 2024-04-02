# Databricks notebook source
# MAGIC %md
# MAGIC Register Model to Unity Catalog 

# COMMAND ----------

import mlflow
catalog = "ang_nara_catalog"
schema = "moh"
model_name = "moh_forecast_2024"
mlflow.set_registry_uri("databricks-uc")
mlflow.register_model(
    model_uri="runs:/097ef40c803e4268b95dd97a8311224e/model",
    name=f"{catalog}.{schema}.{model_name}"
)

# COMMAND ----------


