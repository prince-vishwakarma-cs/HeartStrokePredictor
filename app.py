from flask import Flask,request,render_template
import pickle
import pandas as pd

app= Flask(__name__)

nn_model=pickle.load(open('Neural_Network_MLPClassifier.pkl', 'rb'))
svm_model=pickle.load(open('Support_Vector_Machine.pkl', 'rb'))
transformer=pickle.load(open('column_transformer.pkl', 'rb'))

@app.route("/")
def index():
    return render_template('index.html')


@app.route('/predict',methods=['POST'])
def predict():
    data = request.form
    
    age = int(data['age'])
    gender = data['gender']
    chest_pain = int(data['chest_pain'])
    high_blood_pressure = int(data['high_blood_pressure'])
    irregular_heartbeat = int(data['irregular_heartbeat'])
    shortness_of_breath = int(data['shortness_of_breath'])
    fatigue_weakness = int(data['fatigue_weakness'])
    dizziness = int(data['dizziness'])
    swelling_edema = int(data['swelling_edema'])
    neck_jaw_pain = int(data['neck_jaw_pain'])
    excessive_sweating = int(data['excessive_sweating'])
    persistent_cough = int(data['persistent_cough'])
    nausea_vomiting = int(data['nausea_vomiting'])
    chest_discomfort = int(data['chest_discomfort'])
    cold_hands_feet = int(data['cold_hands_feet'])
    snoring_sleep_apnea = int(data['snoring_sleep_apnea'])
    anxiety_doom = int(data['anxiety_doom'])
    selected_model = data['model']

    test_df = pd.DataFrame({
        'age': [age],
        'gender': [gender],
        'chest_pain': [chest_pain],
        'high_blood_pressure': [high_blood_pressure],
        'irregular_heartbeat': [irregular_heartbeat],
        'shortness_of_breath': [shortness_of_breath],
        'fatigue_weakness': [fatigue_weakness],
        'dizziness': [dizziness],
        'swelling_edema': [swelling_edema],
        'neck_jaw_pain': [neck_jaw_pain],
        'excessive_sweating': [excessive_sweating],
        'persistent_cough': [persistent_cough],
        'nausea_vomiting': [nausea_vomiting],
        'chest_discomfort': [chest_discomfort],
        'cold_hands_feet': [cold_hands_feet],
        'snoring_sleep_apnea': [snoring_sleep_apnea],
        'anxiety_doom': [anxiety_doom]
    })
    
    test_df=pd.DataFrame(transformer.transform(test_df), columns=transformer.get_feature_names_out())

    if selected_model == "nn":
        prediction = nn_model.predict(test_df)[0]
    else:
        prediction = svm_model.predict(test_df)[0]
        
    print(prediction)
    
    return render_template('result.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
    
    
