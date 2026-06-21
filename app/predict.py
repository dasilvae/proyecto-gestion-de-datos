import joblib
import numpy as np

modelo = joblib.load("artifacts/predictor_bank_tree.joblib")

def predecir(data):
    valores = [[
        data["age"],
        data["job"],
        data["marital"],
        data["education"],
        data["default"],
        data["balance"],
        data["housing"],
        data["loan"],
        data["contact"],
        data["day"],
        data["month"],
        data["duration"],
        data["campaign"],
        data["pdays"],
        data["previous"],
        data["poutcome"],
        data["es_cliente_nuevo"],
        data["tiene_doble_prestamo"],
        data["duration_min"]
    ]]

    pred = modelo.predict(valores)[0]

    try:
        prob = round(float(np.max(modelo.predict_proba(valores)[0])) * 100, 2)
    except:
        prob = None

    pred = int(modelo.predict(valores)[0])

    resultado = "SI" if pred == 1 else "NO"

    return {
        "prediccion": pred,
        "resultado": resultado,
        "probabilidad_porcentaje": prob
    }