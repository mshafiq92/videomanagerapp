# Video Dashboard Application - Complete Project Documentation

## �  Security Notice
**IMPORTANT**: This documentation contains placeholder credentials marked with `<>` brackets. Never commit actual credentials to version control. Always replace placeholders with your actual values in local configuration files that are excluded by `.gitignore`.

## 📋 Table of Contents

1. [Project Overview](#project-overview)
2. [Architecture](#architecture)
3. [Technology Stack](#technology-stack)
4. [Project Structure](#project-structure)
5. [Features](#features)
6. [Installation & Setup](#installation--setup)
7. [Docker Implementation](#docker-implementation)
8. [Kubernetes Deployment](#kubernetes-deployment)
9. [API Endpoints](#api-endpoints)
10. [Database Schema](#database-schema)
11. [Configuration](#configuration)
12. [Troubleshooting](#troubleshooting)
13. [Development Workflow](#development-workflow)
14. [Production Considerations](#production-considerations)

---

## 🎯 Project Overview

The Video Dashboard Application is a modern web-based video management system built with FastAPI and MongoDB Atlas. It provides a clean, responsive interface for managing video content with full CRUD (Create, Read, Update, Delete) operations.

### Key Achievements

- ✅ **FastAPI Backend** with robust error handling and validation
- ✅ **MongoDB Atlas Integration** with connection health checks
- ✅ **Modern Responsive UI** with professional styling
- ✅ **Docker Containerization** for consistent deployment
- ✅ **Kubernetes Orchestration** with Minikube support
- ✅ **Production-Ready** with proper logging and monitoring

---

## 🏗️ Architecture

### System Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Web Browser   │────│   FastAPI App   │────│  MongoDB Atlas  │
│   (Frontend)    │    │   (Backend)     │    │   (Database)    │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

### Deployment Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Kubernetes Cluster                       │
│  ┌─────────────────┐  ┌─────────────────┐                  │
│  │   Pod 1         │  │   Pod 2         │                  │
│  │ FastAPI App     │  │ FastAPI App     │                  │
│  └─────────────────┘  └─────────────────┘                  │
│           │                     │                          │
│  ┌─────────────────────────────────────────┐               │
│  │         Load Balancer Service           │               │
│  └─────────────────────────────────────────┘               │
└─────────────────────────────────────────────────────────────┘
                           │
                  ┌─────────────────┐
                  │  MongoDB Atlas  │
                  │   (External)    │
                  └─────────────────┘
```

---

## 🛠️ Technology Stack

### Backend

- **FastAPI** 0.104.1 - Modern Python web framework
- **Uvicorn** - ASGI server for FastAPI
- **Pydantic** 2.5.0 - Data validation and serialization
- **PyMongo** 4.6.0 - MongoDB driver for Python
- **Motor** - Async MongoDB driver
- **Python-multipart** 0.0.6 - Form data handling

### Database

- **MongoDB Atlas** - Cloud-hosted MongoDB database
- **AsyncIOMotorClient** - Async database operations

### Frontend

- **Jinja2 Templates** - Server-side templating
- **HTML5** - Modern markup
- **CSS3** - Responsive styling with modern design
- **JavaScript** - Client-side interactions

### DevOps & Deployment

- **Docker** - Containerization
- **Docker Compose** - Multi-container orchestration
- **Kubernetes** - Container orchestration
- **Minikube** - Local Kubernetes development

### Development Tools

- **Git** - Version control
- **Python Virtual Environment** - Dependency isolation

---

## 📁 Project Structure

```
VideoManagerApp/
├── app/                          # Application source code
│   ├── __init__.py
│   ├── main.py                   # FastAPI application entry point
│   ├── dbConnection.py           # Database connection and health checks
│   ├── routes/
│   │   └── video_routes.py       # Video CRUD API routes
│   ├── templates/                # Jinja2 HTML templates
│   │   ├── index.html           # Dashboard homepage
│   │   ├── add_video.html       # Add video form
│   │   ├── list_videos.html     # Video listing page
│   │   ├── update_video.html    # Update video form
│   │   └── delete_video.html    # Delete video confirmation
│   └── static/
│       └── css/
│           └── style.css        # Modern responsive styling
├── Kubernetes/                   # Kubernetes deployment files
│   ├── secrets.yaml             # Sensitive configuration data
│   ├── configmap.yaml           # Application configuration
│   ├── appdeployment.yaml       # Application deployment & service
│   └── mongodbdeployment.yaml   # MongoDB deployment (optional)
├── .kiro/                       # Kiro IDE specifications
│   └── specs/
│       └── video-dashboard-fixes/
│           ├── requirements.md   # Project requirements
│           ├── design.md        # System design document
│           └── tasks.md         # Implementation tasks
├── Dockerfile                   # Docker image definition
├── docker-compose.yaml          # Docker Compose configuration
├── requirements.txt             # Python dependencies
├── .env                        # Environment variables
├── .gitignore                  # Git ignore rules
├── README.md                   # Basic project information
└── PROJECT_DOCUMENTATION.md    # This comprehensive documentation
```

---

## ✨ Features

### Core Functionality

- **📹 Video Management**: Complete CRUD operations for video records
- **🔍 Video Listing**: Display all videos with pagination support
- **➕ Add Videos**: Form-based video creation with validation
- **✏️ Update Videos**: Edit existing video information
- **🗑️ Delete Videos**: Safe video removal with confirmation
- **🏠 Dashboard**: Clean overview of the application

### Technical Features

- **🔒 Input Validation**: Pydantic models with comprehensive validation
- **🛡️ Error Handling**: Robust error handling with user-friendly messages
- **📊 Health Checks**: Database connection monitoring
- **🔄 Async Operations**: Non-blocking database operations
- **📱 Responsive Design**: Mobile-friendly interface
- **🎨 Modern UI**: Professional styling with CSS Grid and Flexbox
- **🔧 Configuration Management**: Environment-based configuration

### DevOps Features

- **🐳 Docker Support**: Complete containerization
- **☸️ Kubernetes Ready**: Production-ready orchestration
- **📈 Scalability**: Horizontal pod autoscaling
- **🔍 Monitoring**: Health checks and logging
- **🔄 CI/CD Ready**: Structured for automated deployments

---

## 🚀 Installation & Setup

### Prerequisites

- Python 3.12+
- Docker & Docker Compose
- Kubernetes (Minikube for local development)
- MongoDB Atlas account
- Git

### Local Development Setup

1. **Clone the Repository**

   ```bash
   git clone <repository-url>
   cd VideoManagerApp
   ```

2. **Create Virtual Environment**

   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Linux/Mac
   source venv/bin/activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment**

   ```bash
   # Create .env file with your actual MongoDB Atlas connection string
   # Replace <USERNAME>, <PASSWORD>, <CLUSTER>, and <DATABASE> with your actual values
   echo 'MONGO_URI="mongodb+srv://<USERNAME>:<PASSWORD>@<CLUSTER>.mongodb.net/<DATABASE>?retryWrites=true&w=majority"' > .env
   ```
   
   **⚠️ Security Note**: Never commit the `.env` file to version control. It's already excluded in `.gitignore`.

5. **Run the Application**

   ```bash
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

6. **Access the Application**
   - Open browser: `http://localhost:8000`

---

## 🐳 Docker Implementation

### Docker Architecture

The application uses a minimalistic Docker setup optimized for development and production use.

### Dockerfile Explanation

```dockerfile
# Use lightweight Python 3.12 base image
FROM python:3.12-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements first (for better Docker layer caching)
COPY requirements.txt .
# Install Python dependencies
RUN pip install -r requirements.txt

# Copy application code
COPY app/ ./app/
# Copy environment variables file
COPY .env .

# Document that app uses port 8000
EXPOSE 8000

# Start FastAPI app with uvicorn server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Docker Compose Configuration

```yaml
# Docker Compose file format version
version: "3.8"

services:
  # Main FastAPI application service
  video-manager:
    # Build image from Dockerfile in current directory
    build: .
    # Map host port 8000 to container port 8000
    ports:
      - "8000:8000"
    # Pass MongoDB Atlas connection string from .env file
    environment:
      - MONGO_URI=${MONGO_URI}
    # Mount local app folder for live code reload during development
    volumes:
      - ./app:/app/app
```

### Docker Commands

**Build and Run:**

```bash
# Build and start the container
docker-compose up --build

# Run in background
docker-compose up -d

# View logs
docker-compose logs -f video-manager

# Stop containers
docker-compose down
```

**Development Workflow:**

```bash
# Rebuild after dependency changes
docker-compose up --build

# View container status
docker-compose ps

# Execute commands in running container
docker-compose exec video-manager bash
```

---

## ☸️ Kubernetes Deployment

### Kubernetes Architecture

The application is deployed using Kubernetes with the following components:

- **Deployment**: Manages application pods with 2 replicas
- **Service**: Exposes the application via NodePort
- **ConfigMap**: Stores non-sensitive configuration
- **Secret**: Stores sensitive data (MongoDB URI)
- **HPA**: Horizontal Pod Autoscaler for scaling

### Configuration Files

#### 1. Secrets (secrets.yaml)

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: video-dashboard-secrets
  namespace: default
type: Opaque
stringData:
  # MongoDB Atlas connection string (plain text - Kubernetes will encode automatically)
  mongo-uri: "mongodb+srv://<USERNAME>:<PASSWORD>@<CLUSTER>.mongodb.net/<DATABASE>?retryWrites=true&w=majority"
  # MongoDB credentials for local MongoDB (if using local instead of Atlas)
  mongo-username: "<LOCAL_MONGO_USERNAME>"
  mongo-password: "<LOCAL_MONGO_PASSWORD>"
```

#### 2. ConfigMap (configmap.yaml)

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: video-dashboard-config
  namespace: default
data:
  app-name: "video-dashboard"
  database-name: "ytmanager"
  log-level: "INFO"
  environment: "development"
  server-host: "0.0.0.0"
  server-port: "8000"
```

#### 3. Application Deployment (appdeployment.yaml)

- **Deployment**: 2 replicas with health checks
- **Service**: NodePort for external access
- **HPA**: Auto-scaling based on CPU/memory usage

### Deployment Commands

**Minikube Setup:**

```bash
# Start Minikube
minikube start

# Build Docker image in Minikube
eval $(minikube docker-env)
docker build -t video-dashboard:latest .
```

**Deploy to Kubernetes:**

**⚠️ Security Setup First:**
```bash
# 1. Create your actual secrets.yaml from the template
# Replace all <PLACEHOLDER> values with your actual credentials
# 2. Ensure secrets.yaml is in .gitignore (already configured)
# 3. Never commit actual credentials to version control
```

```bash
# Apply configurations
kubectl apply -f Kubernetes/secrets.yaml
kubectl apply -f Kubernetes/configmap.yaml
kubectl apply -f Kubernetes/appdeployment.yaml

# Check deployment status
kubectl get pods
kubectl get services
kubectl get deployments
```

**Access Application:**

```bash
# Get service URL
minikube service video-dashboard-service --url

# Or use port forwarding
kubectl port-forward service/video-dashboard-service 8000:8000
```

**Monitoring & Troubleshooting:**

```bash
# View pod logs
kubectl logs -f <pod-name>

# Describe pod for details
kubectl describe pod <pod-name>

# Check events
kubectl get events --sort-by=.metadata.creationTimestamp
```

**Cleanup:**

```bash
# Remove deployments
kubectl delete -f Kubernetes/

# Stop Minikube
minikube stop

# Delete Minikube cluster
minikube delete
```

---

## 🔌 API Endpoints

### Web Routes (HTML Templates)

| Method | Endpoint | Description | Template |
|--------|----------|-------------|----------|
| GET | `/` | Dashboard homepage | index.html |
| GET | `/videos` | List all videos | list_videos.html |
| GET | `/videos/add` | Add video form | add_video.html |
| POST | `/videos/add` | Create new video | - |
| GET | `/videos/update` | Update video form | update_video.html |
| POST | `/videos/update` | Update existing video | - |
| GET | `/videos/delete` | Delete video form | delete_video.html |
| POST | `/videos/delete` | Delete video | - |

### Request/Response Examples

**Add Video (POST /videos/add):**

```html
<!-- Form Data -->
<form method="post" action="/videos/add">
    <input name="title" type="text" required>
    <input name="description" type="text" required>
    <input name="time" type="text" required>
    <input name="url" type="url" required>
</form>
```

**Update Video (POST /videos/update):**

```html
<!-- Form Data -->
<form method="post" action="/videos/update">
    <input name="id" type="text" required>
    <input name="title" type="text">
    <input name="description" type="text">
    <input name="time" type="text">
    <input name="url" type="url">
</form>
```

---

## 🗄️ Database Schema

### MongoDB Collection: `videos`

**Document Structure:**

```json
{
  "_id": "ObjectId('...')",
  "title": "Video Title",
  "description": "Video description text",
  "time": "Duration or timestamp",
  "url": "https://video-url.com",
  "created_at": "2024-01-01T00:00:00.000Z",
  "updated_at": "2024-01-01T00:00:00.000Z"
}
```

**Field Validation:**

- **title**: Required, max 200 characters, trimmed
- **description**: Required, max 1000 characters, trimmed
- **time**: Required, string format, trimmed
- **url**: Required, valid HTTP/HTTPS URL format
- **created_at**: Auto-generated timestamp
- **updated_at**: Auto-updated on modifications

**Indexes:**

- Primary: `_id` (automatic)
- Recommended: `title` (for search optimization)
- Recommended: `created_at` (for sorting)

---

## ⚙️ Configuration

### Environment Variables (.env)

```bash
# MongoDB Atlas Connection
MONGO_URI/connection ="mongodb+srv://<USERNAME>:<PASSWORD>@<CLUSTER>.mongodb.net/<DATABASE>?retryWrites=true&w=majority"

# Optional: Application Settings
LOG_LEVEL="INFO"
ENVIRONMENT="development"
```

### Application Configuration

- **Host**: 0.0.0.0 (all interfaces)
- **Port**: 8000
- **Database**: ytmanager
- **Connection Pool**: Async with retry logic
- **Timeout**: 10 seconds for database operations

### Docker Configuration

- **Base Image**: python:3.12-slim
- **Working Directory**: /app
- **Exposed Port**: 8000
- **Volume Mount**: ./app:/app/app (development)

### Kubernetes Configuration

- **Replicas**: 2 (default)
- **Auto-scaling**: 2-5 pods based on CPU/memory
- **Service Type**: NodePort
- **Health Checks**: HTTP probes on port 8000
- **Resource Limits**: 256Mi memory, 200m CPU

---

## 🔧 Troubleshooting

### Common Issues & Solutions

#### 1. Database Connection Issues

**Problem**: Cannot connect to MongoDB Atlas

```
pymongo.errors.ServerSelectionTimeoutError
```

**Solutions:**

- Verify MongoDB Atlas connection string in `.env`
- Check IP whitelist in MongoDB Atlas (allow 0.0.0.0/0 for development)
- Ensure correct username/password
- Test connection with MongoDB Compass

#### 2. Docker Build Issues

**Problem**: Docker build fails

```
ERROR: Could not find a version that satisfies the requirement
```

**Solutions:**

- Update `requirements.txt` with correct versions
- Clear Docker cache: `docker system prune -a`
- Check Python version compatibility
- Verify internet connection for package downloads

#### 3. Kubernetes Pod Issues

**Problem**: Pods not starting

```
kubectl get pods
NAME                                     READY   STATUS    RESTARTS   AGE
video-dashboard-deployment-xxx           0/1     Pending   0          5m
```

**Solutions:**

- Check resource availability: `kubectl describe node`
- Verify image exists: `docker images | grep video-dashboard`
- Check pod logs: `kubectl logs <pod-name>`
- Verify secrets and configmaps: `kubectl get secrets,configmaps`

#### 4. Form Submission Issues

**Problem**: Forms not working, multipart errors

```

RuntimeError: Form data requires "python-multipart" to be installed
```

**Solutions:**

- Ensure `python-multipart==0.0.6` in requirements.txt
- Rebuild Docker image after adding dependency
- Verify form `enctype="multipart/form-data"` in HTML

#### 5. Port Access Issues

**Problem**: Cannot access application on localhost:8000

**Solutions:**

- Check if port is occupied: `netstat -an | findstr :8000`
- Verify Docker port mapping: `docker-compose ps`
- For Kubernetes: Use `minikube service video-dashboard-service --url`
- Check firewall settings

### Debugging Commands

**Docker Debugging:**

```bash

# Check container logs
docker-compose logs -f video-manager

# Execute shell in container
docker-compose exec video-manager bash

# Check container status
docker-compose ps

# Rebuild from scratch
docker-compose down
docker-compose up --build --force-recreate
```

**Kubernetes Debugging:**

```bash
# Check all resources
kubectl get all

# Describe problematic pod
kubectl describe pod <pod-name>

# Check events
kubectl get events --sort-by=.metadata.creationTimestamp

# Port forward for testing
kubectl port-forward <pod-name> 8000:8000

# Check logs
kubectl logs -f <pod-name>
```

---

## 🔄 Development Workflow

### Local Development

1. **Setup Environment**

   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   pip install -r requirements.txt
   ```

2. **Run Development Server**

   ```bash
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

3. **Make Changes**
   - Edit code in `app/` directory
   - Auto-reload handles server restart
   - Test changes at `http://localhost:8000`

### Docker Development

1. **Build and Run**

   ```bash
   docker-compose up --build
   ```

2. **Live Development**
   - Volume mount enables live code changes
   - No container restart needed for code changes
   - Restart needed for dependency changes

3. **Testing**

   ```bash

   # Test endpoints
   curl http://localhost:8000/
   curl http://localhost:8000/videos
   ```

### Kubernetes Development

1. **Build Image**

   ```bash
   eval $(minikube docker-env)
   docker build -t video-dashboard:latest .
   ```

2. **Deploy Changes**

   ```bash
   kubectl apply -f Kubernetes/
   kubectl rollout restart deployment/video-dashboard-deployment
   ```

3. **Monitor Deployment**

   ```bash
   kubectl get pods -w
   kubectl logs -f deployment/video-dashboard-deployment
   ```

### Code Quality

- **Validation**: Pydantic models ensure data integrity
- **Error Handling**: Comprehensive try-catch blocks
- **Logging**: Structured logging for debugging
- **Documentation**: Inline comments and docstrings

---

## 🚀 Production Considerations

### Security

- **Environment Variables**: Never commit `.env` to version control
- **Secrets Management**: Use Kubernetes secrets or external secret managers
- **Database Security**: Enable MongoDB authentication and SSL
- **Network Security**: Use HTTPS in production
- **Input Validation**: Pydantic models prevent injection attacks

### Performance

- **Database Indexing**: Add indexes for frequently queried fields
- **Connection Pooling**: Configure appropriate pool sizes
- **CDN**: Use CDN for static assets
- **Load Balancing**: Kubernetes service handles load distribution

### Monitoring

- **Health Checks**: Kubernetes liveness and readiness probes
- **Logging**: Centralized logging with ELK stack
- **Metrics**: Prometheus and Grafana for monitoring
- **Alerting**: Set up alerts for critical failures
- **APM**: Application Performance Monitoring tools

### Scalability

- **Horizontal Scaling**: Kubernetes HPA for automatic scaling
- **Database Scaling**: MongoDB Atlas auto-scaling
- **Resource Limits**: Proper CPU and memory limits
- **Stateless Design**: Application is stateless for easy scaling

### Deployment

- **CI/CD Pipeline**: Automated testing and deployment
- **Blue-Green Deployment**: Zero-downtime deployments
- **Environment Separation**: Dev, staging, and production environments

### Backup & Recovery

- **Database Backups**: MongoDB Atlas automated backups
- **Configuration Backups**: Version control for all configs
- **Disaster Recovery**: Multi-region deployment strategy
- **Data Retention**: Implement data retention policies

---

## 📚 Additional Resources

### Documentation

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [MongoDB Atlas Documentation](https://docs.atlas.mongodb.com/)
- [Docker Documentation](https://docs.docker.com/)
- [Kubernetes Documentation](https://kubernetes.io/docs/)
- [Minikube Documentation](https://minikube.sigs.k8s.io/docs/)

### Tools & Extensions

- **MongoDB Compass**: GUI for MongoDB
- **Postman**: API testing
- **kubectl**: Kubernetes CLI
- **Docker Desktop**: Docker GUI
- **VS Code Extensions**: Python, Docker, Kubernetes

### Best Practices

- **12-Factor App**: Follow 12-factor methodology
- **RESTful APIs**: Follow REST principles
- **Security**: OWASP security guidelines
- **Testing**: Unit and integration testing
- **Documentation**: Keep documentation updated

---

## 🎉 Project Success Summary

This Video Dashboard Application successfully demonstrates:

✅ **Modern Web Development**: FastAPI + MongoDB Atlas integration
✅ **Containerization**: Docker and Docker Compose implementation
✅ **Orchestration**: Kubernetes deployment with Minikube
✅ **Scalability**: Auto-scaling and load balancing
✅ **Production Ready**: Health checks, monitoring, and error handling
✅ **Developer Friendly**: Live reload, comprehensive documentation
✅ **Best Practices**: Security, validation, and proper architecture

The project showcases a complete DevOps pipeline from development to deployment, making it an excellent reference for modern web application development and deployment practices.

---

**Project Completed Successfully** 🚀
*Documentation Version: 1.0* .
