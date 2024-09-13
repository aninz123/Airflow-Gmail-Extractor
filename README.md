# Airflow-Gmail-Extractor

## Sakelaton Project
```
project_name/
├── dags/
│   └── gmail_report_dag.py
├── credentials/
│   └── credentials.json
├── token.pickle
├── requirements.txt
└── README.md
```

__dags__ : โฟลเดอร์นี้เก็บไฟล์ DAG ของ Airflow ทั้งหมด
credentials/: โฟลเดอร์นี้เก็บข้อมูลรับรองของ Google API


token.pickle: ไฟล์นี้เก็บ access token และ refresh token ของผู้ใช้ ซึ่งถูกสร้างขึ้นอัตโนมัติเมื่อทำการอนุญาตครั้งแรก

requirements.txt: ไฟล์ที่ระบุไลบรารี Python ที่จำเป็นสำหรับโปรเจค



# Setup 

## 1. Install Airflow Lib
```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
## 2. Export Env.
```
export AIRFLOW_HOME=$(pwd)
```
# Initialize Database and create user 
```
airflow db init
airflow users create --username admin --firstname Admin --lastname User --role Admin --email admin@example.com
```

# Start Airflow Services
```
airflow scheduler &
airflow webserver --port 8080 &
```


## - option command
```
# create user on airflow
airflow users  create --role Admin --username admin --email admin --firstname admin --lastname admin --password admin

```

