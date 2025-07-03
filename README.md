# פרויקט דאשבורד ב־Streamlit

פרויקט זה הוא דאשבורד אינטראקטיבי שמיועד להצגה וניתוח נתונים בצורה ויזואלית ונוחה לשימוש.

---

## מבנה הפרויקט

הפרויקט מחולק למודולים (קבצים) לפי מחלקות:

my_dashboard_project/
├── dashboard.py # הקובץ הראשי שמריץ את Streamlit
├── data_loader.py # מחלקת DataLoader - טעינת נתונים
├── visualizations.py # מחלקת Visualizer - הפקת גרפים
├── requirements.txt # רשימת ספריות נדרשות
└── README.md # תיעוד הפרויקט


---

## התקנת הספריות

התקנת התלויות הדרושות:

```Terminal

pip install -r requirements.txt

---
להרצת האפליקציה:


streamlit run dashboard.py
