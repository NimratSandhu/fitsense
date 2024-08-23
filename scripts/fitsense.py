import pandas as pd
import joblib
import os

def get_user_input():
    print("Please enter the following feature values:")
    
    # Definitions of features and their types
    features = {
        'age': int,
        'cp': int,           # chest pain type (e.g., 1, 2, 3, 4)
        'trestbps': int,     # resting blood pressure
        'chol': int,         # serum cholesterol
        'thalach': int,      # maximum heart rate achieved
        'exang': int,        # exercise induced angina (1 = yes, 0 = no)
        'oldpeak': float,    # ST depression induced by exercise relative to rest
        'slope': int,        # the slope of the peak exercise ST segment (e.g., 1, 2, 3)
        'ca': int,           # number of major vessels (0-3) colored by fluoroscopy
        'thal': int          # thalassemia (3 = normal, 6 = fixed defect, 7 = reversible defect)
    }

    user_data = {}
    for feature, dtype in features.items():
        while True:
            try:
                value = input(f"{feature}: ")
                user_data[feature] = dtype(value)
                break
            except ValueError:
                print(f"Invalid input for {feature}. Expected {dtype.__name__}. Please try again.")
    return user_data


def main():
    # Paths to the model and scaler (if applicable)
    model_path = "/Users/nimratsandhu/Documents/projects/fitsense/models/random_forest_model.pkl"

    # Check if the model file exists
    if not os.path.exists(model_path):
        print(f"Model file not found at {model_path}")
        return

    # Getting User Input
    user_data = get_user_input()
    user_data['sex'] = 0.5
    user_data['fbs'] = 0.15
    user_data['restecg'] = 0.5

    input_df = pd.DataFrame([user_data])

    input_data = input_df.values 

    model = joblib.load(model_path)

    # Make predictions
    prediction = model.predict(input_data)

    prediction_proba = model.predict_proba(input_data) if hasattr(model, "predict_proba") else None

    # Output the prediction
    result = 'Heart Disease' if prediction[0] == 1 else 'No Heart Disease'
    print(f"Prediction: {result}")
    
    if prediction_proba is not None:
        proba = prediction_proba[0]
        print(f"Prediction Probabilities:")
        for class_label, prob in zip(model.classes_, proba):
            label = 'Heart Disease' if class_label == 1 else 'No Heart Disease'
            print(f"  {label}: {prob:.2f}")

if __name__ == "__main__":
    main()