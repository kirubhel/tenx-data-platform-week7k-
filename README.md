
# 🚀 Tenx Data Platform (Week 7)

This repository implements an end-to-end data platform that extracts, transforms, enriches, and serves data collected from public Telegram channels related to Ethiopian medical products.

## 📦 Overview

**Goal**: Generate insights like top-mentioned drugs, product availability, and posting trends using a modern data pipeline.

**Stack**:
- Telethon (Telegram Scraping)
- PostgreSQL (Data Warehouse)
- dbt (Transformations & Star Schema)
- YOLOv8 (Image Enrichment)
- FastAPI (Analytical API)
- Dagster (Orchestration)
- Docker (Environment Management)

---

## 🧩 Folder Structure

```
├── data/
│   ├── raw/
│   └── images/
├── dbt_project/
├── fastapi_app/
├── dagster_pipeline/
├── scripts/
├── docker/
├── .env.example
```

---

## ✅ Completed Tasks

### Task 0 – Project Setup
- Dockerfile, Docker Compose
- requirements.txt, .env loader, Git branching

### Task 1 – Telegram Scraping
- Telethon-based scraper
- JSON output to `data/raw/YYYY-MM-DD/channel_name.json`

### Task 2 – dbt Transformation
- Star schema: `dim_channels`, `fct_messages`
- Tests: `not_null`, `unique`, custom

### Task 3 – Image Enrichment
- Scraped and saved Telegram images
- Ran YOLOv8 detection and stored results

### Task 4 – FastAPI
- Endpoints for:
  - `/api/reports/top-products`
  - `/api/channels/{channel}/activity`
  - `/api/search/messages?query=...`

### Task 5 – Dagster Orchestration
- Modular `@op` for scraping, loading, dbt, YOLO
- Launched in Dagster UI

---

## 📊 API Documentation

After running:
```bash
uvicorn fastapi_app.main:app --reload
```

Visit: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🔄 Running the Full Pipeline (Dagster)

```bash
dagster dev
```

Runs full pipeline through interactive UI.

---

## 📝 Author

**Kirubel Gizaw**  
10 Academy – Week 7 Challenge  
