# Loan Payment Collection API

A Django REST API for managing personal loan EMI payments.
The system allows customers to view loan details, pay EMIs, and track payment history.

This backend is designed to integrate with a React frontend for the Loan Payment Collection App.

---

# Tech Stack

Backend

* Django
* Django REST Framework

Database

* PostgreSQL

Admin Interface

* django-daisy (Modern Django Admin UI)

Configuration

* python-decouple (.env)

Other Tools

* django-cors-headers

---

# Features

* Retrieve loan details of customers
* Make EMI payments
* Track payment history
* Prevent invalid payment amounts
* Automatically reduce loan tenure after each EMI payment
* Track total loan amount and total paid amount
* Loan marked **PAID when total loan amount is fully paid**
* Styled admin panel using **django-daisy**

---

# Loan Payment Logic

Example Loan

Total Loan Amount: 2000
EMI Amount: 500
Tenure: 4 months

Payment Flow

| EMI Payment | Amount | Remaining Tenure | Total Paid | Status  |
| ----------- | ------ | ---------------- | ---------- | ------- |
| Start       | 0      | 4                | 0          | PENDING |
| EMI 1       | 500    | 3                | 500        | PENDING |
| EMI 2       | 500    | 2                | 1000       | PENDING |
| EMI 3       | 500    | 1                | 1500       | PENDING |
| EMI 4       | 500    | 0                | 2000       | PAID    |

The loan becomes **PAID only when the total loan amount is fully paid**.

---

# API Endpoints

## Get Customers

Retrieve loan details of all customers.

GET

```
/bank/customer/
```

Response Example

```json
{
  "message": "customer fetched successfully",
  "data": [
    {
      "account_no": "1234567890",
      "issue_date": "2024-01-01",
      "interest_rate": "7.00",
      "tenure": 4,
      "emi_due": "500.00",
      "total_loan_amount": "2000.00",
      "total_paid_amount": "0.00",
      "emi_status": "PENDING"
    }
  ]
}
```

---

## Make EMI Payment

Submit EMI payment.

POST

```
/bank/payments/
```

Request Body

```json
{
 "account_no": "1234567890",
 "amount": 500
}
```

Response

```json
{
 "message": "Payment successful",
 "data": {
  "payment_amount": "500.00",
  "status": "SUCCESS"
 }
}
```

Behavior

* Payment record created
* Total paid amount updated
* Tenure reduced by 1
* Loan marked **PAID when total amount is reached**

---

## Payment History

Retrieve payment history for a specific customer.

GET

```
/bank/payments/<account_no>/
```

Example

```
/bank/payments/1234567890/
```

Response Example

```json
{
 "message": "payment history fetched",
 "data": [
  {
   "payment_amount": "500.00",
   "payment_date": "25-03-2026 11:45",
   "status": "SUCCESS"
  }
 ]
}
```

---

# Installation

## Clone Repository

```
git clone https://github.com/ksanuraag/loan-payment-backend.git
cd loan-payment-backend
```

---

## Create Virtual Environment

```
python -m venv venv
source venv/bin/activate
```

---

## Install Dependencies

```
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file in the project root.

Example

```
DJANGO_SECRET_KEY=your_secret_key

DB_NAME=loan_db
DB_USER=postgres
DB_PASSWORD=yourpassword
DB_HOST=localhost
DB_PORT=5432
```

---

# Database Setup

Run migrations

```
python manage.py migrate
```

Create superuser

```
python manage.py createsuperuser
```

---

# Run Server

```
python manage.py runserver
```

Server runs at

```
http://127.0.0.1:8000/
```

---

# Django Admin (django-daisy)

Admin panel is enhanced using **django-daisy** for a cleaner interface.

Access admin panel

```
http://127.0.0.1:8000/admin
```

Admin allows you to

* Create customers
* Manage loan data
* View payment records
* Monitor EMI payments

---

# Project Structure

```
loan-payment-backend
│
├── loan_app
│   ├── models.py
│   ├── views.py
│   ├── serializer.py
│   ├── urls.py
│
├── project
│   ├── settings.py
│   ├── urls.py
│
├── manage.py
├── requirements.txt
├── .env
└── .gitignore
```

---

# Frontend Repository

The React frontend for this API is maintained in a separate repository.

Frontend features

* Display loan details
* Pay EMI
* View payment history
* API integration with Django backend

---

# Author

Anuraag K S
