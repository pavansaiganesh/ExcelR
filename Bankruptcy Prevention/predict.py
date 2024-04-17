import joblib 

rf = joblib.load('RandomForest.pkl') 

def predict_type(arr):
    res = rf.predict(arr)
    if res == 0:
        return "bankruptcy"
    
    return "non-bankruptcy"