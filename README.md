🛡️ Fraud Guard AI: End-to-End MLOps Pipeline
This project features a robust Credit Card Fraud Detection System built not just as a standalone machine learning model, but as a fully Automated Production Pipeline. It automates every stage of the lifecycle—from data versioning to cloud-ready deployment.

🚀 Key Features & Tools
Model Tracking (MLflow): All experiments, parameters, and hyperparameter tuning were meticulously tracked. The model achieved a high performance of 99.94% accuracy.

Data Versioning (DVC): Large datasets (143MB) are managed outside of Git using DVC, ensuring a lightweight and efficient repository.

CI/CD Pipeline (GitHub Actions): Every code push triggers an automated testing and container build process to ensure system integrity.

Containerization (Docker): The entire environment is containerized to eliminate the "it works on my machine" problem, making it deployable anywhere.

Interactive UI (Streamlit): A sleek, user-friendly web interface for real-time transaction fraud checks.

🏗️ Architecture
Ingestion: Data is securely pulled and version-tracked using DVC.

Training: The model training pipeline is logged and managed via MLflow.

CI/CD: GitHub Actions verify the code and build a fresh Docker image on every commit.

Deployment: The image is automatically pushed to Docker Hub (sanya860/credit-card-fraud) for production-ready access.

🛠️ How to Run Locally
No local Python environment or dependencies are required. You only need Docker installed:

Bash

# Pull the image from Docker Hub
docker pull sanya860/credit-card-fraud:latest

# Run the container
docker run -p 8501:8501 sanya860/credit-card-fraud:latest
Once running, open your browser and go to http://localhost:8501 to use the application!