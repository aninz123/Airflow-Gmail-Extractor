# Airflow-Gmail-Extractor

project_name/
├── dags/
│   └── gmail_report_dag.py
├── credentials/
│   └── credentials.json
├── token.pickle
├── requirements.txt
└── README.md

dags/: โฟลเดอร์นี้เก็บไฟล์ DAG ของ Airflow ทั้งหมด
credentials/: โฟลเดอร์นี้เก็บข้อมูลรับรองของ Google API


token.pickle: ไฟล์นี้เก็บ access token และ refresh token ของผู้ใช้ ซึ่งถูกสร้างขึ้นอัตโนมัติเมื่อทำการอนุญาตครั้งแรก

requirements.txt: ไฟล์ที่ระบุไลบรารี Python ที่จำเป็นสำหรับโปรเจค

README.md: ไฟล์อ่านก่อน (README) ที่อธิบายการตั้งค่าและวิธีการใช้งานโปรเจค



set user on airflow

airflow users  create --role Admin --username admin --email admin --firstname admin --lastname admin --password admin