# Veritas AI - Fake News Detection System

## 🎯 Project Overview
This project is an AI-powered web application that classifies news articles as **FAKE** or **REAL**. 

This version is optimized for **Local Kubernetes (Docker Desktop)** development with a simplified **GitHub Actions CI** pipeline for image builds.

---

## 🏗️ Architecture
1.  **CI (GitHub Actions)**: Automatically builds and pushes your Docker image to **Docker Hub** on every push.
2.  **CD (Local Deployment)**: You manage the Kubernetes deployment locally on your machine using **Docker Desktop**.

## 📁 Project Structure
- `app/`: Flask application code, ML model, and training script.
- `docker/`: Dockerfile for containerization.
- `k8s/`: Kubernetes Deployment and Service manifests.
- `.github/workflows/`: GitHub Actions CI pipeline.

---

## 🛠️ Setup Instructions

### 1. Build and CI Setup
1.  Add your Docker Hub secrets to GitHub: `DOCKERHUB_USERNAME` and `DOCKERHUB_PASSWORD`.
2.  Push your code to `main`. GitHub will automatically build and host your image.

### 2. Local Kubernetes Deployment (Docker Desktop)
1.  **Enable Kubernetes** in your Docker Desktop settings.
2.  **Update the Image Name**: Open `k8s/deployment.yaml` and change `your-dockerhub-username` to your actual Docker Hub username.
3.  **Deploy Locally**:
    ```bash
    # Navigate to project root
    kubectl apply -f k8s/
    ```

### 3. Verification
- View running pods: `kubectl get pods`
- Access the app: Once the service is running, it will be available via the LoadBalancer IP (usually `localhost:5000` on Docker Desktop).

---

## 🚀 Advanced Deployment (Cloud)

### 1. Infrastructure Provisioning (Terraform)
Provision a production-ready Azure Kubernetes Service (AKS) cluster.
1.  **Initialize**: `cd terraform && terraform init`
2.  **Plan**: `terraform plan`
3.  **Apply**: `terraform apply -auto-approve`
4.  **Connect**: Run the command provided in the outputs to configure `kubectl`:
    ```bash
    az aks get-credentials --resource-group veritas-ai-rg --name veritas-aks
    ```

### 2. Configuration Management & Deployment (Ansible)
Automate the application deployment and health checks.
1.  **Install Requirements**:
    ```bash
    pip install kubernetes
    ansible-galaxy collection install kubernetes.core
    ```
2.  **Run Playbook**:
    ```bash
    cd ansible && ansible-playbook playbook.yml
    ```

---

**Senior DevOps Engineer & AI Developer**
*Project optimized for Local Kubernetes and Cloud Azure AKS.*