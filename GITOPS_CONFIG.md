# GitOps Configuration with ArgoCD

This document explains how to set up true GitOps with ArgoCD for this project.

## What is GitOps?

GitOps is a way to manage infrastructure and applications using Git as the single source of truth. ArgoCD continuously monitors your Git repository and keeps your Kubernetes clusters in sync.

## Architecture

```
Git Repository (Source of Truth)
    ↓
ArgoCD (GitOps Operator)
    ↓
Kubernetes Cluster (Target Environment)
```

## Files in This Project

### `argocd/application.yaml`

Defines how ArgoCD should deploy your application:

- **Source**: Points to your Git repository and Helm chart
- **Destination**: Target Kubernetes cluster and namespace
- **Sync Policy**: How often to check for changes and how to handle conflicts

### `argocd/install-argocd.sh`

Script to install ArgoCD on a Kubernetes cluster:

- Creates ArgoCD namespace
- Installs ArgoCD components
- Sets up the interview-app application
- Provides access instructions

### `.github/workflows/gitops-setup.yml`

GitHub Actions workflow to set up GitOps on a Kind cluster:

- Creates persistent Kind cluster
- Installs ArgoCD
- Configures the application
- Shows status and access information

## How to Set Up GitOps

### Option 1: Local Development (Minikube)

```bash
# Start Minikube
minikube start

# Install ArgoCD
./argocd/install-argocd.sh

# Access ArgoCD UI
kubectl port-forward svc/argocd-server -n argocd 8080:443
# Visit: https://localhost:8080
# Username: admin
# Password: (shown in terminal)
```

### Option 2: Cloud Cluster (EKS, GKE, AKS)

```bash
# Connect to your cluster
kubectl config use-context your-cluster

# Install ArgoCD
./argocd/install-argocd.sh

# Access ArgoCD UI (if LoadBalancer is available)
kubectl get svc argocd-server -n argocd
```

### Option 3: GitHub Actions (Kind)

1. Go to Actions tab in GitHub
2. Select "GitOps Setup" workflow
3. Click "Run workflow"
4. Choose "kind" as cluster type
5. Wait for completion

## How GitOps Works

### 1. Continuous Monitoring

- ArgoCD checks your Git repository every 3 minutes
- Compares desired state (Git) vs actual state (Kubernetes)
- Detects any changes or drift

### 2. Automatic Deployment

- When you push changes to Git, ArgoCD detects them
- Automatically deploys the new version
- Updates the Kubernetes cluster to match Git

### 3. Drift Detection

- If someone manually changes the cluster, ArgoCD detects it
- Automatically reverts changes to match Git state
- Keeps cluster in sync with your code

### 4. Multi-Environment Support

- Deploy to different clusters (dev, staging, production)
- Use different Helm values for each environment
- Promote applications between environments

## Benefits of GitOps

### Continuous Reconciliation

- **24/7 monitoring** - Always watching for changes
- **Self-healing** - Fixes problems automatically
- **Drift detection** - Catches manual changes

### Better Security

- **No direct cluster access** - All changes through Git
- **Audit trail** - Every change is tracked
- **Approval workflows** - PR reviews before deployment

### Multi-Environment Management

- **Consistent deployments** - Same process everywhere
- **Environment promotion** - Move apps between clusters
- **Configuration management** - Different settings per environment

## Troubleshooting

### Check ArgoCD Status

```bash
kubectl get applications -n argocd
kubectl describe application interview-app -n argocd
```

### Check Application Logs

```bash
kubectl logs -n argocd deployment/argocd-application-controller
kubectl logs -n argocd deployment/argocd-server
```

### Manual Sync

```bash
kubectl patch application interview-app -n argocd --type merge -p '{"operation":{"sync":{"syncStrategy":{"hook":{"force":true}}}}}'
```

## Integration with CI/CD

This GitOps setup works alongside the existing CI/CD pipeline:

1. **CI/CD Pipeline** - Builds, tests, and creates releases
2. **ArgoCD** - Deploys and monitors the application
3. **Git Repository** - Single source of truth for both

The CI/CD pipeline handles the build and release process, while ArgoCD handles the deployment and monitoring. This gives you the best of both worlds!
