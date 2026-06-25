# Proyecto Bank Marketing DataOps

Repositorio académico para preparar, validar, almacenar, analizar y consumir datos de campañas de marketing bancario mediante una arquitectura reproducible de datos e Inteligencia Artificial.

El proyecto utiliza el dataset **Bank Marketing** y permite predecir si un cliente contratará un depósito a plazo.

---

# Objetivo

Desarrollar una solución DataOps que permita trabajar con:

* Python 3.11
* FastAPI
* Docker
*  GitHub
* Render
* Supabase PostgreSQL
* Pandas y NumPy
* Scikit-learn
* Joblib
* Modelo de clasificación binaria
* API REST para consulta y predicción

La variable objetivo del proyecto es:

```text
deposit
```

Donde:

```text
0 = Cliente no contrata depósito
1 = Cliente contrata depósito
```

---

# Estructura del Proyecto

```text
proyecto-gestion-de-datos/
├─ app/
│  ├─ __init__.py
│  ├─ main.py
│  ├─ db.py
│  └─ predict.py
│
├─ artifacts/
│  ├─ predictor_bank_tree.joblib
│  └─ scaler.joblib
│
├─ data/
│  └─ datos_02_bank_validados.csv
│
├─ scripts/
│  ├─ pre_procesamiento_caso_2.py
│  ├─ validación_de_datos_caso_2_.py
│  ├─ carga_de_datos_caso_2.py
│  └─ KFold_caso2.ipynb
│
├─ tests/
│  └─ test_health.py
│
├─ .github/
│  └─ workflows/
│     └─ ci.yml
│
├─ .env.example
├─ .gitignore
├─ .dockerignore
├─ Dockerfile
├─ render.yaml
├─ requirements.txt
└─ README.md
```

---

# Flujo Implementado

El proyecto implementa el siguiente flujo de trabajo:

1. Se utiliza un dataset de campañas de marketing bancario.
2. Se valida la estructura y calidad de los datos.
3. Se detectan registros inconsistentes o inválidos.
4. Se transforman variables categóricas a valores numéricos.
5. Se generan variables derivadas para mejorar el análisis.
6. Se genera un dataset validado.
7. Los datos validados se cargan en Supabase PostgreSQL.
8. Se entrenan modelos de clasificación binaria.
9. Se selecciona el modelo con mejor desempeño.
10. Se guarda el modelo y el scaler mediante Joblib.
11. La API FastAPI consulta datos desde Supabase.
12. La API permite realizar predicciones.
13. Las pruebas se ejecutan automáticamente mediante GitHub Actions.
14. La aplicación se despliega en Render mediante Docker.

---

# Dataset y Variable Objetivo

El dataset contiene información de clientes bancarios y campañas de telemarketing.

Algunas variables utilizadas son:

```text
age
job
marital
education
balance
housing
loan
contact
day
month
duration
campaign
pdays
previous
poutcome
deposit
```

La variable objetivo es:

```text
deposit
```

Interpretación:

```text
deposit = 0 → Cliente no contrata depósito
deposit = 1 → Cliente contrata depósito
```

---

# Variables Derivadas

Durante el preprocesamiento se generaron variables adicionales:

| Variable               | Descripción                                                        |
| ---------------------- | ------------------------------------------------------------------ |
| `es_cliente_nuevo`     | Indica si el cliente no posee contactos previos                    |
| `tiene_doble_prestamo` | Indica si el cliente tiene crédito hipotecario y préstamo personal |
| `duration_min`         | Duración de la llamada expresada en minutos                        |

Estas variables ayudan a mejorar la interpretación y el desempeño del modelo predictivo.

---

# Validación y Calidad de Datos

El pipeline considera validaciones como:

* Verificación de valores nulos.
* Validación de tipos de datos.
* Revisión de duración de llamadas.
* Identificación de valores inconsistentes.
* Validación de variables categóricas.
* Revisión de campos obligatorios.
* Transformación de variables 

El resultado del pipeline es el archivo:

```text
data/datos_02_bank_validados.csv
```

---

# Carga de Datos a Supabase

El script de carga es:

```bash
python scripts/carga_de_datos_caso_2.py
```

Este script:

* Lee el dataset validado.
* Se conecta a Supabase PostgreSQL.
* Inserta los registros procesados.
* Permite que la API consulte los datos desde la nube.

La tabla utilizada en Supabase contiene los registros bancarios procesados y validados.

---

# Modelos Evaluados

Se evaluaron distintos modelos de clasificación:

* Logistic Regression.
* Decision Tree.
* Multilayer Perceptron.

Para evaluar la estabilidad de los modelos se utilizó validación cruzada K-Fold.

Las métricas consideradas fueron:

```text
Accuracy
Precision
Recall
F1 Score
ROC-AUC
Coeficiente Gini
```

El modelo seleccionado se guarda en:

```text
artifacts/predictor_bank_tree.joblib
```

El escalador utilizado se guarda en:

