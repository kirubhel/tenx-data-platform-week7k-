from dagster import job, op
import subprocess

@op
def scrape_telegram():
    subprocess.run(["python", "scripts/scrape_telegram.py"], check=True)

@op
def scrape_images():
    subprocess.run(["python", "scripts/scrape_images.py"], check=True)

@op
def run_yolo():
    subprocess.run(["python", "scripts/run_yolo.py"], check=True)

@op
def load_to_postgres():
    subprocess.run(["python", "scripts/load_to_postgres.py"], check=True)

@op
def run_dbt():
    subprocess.run(["dbt", "run"], cwd="dbt_project", check=True)

@job
def full_pipeline():
    scrape_telegram()
    scrape_images()
    run_yolo()
    load_to_postgres()
    run_dbt()
