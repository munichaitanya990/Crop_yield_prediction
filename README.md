AI-Powered Crop Yield Prediction & Optimization

An AI + ML powered web application that predicts crop yield based on soil, weather, and farming inputs, and optimizes fertilizer and irrigation levels for better productivity.

✨ Features

📊 Predict crop yield using 14+ input parameters
⚡ Real-time slider updates for soil/weather/farm inputs
🌱 Optimization tool to suggest fertilizer & irrigation strategies
🎨 User-friendly dashboard with modern UI (Tailwind + JS)
🔒 Secure login/signup system with Flask backend

🛠️ Tech Stack
Frontend: HTML, TailwindCSS, JavaScript
Backend: Flask (Python)
ML Model: Scikit-learn / custom-trained model
Database: SQLite (for user login/signup)

📂 Project Structure
Crop_Yield_Prediction/
│── app.py              # Flask backend with ML routes
│── users.db            # SQLite database (auto-created)
│── templates/
│   ├── login_signup.html
│   ├── dashboard.html
│── static/
│   ├── css/            # Stylesheets
│   ├── js/             # JavaScript files
│── model.pkl           # Trained ML model (if applicable)
│── README.md           # Project documentation

⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/your-username/crop-yield-prediction.git
cd crop-yield-prediction

2️⃣ Create Virtual Environment & Install Dependencies
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
pip install -r requirements.tx

(Your requirements.txt should include Flask, numpy, scikit-learn, etc.)

3️⃣ Run the App
python app.py


Open your browser and go to:
👉 http://127.0.0.1:5000

🚀 Usage

Sign Up / Log In with your email & password
Enter soil & weather data using sliders/inputs
Click Predict → Get crop yield in tons/ha
Use Optimize → Get best fertilizer & irrigation recommendations

🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you’d like to change.

📜 License

This project is licensed under the MIT License.
