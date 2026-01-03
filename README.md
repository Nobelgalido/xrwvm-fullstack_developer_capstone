# Full-Stack Car Dealership Web Application

A comprehensive dealership management platform built as the capstone project for the IBM Full Stack Software Developer Professional Certificate. This application demonstrates modern full-stack development practices with microservices architecture, containerization, and cloud deployment.

## 🚀 Features

- **User Authentication & Management**: Secure registration and login system
- **Dealership Directory**: Browse and search dealerships by state/location
- **Review System**: Submit and view dealership reviews with sentiment analysis
- **Car Inventory Search**: Advanced filtering by make, model, year, mileage, and price
- **Real-time Sentiment Analysis**: Automated review sentiment classification using IBM Watson NLU
- **Responsive Design**: Tactical dark-themed UI optimized for all devices

## 🛠️ Tech Stack

### Frontend
- **React.js** - Component-based UI with hooks
- **JavaScript ES6+** - Modern JavaScript features
- **CSS3** - Custom tactical dark theme styling

### Backend
- **Django** - Main application server and REST API
- **Node.js + Express.js** - Microservices for dealerships and car inventory
- **Python 3.12** - Backend logic and API integration

### Databases
- **MongoDB** - NoSQL database for dealerships, reviews, and car inventory
- **SQLite** - Relational database for Django models

### DevOps & Cloud
- **Docker** - Application containerization
- **Docker Compose** - Multi-container orchestration
- **Kubernetes** - Container orchestration and deployment
- **IBM Cloud Code Engine** - Serverless sentiment analysis microservice
- **GitHub Actions** - CI/CD pipeline with automated linting

### APIs & Services
- **IBM Watson NLU** - Natural Language Understanding for sentiment analysis
- **REST APIs** - Custom endpoints for all services

## 📋 Architecture

The application follows a microservices architecture:
```
├── Django Backend (Port 8000)
│   ├── User Management
│   ├── API Gateway
│   └── Frontend Serving
├── Dealership Service (Port 3030)
│   ├── Express.js + MongoDB
│   └── Dealer & Review Management
├── Car Inventory Service (Port 3050)
│   ├── Express.js + MongoDB
│   └── Advanced Search & Filtering
└── Sentiment Analysis Service
    └── IBM Code Engine (Serverless)
```

## 🚦 Getting Started

### Prerequisites
- Python 3.12+
- Node.js 18+
- Docker & Docker Compose
- IBM Cloud Account (for sentiment analysis)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/Nobelgalido/xrwvm-fullstack_developer_capstone.git
cd xrwvm-fullstack_developer_capstone
```

2. **Set up environment variables**
```bash
cd server/djangoapp
cp .env.example .env
# Edit .env with your configuration
```

3. **Start the dealership microservice**
```bash
cd server/database
docker-compose up -d
```

4. **Start the car inventory microservice**
```bash
cd server/carsInventory
docker-compose up -d
```

5. **Install Python dependencies and run Django**
```bash
cd server
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

6. **Build the React frontend**
```bash
cd server/frontend
npm install
npm run build
```

7. **Access the application**
```
http://localhost:8000
```

## 🧪 Testing

- **Linting**: Automated via GitHub Actions
  - Python: `flake8`
  - JavaScript: `jshint`

- **API Endpoints**: Test with curl or Postman
```bash
# Dealerships
curl http://localhost:3030/fetchDealers

# Car Inventory
curl http://localhost:3050/cars/1

# Django API
curl http://localhost:8000/djangoapp/get_dealers
```

## 📦 Deployment

### Docker Deployment
```bash
# Build Django image
cd server
docker build -t dealership-app .

# Deploy to Kubernetes
kubectl apply -f deployment.yaml
```

### Kubernetes Configuration
- Deployment manifests in `server/deployment.yaml`
- Configured for IBM Cloud Kubernetes Service
- Persistent volumes for MongoDB data

## 🎨 Key Features Implemented

### Frontend Enhancements
- ✅ Searchable state input (replaced dropdown)
- ✅ Tactical dark theme with matrix green accents
- ✅ Centered, readable review panels
- ✅ Dynamic car inventory filtering

### Backend Enhancements
- ✅ Car inventory microservice with MongoDB
- ✅ Advanced search endpoints (make, model, year, mileage, price)
- ✅ Django proxy services for API integration
- ✅ Sentiment analysis integration

### DevOps
- ✅ Multi-container Docker setup
- ✅ Kubernetes orchestration
- ✅ CI/CD pipeline with GitHub Actions
- ✅ Automated code quality checks

## 📸 Screenshots

*Add your deployment screenshots here*

## 🤝 Contributing

This is a capstone project for educational purposes. Feel free to fork and adapt for your own learning!

## 📄 License

This project is part of the IBM Full Stack Software Developer Professional Certificate program.

## 👤 Author

**Alfred Galido**
- GitHub: [@Nobelgalido](https://github.com/Nobelgalido)
- Location: Quezon City, Philippines
- Education: Computer Science Graduate (May 2025)

## 🎓 Certifications

- IBM Full Stack Software Developer Professional Certificate
- AWS Cloud Practitioner (In Progress)

## 🙏 Acknowledgments

- IBM Skills Network for the comprehensive curriculum
- Anthropic's Claude for development assistance
- The open-source community for amazing tools and libraries

---

**Built with ❤️ as part of my journey to becoming a full-stack developer**
