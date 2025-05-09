# Batch ETL PySpark Pipeline (Databricks-style)

This is a production-grade local PySpark ETL project built in VS Code with:

- ✅ Local Spark + Jupyter Notebooks
- ✅ Airflow DAG orchestration
- ✅ CI/CD with GitHub Actions
- ✅ Logging, unit tests, `.env` secrets
- ✅ Windows Task Scheduler support

## Quickstart

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python main.py
