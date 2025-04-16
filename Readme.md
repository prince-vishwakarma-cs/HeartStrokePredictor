# Heart Stroke Predictor

**Heart Stroke Predictor** is a machine learning-based web application designed to assess the risk of heart stroke in individuals based on various health and demographic parameters. By leveraging advanced classification algorithms, the application provides users with a predictive analysis to aid in early detection and preventive healthcare measures.

## 🌐 Live Demo

Access the application here: [heart-stroke-predictor.onrender.com](https://heart-stroke-predictor.onrender.com)

## 🧠 Features

- **User-Friendly Interface**: Intuitive design for seamless user interaction.
- **Predictive Analysis**: Utilizes trained machine learning models to predict stroke risk.
- **Multiple Model Support**: Incorporates both Support Vector Machine (SVM) and Multi-Layer Perceptron (MLP) classifiers.
- **Data Preprocessing**: Implements column transformers for efficient data handling.
- **Deployment Ready**: Configured for deployment on platforms like Render.

## 🛠️ Tech Stack

- **Frontend**: HTML, CSS
- **Backend**: Python (Flask)
- **Machine Learning**: scikit-learn
- **Model Serialization**: pickle
- **Deployment**: Render

## 📁 Project Structure

```
heart-stroke-predictor/
├── notebook/
│   └── [Jupyter notebooks for model training and evaluation]
├── templates/
│   └── index.html
├── app.py
├── requirements.txt
├── procfile
├── Neural_Network_MLPClassifier.pkl
├── Support_Vector_Machine.pkl
├── column_transformer.pkl
└── .gitignore
```

## ⚙️ Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone https://github.com/prince-vishwakarma-cs/heart-stroke-predictor.git
   cd heart-stroke-predictor
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**

   ```bash
   python app.py
   ```

   The application will be accessible at `http://127.0.0.1:5000/`.

## 📊 Dataset Overview

The model is trained on a comprehensive dataset encompassing various health indicators:

- **Demographic Features**: Gender, Age, Marital Status, Residence Type
- **Health Metrics**: Hypertension, Heart Disease, Average Glucose Level, BMI
- **Lifestyle Factors**: Smoking Status, Work Type

Each record in the dataset represents an individual's health profile, enabling the model to learn patterns associated with stroke occurrences.

## 📄 License

This project is licensed under the [MIT License](LICENSE).

## 🤝 Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## 📧 Contact

For any inquiries or feedback, please reach out to [emailaddress.prince@gmail.com].