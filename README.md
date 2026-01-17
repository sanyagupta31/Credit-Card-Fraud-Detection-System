# 💳 Credit Card Fraud Detection System

An end-to-end Machine Learning solution to detect fraudulent credit card transactions in real-time. This project demonstrates high-performance API development and multi-container orchestration.

## 🚀 Project Overview
* **ML Model:** Trained on a highly imbalanced dataset to identify fraud with high precision.
* **Backend:** Built using **FastAPI** for high-speed asynchronous processing.
* **Database:** **MySQL** used to store transaction logs and prediction history.
* **Orchestration:** Managed using **Docker Compose** to run the API and Database as separate services.

## 🛠️ Tech Stack
* **Language:** Python 3.9
* **Framework:** FastAPI
* **ML Libraries:** Scikit-learn, Pandas, Numpy, Imbalanced-learn
* **Database:** MySQL 8.0
* **Containerization:** Docker & Docker Compose

## 📦 How to Run
Since this is a multi-container application, we use Docker Compose:

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/SanyaGupta31/Credit-Card-Fraud-Detection.git](https://github.com/SanyaGupta31/Credit-Card-Fraud-Detection.git)
    cd Credit-Card-Fraud-Detection
    ```

2.  **Start the Services:**
    ```bash
    docker-compose up --build
    ```

3.  **Access the API:**
    * API Documentation (Swagger UI): `http://localhost:8000/docs`
    * The application will automatically connect to the MySQL database container.

## 🏗️ Architecture
The system consists of two main services:
1.  **FastAPI Service:** Handles prediction requests and communicates with the model.
2.  **MySQL Service:** Stores transaction data for future auditing and retraining.

---
