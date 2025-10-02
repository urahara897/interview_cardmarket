# Interview Project - Kubernetes & DevOps

A comprehensive DevOps project demonstrating Kubernetes deployment, CI/CD, GitOps, and Infrastructure as Code practices.

## Features

- **Flask Application**: Simple Python web application with environment variable support
- **Docker Containerization**: Multi-stage Dockerfile with security best practices
- **Kubernetes Deployment**: Complete K8s manifests with health checks and resource limits
- **GitHub Actions CI/CD**: Automated testing, building, and deployment
- **Kind Cluster**: Local Kubernetes cluster for development and CI
- **GitOps with ArgoCD**: Continuous deployment using GitOps principles
- **Helm Charts**: Infrastructure as Code with templated Kubernetes manifests
- **Semantic Versioning**: Automated releases with conventional commits
- **Comprehensive Testing**: Unit tests with pytest and coverage reporting

## Requirements Checklist

**Repository forked** - Work in your own forked version  
**No paid services** - All tools are free and open source  
**Kubernetes cluster** - Kind cluster setup in GitHub Actions  
**Docker application** - Custom Flask app with Dockerfile  
**Automated releases** - Semantic versioning with GitHub Actions  
**K8s deployment** - Complete deployment with manifests  
**Infrastructure as Code** - Helm charts for templated deployments  
**GitOps** - ArgoCD workflow for continuous deployment  
**Semantic Versioning** - Automated versioning with conventional commits  
**Changelog** - Keep a Changelog format with automated updates

## Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   GitHub Repo   │───▶│  GitHub Actions  │───▶│   Kind Cluster  │
│                 │    │     CI/CD        │    │   (Kubernetes)  │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                                │
                                ▼
                       ┌──────────────────┐
                       │  GitHub Container│
                       │     Registry     │
                       └──────────────────┘
                                │
                                ▼
                       ┌──────────────────┐
                       │     ArgoCD       │
                       │   (GitOps)       │
                       └──────────────────┘
```

## Local Development

### Prerequisites

- Docker
- kubectl
- Kind (Kubernetes in Docker)
- Helm (optional)

### Quick Start

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/interview.git
   cd interview
   ```

2. **Run locally with Docker**

   ```bash
   cd app
   docker build -t interview-app .
   docker run -p 8080:8080 interview-app
   ```

3. **Deploy to Kind cluster**

   ```bash
   # Create Kind cluster
   kind create cluster --name interview-cluster

   # Build and load image
   docker build -t interview-app:latest ./app
   kind load docker-image interview-app:latest --name interview-cluster

   # Deploy with Helm
   helm install interview-app ./helm/interview-app

   # Access the application
   kubectl port-forward service/interview-app-service 8080:80
   ```

4. **Deploy with Helm**

   ```bash
   # Install Helm chart
   helm install interview-app ./helm/interview-app

   # Upgrade with new values
   helm upgrade interview-app ./helm/interview-app --set replicaCount=3
   ```

## CI/CD Pipeline

The project includes multiple GitHub Actions workflows:

### 1. Main CI/CD Pipeline (`.github/workflows/ci-cd.yml`)

- **Triggers**: Push to main/develop, Pull requests
- **Features**:
  - Python testing with pytest
  - Code linting with flake8
  - Docker image building and pushing to GHCR
  - Kind cluster deployment
  - Application health checks
  - Automated release generation

### 2. GitOps Workflow (`.github/workflows/gitops.yml`)

- **Triggers**: Changes to k8s/ or helm/ directories
- **Features**:
  - ArgoCD installation and configuration
  - Application synchronization
  - GitOps-based deployment

### 3. Semantic Release (`.github/workflows/semantic-release.yml`)

- **Triggers**: Push to main branch
- **Features**:
  - Automated version bumping
  - Changelog generation
  - GitHub releases
  - Helm chart version updates

## Project Structure

```
interview/
├── .github/
│   └── workflows/
│       ├── ci-cd.yml          # Main CI/CD pipeline
│       ├── gitops.yml         # GitOps workflow
│       └── semantic-release.yml # Automated releases
├── app/
│   ├── app.py                 # Flask application
│   ├── Dockerfile             # Container definition
│   ├── requirements.txt       # Python dependencies
│   └── tests/                 # Unit tests
├── helm/
│   └── interview-app/         # Helm chart (GitOps + IaC)
│       ├── Chart.yaml
│       ├── values.yaml
│       └── templates/
│           ├── deployment.yaml
│           ├── service.yaml
│           └── configmap.yaml
├── CHANGELOG.md               # Automated changelog
├── .releaserc.json           # Semantic release config
└── README.md
```

## 🧪 Testing

Run tests locally:

```bash
cd app
pip install -r requirements.txt
pytest tests/ -v --cov=.
```

## Deployment

### GitHub Actions (Recommended)

1. Fork this repository
2. Push changes to trigger the CI/CD pipeline
3. The pipeline will automatically:
   - Run tests
   - Build and push Docker images
   - Deploy to Kind cluster
   - Create releases (if on main branch)

### Manual Deployment

**Using Helm**:

```bash
helm install interview-app ./helm/interview-app
```

## 🔧 Configuration

### Environment Variables

- `APP_MESSAGE`: Custom message to display (default: "Hello, DevopsCardmarket Interview!")
- `APP_PORT`: Port to run the application (default: 8080)

### Helm Values

Key configuration options in `helm/interview-app/values.yaml`:

```yaml
replicaCount: 2
image:
  repository: ghcr.io/your-username/interview-app
  tag: "latest"
service:
  type: NodePort
  port: 80
  nodePort: 30080
resources:
  limits:
    cpu: 100m
    memory: 128Mi
```

## 📊 Monitoring & Observability

The application includes:

- **Health Checks**: Liveness and readiness probes
- **Resource Limits**: CPU and memory constraints
- **Logging**: Structured logging for debugging
- **Metrics**: Basic application metrics

## Security

- Non-root container user
- Read-only root filesystem
- Resource limits and requests
- Security context configurations
- Container image scanning in CI

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes following conventional commit format
4. Add tests for new functionality
5. Commit your changes (`git commit -m 'feat: add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

---

## Original Interview Tasks

### k8s deployment

1. ✅ Set up a kubernetes cluster ie. kind, minikube, k3s etc. (Using Kind in GitHub Actions)
2. ✅ Build and release an app. This application should have a dockerfile created by you and it should be built by you. (Flask app with automated releases)
3. ✅ Create a deployment of this app. (Complete K8s manifests with health checks)

**Extras completed:**

- IaC (Helm charts)
- GitOps (ArgoCD workflow)
- semver (Semantic versioning with automated releases)
- changelog (Keep a Changelog format)

### review

- please review [shellscript](shell/script.sh)
- please review [deployment](k8s/nginx.yaml)
- extras: proper explanation
