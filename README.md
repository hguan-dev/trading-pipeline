
# Trading Pipeline Project

## Introduction

This project is a fully functional **trading pipeline** for **Coinbase's BTC**, designed to fetch market data, compute trading features, make predictions, and analyze performance. The system is built using a mix of **Python** and **C++**, integrating real-time data processing with machine learning-based inference. 

The pipeline consists of multiple components:
- **Data Ingestion**: Fetching and processing real-time market data.
- **Feature Computation**: Generating key trading indicators in **C++**.
- **Inference & Model Training**: Implementing an **online learning** model in **Python**.
- **Performance Analysis**: Evaluating prediction accuracy using statistical methods.

At the end of the pipeline, the system can analyze historical market data, generate insights, and validate prediction effectiveness.

## Technologies Used

- **Programming Languages**: Python, C++
- **Data Ingestion**: REST API (Coinbase, Gemini)
- **Machine Learning**: Scikit-learn (Lasso Regression)
- **C++ Integration**: Pybind11
- **Build System**: CMake, Ninja, GNU Make
- **Dependency Management**: Poetry (Python), Conan (C++)
- **Testing Frameworks**: Pytest (Python), GoogleTest (C++)
- **Linting & Formatting**: Ruff, Mypy, Clang-Format, Clang-Tidy
- **CI/CD**: GitHub Actions

## System Requirements

The following packages must be installed on a **UNIX or UNIX-like environment**:

- **C++ Build Tools**:  
  - GNU Make  
  - CMake  
  - Ninja  
  - Conan  

- **C++ Linters & Formatters**:  
  - Clang-Format  
  - Clang-Tidy  

- **Python Tools**:  
  - Poetry  
  - Mypy  
  - Ruff  
  - Pytest  

- **Python Version**:  
  - Python **3.12** with Development Headers  

## Project Structure

```
/trading-pipeline
│── pysrc/                  # Python source files
│   ├── data_client.py      # Fetches and processes market data
│   ├── inference.py        # Machine learning model for predictions
│   ├── analysis.py         # Evaluates prediction performance
│── cppsrc/                 # C++ source files
│   ├── features.hpp        # C++ feature computation (header-only)
│   ├── bindings.cpp        # Pybind11 integration for Python
│── tests/                  # Unit and integration tests
│── scripts/                # Utility scripts for data and model handling
│── CMakeLists.txt          # CMake build configuration
│── pyproject.toml          # Python dependencies (Poetry)
│── README.md               # Project documentation
```

## Key Features

- **Real-Time Market Data Fetching**: Collects trade history from **Gemini API**.
- **High-Performance Feature Computation**: Implements feature calculations in **C++** using a header-only architecture.
- **Online Machine Learning**: Uses **Lasso regression** with a rolling dataset to make predictions.
- **Automated Testing & CI/CD**: Ensures stability with **GitHub Actions** running **unit and integration tests**.
- **Optimized for Performance**: Moves critical data processing from Python to C++ for improved efficiency.
