#!/bin/bash

# ArgoCD Installation Script
# This script installs ArgoCD on a Kubernetes cluster

set -e

echo "Installing ArgoCD..."

# Create ArgoCD namespace
kubectl create namespace argocd --dry-run=client -o yaml | kubectl apply -f -

# Install ArgoCD
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml

# Wait for ArgoCD to be ready
echo "Waiting for ArgoCD to be ready..."
kubectl wait --for=condition=available --timeout=300s deployment/argocd-server -n argocd

# Get ArgoCD admin password
echo "ArgoCD admin password:"
kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d
echo ""

# Port forward ArgoCD server (optional)
echo "To access ArgoCD UI, run:"
echo "kubectl port-forward svc/argocd-server -n argocd 8080:443"
echo ""
echo "Then visit: https://localhost:8080"
echo "Username: admin"
echo "Password: (see above)"

# Install the application
echo "Installing interview-app application..."
kubectl apply -f argocd/application.yaml

echo "ArgoCD installation complete!"
echo "Check application status: kubectl get applications -n argocd"
