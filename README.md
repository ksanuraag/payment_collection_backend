# Loan Payment Collection API

A Django REST API for managing personal loan payments.
This backend allows customers to view loan details, make EMI payments, and check payment history.

---

## Tech Stack

* **Backend:** Django, Django REST Framework
* **Database:** PostgreSQL
* **Environment Management:** python-decouple
* **CORS:** django-cors-headers

---

## Features

* Retrieve loan details for all customers
* Make EMI payments
* Track payment history
* Prevent duplicate EMI payments
* Automatically update EMI status and reduce loan tenure after payment

---

## API Endpoints

### Get Customers

Retrieve loan details of all customers.

```
GET /bank/customer/
```

Response Example:

```json
{
  "message": "customer fetched successfully",
  "data": [
    {
      "account_no": "1234567890",
      "issue_date": "2024-01-01",
      "interest_rate": "8.50",
      "tenure": 12,
      "emi_due": "5000.00",
      "emi_status": "PENDING"
    }
  ]
}
```

---

### Make Payment

Submit EMI payment.

```
POST /bank/payments/
```

Request Body:

```json
{
  "account_no": "1234567890",
  "amount": 5000
}
```

Response:

```json
{
  "message": "Payment successful",
  "data": {
    "payment_amount": "5000.00",
    "status": "SUCCESS"
  }
}
```

---

### Payment History

Retrieve payment history for a specific account.

```
GET /bank/payments/<account_no>/
```

Example:

```
GET /bank/payments/1234567890/
```

---

## Installation

### 1. Clone the Repository

```
git clone https://github.com/yourusername/loan-payment-backend.git
cd loan-payment-backend
```

---

### 2. Create Virtual Environment

```
python -m venv venv
source venv/bin/activate
```

---

### 3. Install Dependencies

```
pip install -r requirements.txt
```

---

### 4. Configure Environment Variables

Create a `.env` file in the project root:

```
DJANGO_SECRET_KEY=your-secret-key

DB_NAME=loan_db
DB_USER=postgres
DB_PASSWORD=yourpassword
DB_HOST=localhost
DB_PORT=5432
```

---

### 5. Run Migrations

```
python manage.py migrate
```

---

### 6. Run Server

```
python manage.py runserver
```

Server will start at:

```
http://127.0.0.1:8000/
```

---

## Project Structure

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
└── .gitignore
```

---

## Notes

* Customers can be created through **Django Admin Panel**
* Payment API validates EMI amount before processing
* Tenure decreases automatically after successful payment

---

## Author

Anuraag K S
