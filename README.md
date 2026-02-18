# OmniOps – DevOps Practice Project

OmniOps is a hands-on DevOps project that demonstrates containerization, Kubernetes deployment, and CI automation using GitHub Actions.

The project uses a lightweight Python application packaged into a Docker image, deployed on Kubernetes, and exposed locally for testing. A CI pipeline automatically builds and pushes the Docker image to Docker Hub on every push.

---

## What This Project Covers

- Docker image creation using a custom Dockerfile  
- Running a containerized application on Kubernetes (Minikube)  
- Kubernetes Deployment and Service configuration  
- Environment variable injection into containers  
- Local access using `kubectl port-forward`  
- Automated Docker build & push using GitHub Actions  
- Real-world debugging of CI, image, and Kubernetes issues  

---

## Tech Stack

- Python  
- Docker  
- Kubernetes (Minikube)  
- GitHub Actions  
- Docker Hub  

---

## Project Structure

app/ - Application source code
docker/ - Dockerfile
k8s/ - Kubernetes manifests
.github/ - GitHub Actions CI workflow


---

## How It Works (High Level)

1. Application runs on port `80` inside a Docker container  
2. Kubernetes Deployment manages the container lifecycle  
3. Kubernetes Service exposes the application internally  
4. Local access is provided via port-forwarding  
5. GitHub Actions builds and pushes the Docker image automatically  

---

## Status

✔ Dockerized  
✔ Kubernetes deployed  
✔ Service accessible  
✔ CI pipeline working  

This repository is intended for DevOps learning, experimentation, and interview demonstration.
