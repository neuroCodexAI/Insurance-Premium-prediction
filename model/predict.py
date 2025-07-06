import pickle
import pandas as pd


# import the ml model
with open('model/model.pkl', 'rb') as f:
    model = pickle.load(f)
    
#MLflow
MODEL_VERSION = '1.0.0'

# Get class labels from model (important for matching probabilities to class names)
class_labels = model.classes_.tolist()

def predict_output(user_input:dict):
    
    df = pd.DataFrame(user_input)
    
    predict_class = model.predict(df)[0]
    
    probabilites = model.predict_proba(df)[0]
    confidence = max(probabilites)
    
    class_probs = dict(zip(class_labels, map(lambda p: round(p,4), probabilites)))
    
    return {
        "predicted_category": predict_class,
        "confidence":round(confidence,4),
        "class_probabilities":class_probs
    }
    
    