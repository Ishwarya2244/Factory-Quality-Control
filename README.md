Factory Quality Control System::

TNWISE Project – AI-Based Factory Quality Control

Project Description::

This project allows factory operators to input machine data like:

1.Temperature

2.Speed

3.Usage

The system processes this data using a trained AI model and predicts whether the production output is acceptable or defective.

Technologies Used:

*Python

*FastAPI / Flask (backend API)

*HTML (index.html frontend)

*Machine Learning (train_model.py)

*Pickle (factory_ai_model.pkl)

Project Files:

1.backend/ – Backend scripts

2.check_model.py – Test the trained model with new inputs

3.train_model.py – Train the AI model

4.factory_ai_model.pkl – Trained model

5.index.html – Web interface to input machine data and get predictions

How to Run ?

#Clone the repository:

git clone https://github.com/Ishwarya2244/Factory-Quality-Control.git


#Install dependencies:

pip install -r requirements.txt


(Include packages like pandas, numpy, scikit-learn, fastapi, etc.)
#Run the backend server:

python backend/main.py

Open index.html in a browser.

Enter machine data (temperature, speed, usage) → get prediction response.

***Author***

""Ishwarya R"" – 3nd-year{ AI & Data Science student}
