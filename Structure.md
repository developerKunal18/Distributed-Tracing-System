🧠 Why This Is Important

Imagine a request passing through multiple services:
Client
   ↓
API Gateway
   ↓
User Service
   ↓
Order Service
   ↓
Payment Service

If one service is slow, which one?

Distributed tracing answers this.

Used By:
Jaeger
Zipkin
OpenTelemetry
AWS X-Ray

🛠 Tech Stack
Python
Flask
UUID
datetime

📂 Project Structure
distributed-tracing-system/
│
├── app.py
└── README.md
