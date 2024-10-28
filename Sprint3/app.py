import streamlit as st
import pickle
import pandas as pd

# Load the trained model
st.write("Loading the model...")
with open('rf_model.pkl', 'rb') as file:
    model = pickle.load(file)

st.write("Model loaded successfully.")

# Define a function to encode categorical variables
def encode_categorical(values, categories):
    return [categories.index(value) for value in values]

# Function to get user input
def get_user_input():
    st.header("Patient Information")
    st.write("Rendering input fields...")

    # Demographic Details
    age = st.number_input("Age", min_value=5, max_value=80, value=25)
    gender = st.selectbox("Gender", ["Male", "Female"])
    ethnicity = st.selectbox("Ethnicity", ["Caucasian", "African American", "Asian", "Other"])
    education_level = st.selectbox("Education Level", ["None", "High School", "Bachelor's", "Higher"])

    # Lifestyle Factors
    bmi = st.number_input("BMI", min_value=15.0, max_value=40.0, value=22.5)
    smoking = st.selectbox("Smoking", ["No", "Yes"])
    physical_activity = st.slider("Weekly Physical Activity (hours)", min_value=0, max_value=10, value=3)
    diet_quality = st.slider("Diet Quality", min_value=0, max_value=10, value=5)
    sleep_quality = st.slider("Sleep Quality", min_value=4, max_value=10, value=6)

    # Environmental and Allergy Factors
    pollution_exposure = st.slider("Pollution Exposure", min_value=0, max_value=10, value=5)
    pollen_exposure = st.slider("Pollen Exposure", min_value=0, max_value=10, value=4)
    dust_exposure = st.slider("Dust Exposure", min_value=0, max_value=10, value=5)
    pet_allergy = st.selectbox("Pet Allergy", ["No", "Yes"])

    # Medical History
    family_history_asthma = st.selectbox("Family History of Asthma", ["No", "Yes"])
    history_of_allergies = st.selectbox("History of Allergies", ["No", "Yes"])
    eczema = st.selectbox("Eczema", ["No", "Yes"])
    hay_fever = st.selectbox("Hay Fever", ["No", "Yes"])
    gastro_reflux = st.selectbox("Gastroesophageal Reflux", ["No", "Yes"])

    # Clinical Measurements
    lung_function_fev1 = st.slider("Lung Function (FEV1 in liters)", min_value=1.0, max_value=4.0, value=3.0)
    lung_function_fvc = st.slider("Lung Function (FVC in liters)", min_value=1.5, max_value=6.0, value=4.0)

    # Symptoms
    wheezing = st.selectbox("Wheezing", ["No", "Yes"])
    shortness_of_breath = st.selectbox("Shortness of Breath", ["No", "Yes"])
    chest_tightness = st.selectbox("Chest Tightness", ["No", "Yes"])
    coughing = st.selectbox("Coughing", ["No", "Yes"])
    nighttime_symptoms = st.selectbox("Nighttime Symptoms", ["No", "Yes"])
    exercise_induced = st.selectbox("Exercise-Induced Symptoms", ["No", "Yes"])

    # Convert categorical values
    gender = 1 if gender == "Female" else 0
    smoking = 1 if smoking == "Yes" else 0
    pet_allergy = 1 if pet_allergy == "Yes" else 0
    family_history_asthma = 1 if family_history_asthma == "Yes" else 0
    history_of_allergies = 1 if history_of_allergies == "Yes" else 0
    eczema = 1 if eczema == "Yes" else 0
    hay_fever = 1 if hay_fever == "Yes" else 0
    gastro_reflux = 1 if gastro_reflux == "Yes" else 0
    wheezing = 1 if wheezing == "Yes" else 0
    shortness_of_breath = 1 if shortness_of_breath == "Yes" else 0
    chest_tightness = 1 if chest_tightness == "Yes" else 0
    coughing = 1 if coughing == "Yes" else 0
    nighttime_symptoms = 1 if nighttime_symptoms == "Yes" else 0
    exercise_induced = 1 if exercise_induced == "Yes" else 0

    # Encode categorical variables
    ethnicity_encoded = encode_categorical([ethnicity], ["Caucasian", "African American", "Asian", "Other"])[0]
    education_level_encoded = encode_categorical([education_level], ["None", "High School", "Bachelor's", "Higher"])[0]

    # Create DataFrame
    features = pd.DataFrame({
        "Age": [age], "Gender": [gender], "Ethnicity": [ethnicity_encoded],
        "EducationLevel": [education_level_encoded], "BMI": [bmi],
        "Smoking": [smoking], "PhysicalActivity": [physical_activity],
        "DietQuality": [diet_quality], "SleepQuality": [sleep_quality],
        "PollutionExposure": [pollution_exposure], "PollenExposure": [pollen_exposure],
        "DustExposure": [dust_exposure], "PetAllergy": [pet_allergy],
        "FamilyHistoryAsthma": [family_history_asthma],
        "HistoryOfAllergies": [history_of_allergies], "Eczema": [eczema],
        "HayFever": [hay_fever], "GastroesophagealReflux": [gastro_reflux],
        "LungFunctionFEV1": [lung_function_fev1], "LungFunctionFVC": [lung_function_fvc],
        "Wheezing": [wheezing], "ShortnessOfBreath": [shortness_of_breath],
        "ChestTightness": [chest_tightness], "Coughing": [coughing],
        "NighttimeSymptoms": [nighttime_symptoms], "ExerciseInduced": [exercise_induced]
    })

    st.write("User input collected:", features)  # Log user input
    return features

# Main function
def main():
    st.title("Asthma Prediction App")
    user_input = get_user_input()

    if st.button("Predict"):
        st.write("Making a prediction...")
        prediction = model.predict(user_input)[0]
        st.write(f"Prediction result: {prediction}")

        if prediction == 1:
            st.success("The model predicts: Asthma")
        else:
            st.success("The model predicts: No Asthma")

if __name__ == "__main__":
    main()
