# Invoice Management API

This project provides a simple API to create and update invoices and their details.

## Setup Instructions

1. Clone the repository.
2. Install dependencies(Make sure DEBUG is True for local): `pip install -r requirements.txt`
3. Run migrations: `python manage.py migrate`
4. Start the server: `python manage.py runserver`

## Endpoint Usage

- **POST /api/invoices/**: Create a new invoice.
- **PUT /api/invoices/<id>/**: Update an existing invoice.

### Example Payload:
```json
{
  "invoice_number": "INV001",
  "customer_name": "John Doe",
  "date": "2024-11-12",
  "details": [
    {
      "description": "Product A",
      "quantity": 2,
      "price": 50.00,
      "line_total": 100.00
    }
  ]
}
