# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- GitHub Actions workflow for automated CI/CD with Kind cluster
- GitOps workflow using ArgoCD for continuous deployment
- Semantic versioning with automated releases
- Helm chart for Infrastructure as Code
- Comprehensive testing and linting in CI pipeline
- Automated Docker image building and pushing to GitHub Container Registry
- Health checks and resource limits for better reliability
- Port forwarding and application testing in CI

### Changed

- Migrated from minikube to Kind for better CI/CD compatibility
- Enhanced Kubernetes manifests with proper labels and selectors
- Improved Dockerfile with security best practices

### Security

- Added non-root user support in Dockerfile
- Implemented resource limits and requests
- Added health checks for better reliability
- Container image scanning in CI pipeline

## [1.0.0] - 2024-01-XX

### Added

- Initial Flask application with environment variable support
- Dockerfile for containerization
- Kubernetes manifests (Deployment, Service, ConfigMap)
- Basic GitHub Actions CI/CD pipeline
- Health checks and resource limits
- Automated testing and deployment

### Fixed

- Shell script variable naming issues
- Dockerfile security improvements
- Kubernetes manifest labels and selectors