```text
artifacts/scaler.joblib
```

---

# Endpoints Actuales

| Método | Endpoint             | Descripción                                |
| ------ | -------------------- | ------------------------------------------ |
| GET    | `/`                  | Verifica que la API esté activa            |
| GET    | `/health`            | Verifica el estado general de la API       |
| GET    | `/servicio?limit=10` | Devuelve registros almacenados en Supabase |
| POST   | `/predict`           | Realiza predicción de depósito             |
| GET    | `/docs`              | Documentación automática Swagger           |

---

# Ejecución Local

## 1. Clonar repositorio

```bash
git clone https://github.com/dasilvae/proyecto-gestion-de-datos.git
cd proyecto-gestion-de-datos
```

## 2. Crear entorno virtual

```bash
python -m venv venv
```

En Windows:

```bash
venv\Scripts\activate
```

En Linux o macOS:

```bash
source venv/bin/activate
```

## 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

## 4. Crear archivo `.env`

Crear un archivo `.env` utilizando como referencia `.env.example`.

Ejemplo:

```env
SUPABASE_URL=
SUPABASE_KEY=
DATABASE_URL=
```

No subir el archivo `.env` al repositorio.

## 5. Ejecutar la API

```bash
python -m uvicorn app.main:app --host 127.0.0.1 --port 8000
```

La API estará disponible en:

```text
http://127.0.0.1:8000
```

---

# Pruebas Locales de API

Probar en navegador, Swagger o Postman:

```text
http://127.0.0.1:8000/
http://127.0.0.1:8000/health
http://127.0.0.1:8000/servicio?limit=5
http://127.0.0.1:8000/docs
```

---

# Pruebas Automatizadas

Las pruebas se encuentran en:

```text
tests/test_health.py
```

Para ejecutarlas localmente:

```bash
pytest -v
```

Las pruebas verifican:

* Disponibilidad general de la API.
* Funcionamiento del endpoint `/health`.
* Acceso a la documentación Swagger.
* Generación de logs de auditoría.

---

# Docker

Construir imagen:

```bash
docker build -t bank-marketing-api .
```

Ejecutar contenedor:

```bash
docker run --name bank-marketing-container -p 8000:8000 --env-file .env bank-marketing-api
```

Luego acceder a:

```text
http://localhost:8000/docs
```

---

# CI/CD

El proyecto utiliza GitHub.

El workflow se encuentra en:

```text
.github/workflows/ci.yml
```

El pipeline:

* Instala dependencias.
* Ejecuta pruebas automatizadas.
* Valida el proyecto en cada `push` a la rama `main`.

Comando ejecutado por CI:

```bash
pytest -v
```

---

# Render

La aplicación se encuentra desplegada en Render.

URL pública:

[API Bank Marketing desplegada](https://proyecto-gestion-de-datos.onrender.com)

Pruebas públicas sugeridas:

[Estado de la API](https://proyecto-gestion-de-datos.onrender.com/health)

[Consulta de 5 registros](https://proyecto-gestion-de-datos.onrender.com/servicio?limit=5)

[Documentación Swagger](https://proyecto-gestion-de-datos.onrender.com/docs)

---

# Supabase

La conexión a Supabase PostgreSQL se realiza mediante variables de entorno.

Ejemplo:

```env
SUPABASE_URL=
SUPABASE_KEY=
DATABASE_URL=
```

La API consulta los datos mediante:

```text
GET /servicio?limit=10
```

Ejemplo público:

[Consulta de datos desde Supabase mediante la API](https://proyecto-gestion-de-datos.onrender.com/servicio?limit=10)

Las credenciales no deben ser publicadas en GitHub ni incluidas en el archivo `.env.example`.

---

# Estado Actual del Proyecto

* Repositorio creado y conectado a GitHub.
* Dataset bancario procesado.
* Validación y limpieza de datos implementada.
* Dataset validado generado.
* Datos cargados en Supabase.
* API FastAPI implementada.
* Endpoint de consulta de datos funcionando.
* Endpoint de predicción funcionando.
* Modelo de clasificación entrenado.
* Scaler guardado con Joblib.
* Dockerfile configurado.
* Pruebas locales implementadas.
* GitHub Actions configurado.
* Servicio desplegado en Render.
* Swagger disponible públicamente.
* Variables de entorno utilizadas para proteger credenciales.

---

# Checklist del Proyecto

* [x] Repositorio en GitHub.
* [x] README documentado.
* [x] Archivo `.env.example`.
* [x] Archivo `.gitignore`.
* [x] Dockerfile.
* [x] Workflow GitHub.
* [x] Servicio desplegado en Render.
* [x] Proyecto Supabase configurado.
* [x] Carga de datos ejecutada.
* [x] Endpoint de consulta funcionando.
* [x] Endpoint de predicción funcionando.
* [x] Modelo persistido.
* [x] Scaler persistido.
* [x] Pruebas automatizadas.

#
