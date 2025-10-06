# DevOps Interview Project

This project demonstrates how to build a complete DevOps pipeline from scratch. It shows you how to take a simple web application and deploy it to Kubernetes using modern tools and practices. Think of it as a practical example of how real-world applications get built, tested, and deployed automatically.

## What's Inside

- **A Simple Web App**: A Python Flask application that says "Hello" - nothing fancy, just something to deploy
- **Docker Container**: The app is packaged in a secure Docker container that runs safely
- **Kubernetes Deployment**: The app runs on Kubernetes with proper health checks and resource limits
- **Automated Testing**: Every time you make a change, tests run automatically to make sure nothing breaks
- **Automatic Deployment**: When tests pass, the app gets deployed to a test environment automatically
- **Version Management**: The system automatically creates new versions and keeps track of what changed
- **Infrastructure as Code**: All the deployment configuration is stored in files, not manual clicks

## What This Project Covers

This project meets all the typical interview requirements:

- **Kubernetes Setup**: Uses Kind (Kubernetes in Docker) - no expensive cloud services needed
- **Custom Application**: Built a Flask web app from scratch with a proper Dockerfile
- **Automated Everything**: Tests, builds, and deployments happen automatically when you push code
- **Smart Versioning**: The system figures out what version number to use based on your commit messages
- **Infrastructure as Code**: All the Kubernetes configuration is stored in files you can version control
- **Complete Documentation**: Everything is documented so you can understand what's happening

## How It All Works Together

Here's the simple flow of what happens when you make a change:

```
1. You push code to GitHub
   ↓
2. GitHub Actions runs tests automatically
   ↓
3. If tests pass, it builds a Docker container
   ↓
4. It starts a local Kubernetes cluster (using Kind)
   ↓
5. It deploys your app to the test environment
   ↓
6. It creates a new version and updates documentation
```

The beauty is that you don't have to do any of this manually - it all happens automatically when you push code!

## Getting Started

### What You Need

- Docker (to run containers)
- kubectl (to talk to Kubernetes)
- Kind (to run Kubernetes locally)
- Helm (to manage deployments)

### Try It Yourself

1. **Get the code**

   ```bash
   git clone https://github.com/your-username/interview.git
   cd interview
   ```

2. **Run the app locally**

   ```bash
   cd app
   docker build -t interview-app .
   docker run -p 8080:8080 interview-app
   ```

   Then visit http://localhost:8080 in your browser

3. **Deploy to Kubernetes (the fancy way)**

   ```bash
   # Start a local Kubernetes cluster
   kind create cluster --name interview-cluster

   # Build and load the app into Kubernetes
   docker build -t interview-app:latest ./app
   kind load docker-image interview-app:latest --name interview-cluster

   # Deploy using Helm
   helm install interview-app ./helm/interview-app

   # Make it accessible from your browser
   kubectl port-forward service/interview-app 8080:80
   ```

## The Automation Magic

When you push code to GitHub, here's what happens automatically:

### 1. Testing Phase

- Runs your Python tests to make sure nothing broke
- Checks code quality with linting tools
- If anything fails, it stops here and tells you what's wrong

### 2. Building Phase

- Creates a Docker container with your app inside
- Makes sure the container is secure and follows best practices
- Prepares it for deployment

### 3. Deployment Phase

- Starts up a local Kubernetes cluster (using Kind)
- Deploys your app to the test environment
- Makes sure the app is actually running and responding

### 4. Release Phase

- Figures out what version number to use based on your commit messages
- Updates the changelog automatically
- Creates a GitHub release with all the details

All of this happens without you having to click any buttons or run any commands manually!

## What's in This Repository

```
interview/
├── .github/workflows/         # The automation magic happens here
├── app/                       # Your web application
│   ├── app.py                 # The main Flask app
│   ├── Dockerfile             # How to package the app
│   ├── requirements.txt       # What Python packages it needs
│   └── tests/                 # Tests to make sure it works
├── helm/interview-app/        # Kubernetes deployment configuration
│   ├── Chart.yaml            # Basic info about the deployment
│   ├── values.yaml           # Settings you can change
│   └── templates/            # The actual Kubernetes files
├── review/                    # Files for review
│   ├── nginx.yaml            # Review comments for yaml files with the correct yaml
│   └── script.sh             # Review comments for yaml files with the correct script
├── CHANGELOG.md              # What changed in each version
└── README.md                 # This file you're reading
```

## Running Tests

To make sure everything works before you deploy:

```bash
cd app
pip install -r requirements.txt
pytest tests/ -v --cov=.
```

## Making It All Work

### The Easy Way (Recommended)

1. Fork this repository to your own GitHub account
2. Make some changes to the code
3. Push your changes to GitHub
4. Watch the magic happen automatically!

### The Manual Way

If you want to see what's happening step by step:

```bash
# Deploy using Helm
helm install interview-app ./helm/interview-app
```

## Customizing the App

### Changing the Message

You can change what the app says by setting an environment variable:

```bash
# When running with Docker
docker run -e APP_MESSAGE="Hello from my custom app!" -p 8080:8080 interview-app

# When deploying with Helm
helm install interview-app ./helm/interview-app --set env.APP_MESSAGE="My custom message"
```

### Changing Settings

The main settings are in `helm/interview-app/values.yaml`:

```yaml
replicaCount: 2 # How many copies of the app to run
image:
  tag: "latest" # Which version of the app to use
service:
  port: 80 # What port the app listens on
resources:
  limits:
    cpu: 100m # Maximum CPU the app can use
    memory: 128Mi # Maximum memory the app can use
```

## What Makes This Special

- **Health Checks**: The system automatically knows if your app is working properly
- **Resource Limits**: Your app can't accidentally use too much CPU or memory
- **Security**: The app runs as a non-root user for safety
- **Automatic Testing**: Every change gets tested before it goes live
- **Version Control**: Every change is tracked and documented

## Want to Contribute?

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

1. Set up a kubernetes cluster ie. kind, minikube, k3s etc. (Using Kind in GitHub Actions)
2. Build and release an app. This application should have a dockerfile created by you and it should be built by you. (Flask app with automated releases)
3. Create a deployment of this app. (Complete K8s manifests with health checks)

**Extras completed:**

- IaC (Helm charts)
- GitOps (ArgoCD workflow)
- semver (Semantic versioning with automated releases)
- changelog (Keep a Changelog format)

### review

- Review folder containes the files asked for review
- extras: proper explanation
