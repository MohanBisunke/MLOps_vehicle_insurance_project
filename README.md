**MLOps Vehicle Insurance Prediction**

---

# 🚗 **MLOps Vehicle Insurance Prediction**

A fully-automated, end-to-end MLOps project that predicts whether a customer will purchase vehicle insurance.
This project includes data ingestion from MongoDB, data validation, data transformation, model training, model evaluation, CI/CD pipelines, Dockerization, AWS deployment, and a prediction web app.

---

## 📂 **Project Features**

* Modular & scalable project structure
* Local package development using `setup.py` + `pyproject.toml`
* MongoDB Atlas integration
* Custom logging and exception handling
* Data Ingestion → Validation → Transformation → Model Training
* Model evaluation + model registry on AWS S3
* CI/CD pipeline using GitHub Actions
* Docker containerization
* Deployment on AWS EC2 (self-hosted runner)
* Web App for predictions
* Training endpoint exposed at `/training`

---


# ⚙️ **Step-by-Step Workflow**

Below is the refined and clearly formatted version of your 34-step workflow.

---

# 🔰 **1. Project Setup**

### **Step 1 — Create project template**

Run:

```bash
python template.py
```

This generates the complete project folder structure.

---

# 📦 **2. Setup Local Package Imports**

Edit `setup.py` and `pyproject.toml` to allow importing local modules.

Refer to **crashcourse.txt** for more info on both files.

---

# 🧪 **3. Create Virtual Environment & Install Dependencies**

```bash
conda create -n mlops-vehicle python=3.10 -y
conda activate mlops-vehicle
pip install -r requirements.txt
```

Add any required libraries to `requirements.txt` before installation.

---

# 📝 **4. Verify Local Package Installation**

```bash
pip list
```

Ensure your custom modules appear in the list.

---

# 🍃 **MongoDB Atlas Setup**

## **5–9. Setup MongoDB Atlas**

1. Sign up → Create project → Proceed with defaults
2. “Create cluster” → Select free tier (M0) → Deploy
3. Create DB user → username/password
4. Network Access → Add IP: `0.0.0.0/0`
5. “Get Connection String” → Choose *Python 3.6+* → Copy URL

---

# 📓 **10–13. Notebook Preparation**

* Create folder `notebook/`
* Add dataset
* Create `mongoDB_demo.ipynb`
* Select kernel → Python → vehicle
* Write notebook code to push dataset into MongoDB
* Go to MongoDB → Browse Collections → Verify stored documents

---

# 🧾 **Logging, Exceptions & Notebooks**

## **14–16. Logging & Exception Handling**

* Implement `logger.py`
* Implement custom exception handler
* Test both using `demo.py`
* Add EDA + Feature Engineering notebook

---

# 🛠️ **Data Ingestion (Core Pipeline Work)**

## **17. Build Data Ingestion Component**

You will:

* Add variables in `constants/__init__.py`
* Implement MongoDB connection in `configuration/mongo_db_connections.py`
* Add `proj1_data.py` under `data_access/`
* Convert MongoDB key-value data → DataFrame
* Add config classes in `entity/config_entity.py`
* Add artifact classes in `entity/artifact_entity.py`
* Build ingestion logic in `components/data_ingestion.py`
* Add ingestion logic to `training_pipeline.py`
* Run everything via `demo.py`

---

## **18. Set MongoDB URL as Environment Variable**

### **For Bash**

```bash
export MONGODB_URL="mongodb+srv://user:pass@cluster-url"
echo $MONGODB_URL
```

### **For PowerShell**

```powershell
$env:MONGODB_URL="mongodb+srv://user:pass@cluster-url"
echo $env:MONGODB_URL
```

### **Windows GUI**

Environment Variables → Add:

```
Name: MONGODB_URL
Value: <your url>
```

Add `artifact/` to `.gitignore`.

---

# 🧹 **Data Validation, Transformation & Model Trainer**

## **19–22. Continue Pipeline Implementation**

1. Complete `utils/main_utils.py`
2. Create `config/schema.yaml` with dataset schema
3. Implement **Data Validation** component
4. Implement **Data Transformation** component

   * Add `estimator.py` inside entity folder
5. Implement **Model Trainer**

   * Update estimator class

---

# ☁️ **AWS Setup (Required Before Model Evaluation)**

## **23. Configure AWS IAM + S3**

* Create IAM user → AdminAccess
* Create Access Keys
* Set the following env vars:

### **Bash**

```bash
export AWS_ACCESS_KEY_ID="..."
export AWS_SECRET_ACCESS_KEY="..."
```

### **PowerShell**

```powershell
$env:AWS_ACCESS_KEY_ID="..."
$env:AWS_SECRET_ACCESS_KEY="..."
```

### **Add the following to** `constants/__init__.py`

```
MODEL_EVALUATION_CHANGED_THRESHOLD_SCORE = 0.02
MODEL_BUCKET_NAME = "my_bucket"
MODEL_PUSHER_S3_KEY = "model-registry"
```

### **Create S3 Bucket**

* Region: us-east-1
* Name: *name*
* Disable “Block public access”

### **Update Code**

* Add `aws_connection.py`
* Add `aws_storage/` utilities
* Add `s3_estimator.py` inside entity folder

---

# 🧪 **24. Model Evaluation + Model Pusher**

Build components that:

* Compare new vs existing models
* Push better model to AWS S3
* Update local registry

---

# 🔮 **25–26. Prediction Pipeline & Web App**

* Implement prediction pipeline
* Create `app.py`
* Add `static/` and `templates/` folder for UI

---

# 🐳 **27–32. CI/CD, Docker & Deployment**

## **Docker**

* Add `Dockerfile`
* Add `.dockerignore`

## **GitHub Actions**

* Add `.github/workflows/aws.yaml`

## **ECR Setup**

* Create repo: `vehicleproj`
* Copy repository URI

## **EC2 Setup**

* Launch Ubuntu instance
* Install Docker
* Connect GitHub self-hosted runner
* Add GitHub secrets:

```
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
AWS_DEFAULT_REGION
ECR_REPO
```

## **Open port 5080**

* EC2 → Security Group → Inbound Rules
* Add: TCP | 5080 | 0.0.0.0/0

## **Access App**

```
http://<public-ip>:5080
```

---

# 🏁 **33–34. Final Steps**

* CI/CD triggers on every push
* Web app available at port 5080
* Run model training via:

```
/training
```

---

# 🚀 **How to Run the Project Locally**

```bash
conda activate vehicle
python demo.py        # For running pipeline
python app.py         # For running UI app
```

---
