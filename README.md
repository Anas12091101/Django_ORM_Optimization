# **Optimizing Django ORM Queries for Performance**

This repository demonstrates best practices for optimizing Django ORM queries and highlights common pitfalls. The project includes examples of **good and bad queries**, allowing you to analyze their performance using **Django Silk**.

---

## **Getting Started**

### **1. Clone the Repository**
```bash
git clone https://github.com/Anas12091101/Django_ORM_Optimization
cd Django_ORM_Optimization
```

### **2. Set Up a Virtual Environment**
#### **On macOS/Linux:**
```bash
python -m venv venv
source venv/bin/activate
```
#### **On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4. Apply Migrations**
```bash
python manage.py migrate
```

### **5. Populate the Database**
Run the following command to generate sample data:
```bash
python manage.py populate_data
```
This will create sample authors and books for testing different query optimizations.

### **6. Start the Development Server**
```bash
python manage.py runserver
```
Visit `http://127.0.0.1:8000/` to access the application.

---

## **Analyzing Query Performance with Django Silk**
Django Silk is used to analyze query performance. Follow these steps to monitor database queries:

### **1. Access the Silk Dashboard**
After running the server, navigate to:
```
http://127.0.0.1:8000/silk/
```
Here, you can view all executed queries, their execution time, and potential optimizations.

### **2. Run Example Queries**
Try hitting the following endpoints to observe query execution times in Silk:

- **Bad Query:**
  ```
  http://127.0.0.1:8000/bad-query-n-plus-1/
  ```

- **Optimized Query:**
  ```
  http://127.0.0.1:8000/good-query-n-plus-1/
  ```

Check the **Silk Dashboard** to see how different queries perform.

---
