variable "resource_group_name" {
  description = "The name of the resource group"
  type        = string
  default     = "veritas-ai-rg"
}

variable "location" {
  description = "The Azure region to deploy resources"
  type        = string
  default     = "East US"
}

variable "cluster_name" {
  description = "The name of the AKS cluster"
  type        = string
  default     = "veritas-aks"
}

variable "dns_prefix" {
  description = "DNS prefix for the cluster"
  type        = string
  default     = "veritasaks"
}

variable "node_count" {
  description = "The number of nodes in the default node pool"
  type        = number
  default     = 2
}

variable "node_vm_size" {
  description = "The size of the VMs in the default node pool"
  type        = string
  default     = "Standard_B2s"
}
