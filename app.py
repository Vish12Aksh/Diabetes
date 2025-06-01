from flask import Flask, render_template, request, jsonify
import numpy as np
import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score , classification_report

pregnancies ,Glucose, BloodPressure, SkinThickness, Insulin, BMI, diabetesPedigreeFunction, age = 0,0,0,0,0, 0, 0,0
storeresult = ''

# Initialize Flask app
app = Flask(__name__)

# Load and preprocess data
data = pd.read_csv('diabetes.csv')
data[['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']] = data[['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']].replace(0, np.nan)
data.fillna(data.mean(), inplace=True)


# Prepare training data
scaler = StandardScaler()
X = scaler.fit_transform(data.drop(['Outcome'], axis=1))
# print(X[0])
Y = data['Outcome']

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42, stratify=Y)

model = SVC(kernel='linear', probability=True)
model.fit(x_train, y_train)

# Evaluate model
y_pred = model.predict(x_test)
print()


print(f"Model Accuracy: {accuracy_score(y_test, y_pred):.2f}")
print(f"Model report: {classification_report(y_test, y_pred)}")


def get_user_input(**dftg):
   
    # Convert values to integers and store in xycheck
    xycheck = np.array(list(map(int, dftg.values()))).reshape(1, -1)
    print(xycheck, 908)
    # Scale user input
    user_input_scaled = scaler.transform(xycheck)
    print(3)
    # Make prediction
    prediction = model.predict(user_input_scaled)
    result = "Diabetic" if prediction[0] == 1 else "Non-Diabetic"

    return  result # Returning the prediction result





@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    data = request.get_json()
    pregnancies = data.get('pregnancies')
    glucose = data.get('glucose')
    bloodPressure = data.get('bloodPressure')
    skinThickness = data.get('skinThickness')
    insulin = data.get('insulin')
    bmi = data.get('bmi')
    diabetesPedigreeFunction = data.get('diabetesPedigreeFunction')
    age = data.get('age')
    

    storeresult  = get_user_input(pregnancies=pregnancies, Glucose=glucose, BloodPressure=bloodPressure, SkinThickness=skinThickness, Insulin=insulin, BMI=bmi, diabetesPedigreeFunction=diabetesPedigreeFunction, age=age)
    return jsonify({
        # 'pregnancies': pregnancies,
        # 'glucose': glucose,
        
        'result': storeresult

    })



if __name__ == '__main__':
        
    app.run()

