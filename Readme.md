# 🩺 Multiple Disease Prediction System

A collaborative Streamlit web application designed to predict the likelihood of multiple diseases based on user-provided medical data.

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![License](https://img.shields.io/badge/license-MIT License-green)
![Stars](https://img.shields.io/github/stars/Netri-100224/Multiple_Disease_Prediction_System?style=social)
![Forks](https://img.shields.io/github/forks/Netri-100224/Multiple_Disease_Prediction_System?style=social)

![Project Preview](/preview_example.png)
_A preview of the Multiple Disease Prediction System in action, showcasing its intuitive interface._


## ✨ Features

*   **Comprehensive Disease Prediction:** Integrates four distinct prediction models for various diseases including Breast Cancer, Diabetes, Heart Disease, and Parkinson's.
*   **User-Friendly Web Interface:** Built with Streamlit, providing an intuitive and interactive experience for users to input medical data and receive predictions.
*   **Data-Driven Insights:** Leverages pre-trained machine learning models (`.sav` files) to offer accurate and reliable predictions based on medical reports.
*   **Modular & Extensible Architecture:** Designed to easily incorporate additional disease prediction models, making the system adaptable and future-proof.
*   **Quick Health Status Overview:** Offers a streamlined assessment of a person's overall health by combining predictions from multiple medical report analyses.


## 🚀 Installation

Follow these steps to set up and run the Multiple Disease Prediction System locally on your machine.

### Prerequisites

Ensure you have Python 3.8 or higher installed on your system.

### Step-by-Step Installation

1.  **Clone the Repository:**
    Begin by cloning the project repository to your local machine using Git:

    ```bash
    git clone https://github.com/Netri-100224/Multiple_Disease_Prediction_System.git
    cd Multiple_Disease_Prediction_System
    ```

2.  **Create a Virtual Environment (Recommended):**
    It is highly recommended to create a virtual environment to manage project dependencies and avoid conflicts with other Python projects:

    ```bash
    python -m venv venv
    ```

3.  **Activate the Virtual Environment:**
    Activate the newly created virtual environment based on your operating system:

    *   **On Windows:**
        ```bash
        .\venv\Scripts\activate
        ```
    *   **On macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```

4.  **Install Dependencies:**
    Install all required Python packages listed in the `requirements.txt.txt` file using `pip`:

    ```bash
    pip install -r requirements.txt.txt
    ```
    _Note: The dependency file is named `requirements.txt.txt`. Please use this exact filename during installation._


## 💡 Usage

Once the application is installed and the virtual environment is activated, you can launch the Streamlit web application.

1.  **Start the Streamlit Application:**
    Navigate to the root directory of the project (if not already there) and execute the Streamlit application:

    ```bash
    streamlit run mul_disease.py
    ```

2.  **Access the Web Interface:**
    Open your web browser and navigate to the URL provided by Streamlit (typically `http://localhost:8501`).

3.  **Input Medical Data:**
    On the web interface, you will find options to select different disease prediction systems. Input the required medical parameters into the respective fields. The system will then process your data and provide a prediction.

![Usage Screenshot](/usage_screenshot.png)
_An example of the user interface where medical parameters are input for prediction._


## 🗺️ Project Roadmap

The Multiple Disease Prediction System is actively being developed and improved. Here are some of the upcoming features and planned enhancements:

*   **Version 1.1.0 - Enhanced UI/UX:** Focus on refining the user interface and overall user experience, including more intuitive input forms, dynamic visualizations for results, and improved accessibility.
*   **Integration of More Models:** Expand the system by incorporating prediction models for additional diseases (e.g., Kidney Disease, Liver Disease, Thyroid conditions).
*   **User Authentication & History:** Implement a basic user authentication system to allow users to save their medical reports and track their prediction history over time.
*   **API Endpoints:** Develop RESTful API endpoints for each prediction model, enabling easy integration with other applications and services.
*   **Performance Optimization:** Continuously optimize model loading times, prediction speed, and overall application responsiveness for a smoother user experience.


## 🤝 Contributing

We warmly welcome contributions to the Multiple Disease Prediction System! Your efforts can help make this project even better. Please follow these guidelines to contribute:

1.  **Fork the Repository:** Start by forking the `Multiple_Disease_Prediction_System` repository to your GitHub account.
2.  **Create a New Branch:** Create a new branch for your feature or bug fix. Use a descriptive name that reflects your changes.
    ```bash
    git checkout -b feature/add-new-disease-model
    ```
    or
    ```bash
    git checkout -b fix/resolve-ui-bug
    ```
3.  **Implement Your Changes:** Write clear, concise, and well-documented code. Ensure your code adheres to Python's [PEP 8 style guide](https://www.python.org/dev/peps/pep-0008/).
4.  **Test Your Changes:** Before submitting, thoroughly test your changes to ensure they do not introduce new issues and that existing functionalities work as expected. Add new test cases if applicable.
5.  **Commit Your Changes:** Write clear, descriptive commit messages following conventional commits if possible .
