# 🛡️ Fraud Guard AI: End-to-End MLOps Pipeline

This project features a robust **Credit Card Fraud Detection System** built as a fully **Automated Production Pipeline**. It automates every stage of the lifecycle—from data versioning to cloud-ready deployment.

---

## 🚀 Key Features & Tools
* **Model Tracking (MLflow):** Achieved **99.94% accuracy** with full experiment logging.
* **Data Versioning (DVC):** Managed 143MB dataset efficiently using DVC.
* **CI/CD Pipeline (GitHub Actions):** Automated testing and Docker build on every commit.
* **Containerization (Docker):** Fully containerized for seamless deployment.
* **Interactive UI (Streamlit):** Real-time web interface for fraud prediction.

---

## 🏗️ Architecture
1. **Data Ingestion:** Version-tracked using **DVC**.
2. **CI/CD:** **GitHub Actions** builds the Docker image.
3. **Deployment:** Pushed to **Docker Hub** (`sanya860/credit-card-fraud`).

---

## 🛠️ How to Run Locally
Run this project with a single command using Docker:

```bash
docker pull sanya860/credit-card-fraud:latest
docker run -p 8501:8501 sanya860/credit-card-fraud:latest

