# 🛡 Windows AI Security Audit & Anomaly Detection System (Project 1)

## 📌 Project Overview

The **Windows AI Security Audit & Anomaly Detection System** is a standalone Python-based security auditing framework designed to:

- Collect Windows system telemetry
- Detect abnormal system behavior using Artificial Intelligence
- Generate detailed anomaly reports
- Provide automated security insights

This project runs locally and does not require any web interface.

---

# 🎯 Main Objective

The main objective of this project is:

- To automate Windows system security auditing
- To detect unusual or suspicious system behavior
- To apply AI-based anomaly detection using Isolation Forest
- To generate structured security reports
- To simulate endpoint-level security monitoring

---

# 🧠 Technologies Used

- Python
- psutil (System telemetry collection)
- pandas (Data processing)
- scikit-learn (Isolation Forest AI model)
- CSV reporting
- Windows Registry access (optional extended version)

---

# 🏗 Project Architecture

This project contains three main modules:

Project Folder
│
├── run.py
├── audit_collector.py
├── anomaly_detector.py

---


## 📂 File Descriptions

### 1️⃣ audit_collector.py

Responsible for:

- Collecting system information
- Extracting:
  - CPU usage
  - Memory usage
  - Running processes
  - Open ports
- Generating structured CSV file

---

### 2️⃣ anomaly_detector.py

Responsible for:

- Reading generated CSV file
- Extracting numeric features
- Running Isolation Forest
- Identifying anomalies
- Returning anomaly summary

---

### 3️⃣ run.py

Main controller script that:

- Calls audit_collector
- Runs anomaly_detector
- Prints anomaly results
- Generates structured text report
- Deletes temporary CSV files
- Shows detected anomaly details

---

# 🔎 How Scanning Works

## Step 1 – Data Collection

The system collects:

- CPU percentage
- Memory percentage
- Running process metrics
- Listening network ports

Data is saved in structured CSV format.

---

## Step 2 – AI Anomaly Detection

The anomaly detection process:

1. Load CSV file
2. Extract numeric features
3. Train Isolation Forest model
4. Predict anomalies
5. Label records as:
   - Normal
   - Anomaly

---

# 🤖 AI Model Used

## Isolation Forest

Why Isolation Forest?

- Unsupervised learning (no labeled attack data needed)
- Efficient for anomaly detection
- Works well on tabular system telemetry
- Detects statistical outliers

Prediction Mapping:

- `1 → Normal`
- `-1 → Anomaly`

---

# 📊 Output Generated

After execution:

- Terminal shows:
  - Total records
  - Total anomalies
  - Names of anomalous processes/ports
- Text report file generated:
  - Machine name
  - Timestamp
  - Anomaly summary
  - Detailed anomaly listing
- Temporary CSV files automatically removed

---

# ⚠ Limitations

- Works only on Windows
- Requires Python installed
- Requires local execution
- Statistical anomaly detection (not signature-based)
- Does not detect specific malware signatures

---

# 🚀 Future Scope

- Add GUI interface
- Add server-client architecture
- Store historical scans in database
- Add severity scoring system
- Add PDF export
- Add rule-based detection engine
- Integrate with SIEM systems
- Convert into background agent
- Implement deep learning Autoencoder model

---

# 👥 Team

- **Adithya Vallabhaneni**

---

# 🛠 Local Deployment Guide

Follow the steps below to run the project locally.

---

## ✅ Step 1 – Install Python

Download Python from:

https://www.python.org/downloads/

During installation:

- Check "Add Python to PATH"
- Click Install

Verify installation:

```bash
python --version
```

## Step 2 – Navigate to Project Folder

```bash
git clone https://github.com/Adithya0503/IDS_Vanilla
cd IDS_Vanilla
```

## Step 3 – Create Virtual Environment

```bash
python -m venv venv
```

## Step 4 - Activate the Virtual Environment
```bash
venv\Scripts\activate
```
If You Get PowerShell Execution Error
Run once:
```bash
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```
Then activate venv again.

## Step 5 - Install Dependencies
```bash
pip install -r requirements.txt
```
