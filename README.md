# 📧 Spam Email Detector

A machine learning-based Spam Email Detector built using Python and Scikit-learn. This application classifies email or SMS messages as **Spam** or **Not Spam** using Natural Language Processing (NLP) techniques and a Multinomial Naive Bayes classifier. The project also includes an interactive web interface built with Streamlit.

---

## 🚀 Features

- Detects Spam and Legitimate messages
- Text preprocessing using TF-IDF Vectorization
- Machine Learning model using Multinomial Naive Bayes
- Interactive Streamlit web application
- Simple and user-friendly interface
- Trained on the SMS Spam Collection Dataset

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Natural Language Processing (NLP)
- TF-IDF Vectorizer
- Multinomial Naive Bayes
- Streamlit
- Pickle
- Git & GitHub

---

## 📂 Project Structure

```
spam_email_detector/
│
├── data/
│   └── spam.csv
│
├── models/
│   ├── model.pkl
│   └── vectorizer.pkl
│
├── venv/
├── app.py
├── train_model.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/your-username/spam-email-detector.git

cd spam-email-detector
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Train the Model

Run:

```bash
python train_model.py
```

This will:

- Load the dataset
- Train the machine learning model
- Save the trained model in the `models` folder

---

## 🌐 Run the Application

```bash
streamlit run app.py
```

The application will open in your browser at:

```
http://localhost:8501
```

---

## 📊 Model Performance

- Algorithm: Multinomial Naive Bayes
- Feature Extraction: TF-IDF Vectorizer
- Accuracy: **96.68%**

---

## 📸 Application Preview

_Add screenshots of your application here._

Example:

```
Home Page Screenshot
Prediction Result Screenshot
```

---

## 📚 Dataset

SMS Spam Collection Dataset containing labeled spam and legitimate (ham) messages.

---

## 🎯 Future Improvements

- Email file (.eml) support
- Confidence score for predictions
- Deep Learning model (LSTM/BERT)
- Email attachment analysis
- Dark mode UI
- Deploy using Streamlit Cloud

---

## 👨‍💻 Author

**Viveka Sengalvarayan**

AI & Data Science Student

Passionate about Machine Learning, Artificial Intelligence, and Cybersecurity projects.

---

## ⭐ If you found this project useful, consider giving it a star!
