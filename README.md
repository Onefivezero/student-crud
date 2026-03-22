# Student REST Application

This is a REST application meant to simulate a school's internal systems.

You can add Students and Classes, and enroll students in classes.

---

## 🛠️ Installation Guide

Follow these steps to set up the simulation environment locally.

### 1. Prerequisites
* **Python 3.10+**
* **Docker Desktop** (Required for the database testing suite)

### 2. Environment Setup
Clone the repository and navigate to the root directory:
```bash
# Create a virtual environment
python -m venv .venv

# Activate the environment
# On Windows:
.\.venv\Scripts\activate
# On Mac/Linux:
source .venv/bin/activate
```

### 3. Installing Dependencies
```bash
pip install -r requirements.txt
```

## Running The Tests
```bash
pip install pytest
pytest
```

## Running The Application
```bash
uvicorn src.app.app:app --reload
```