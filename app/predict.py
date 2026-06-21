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

    pred = int(modelo.predict(valores)[0])

    try:
        proba = modelo.predict_proba(valores)[0]

        probability_no = round(float(proba[0]) * 100, 2)
        probability_si = round(float(proba[1]) * 100, 2)

    except Exception:
        probability_no = None
        probability_si = None

    return {
        "status": "ok",
        "prediction": {
            "predicted_class": pred,
            "predicted_label": "SI" if pred == 1 else "NO",
            "probability_no": probability_no,
            "probability_si": probability_si
        }
    }
