# Ansible Execution Script for Windows (requires WSL or Ansible install)
# This script helps you run the deployment playbook locally.

$DOCKERHUB_USER = "chrispinmourus"  # Change this to your Docker Hub username
$IMAGE_TAG = "latest"

Write-Host "--- Starting Ansible Deployment for Veritas AI ---" -ForegroundColor Cyan

# Check for Ansible
if (Get-Command "ansible-playbook" -ErrorAction SilentlyContinue) {
    Write-Host "[OK] Ansible found. Running playbook..." -ForegroundColor Green
    ansible-playbook playbook.yml --extra-vars "dockerhub_user=$DOCKERHUB_USER image_tag=$IMAGE_TAG"
} else {
    Write-Host "[ERROR] ansible-playbook not found in your PATH." -ForegroundColor Red
    Write-Host "TIP: If you are on Windows, we recommend running this from WSL (Ubuntu)." -ForegroundColor Yellow
    Write-Host "Command to run in WSL:" -ForegroundColor Yellow
    Write-Host "cd ansible && ansible-playbook playbook.yml --extra-vars 'dockerhub_user=$DOCKERHUB_USER image_tag=$IMAGE_TAG'"
}

Write-Host "----------------------------------------------------" -ForegroundColor Cyan
