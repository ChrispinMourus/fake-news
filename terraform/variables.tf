variable "resource_group_name" {
  description = "Name of the Azure Resource Group"
  type        = string
  default     = "fake-news-rg"
}

variable "location" {
  description = "Azure region"
  type        = string
  default     = "East US"
}

variable "acr_name" {
  description = "Name of the Azure Container Registry"
  type        = string
  default     = "fakenewsacr2026"
}

variable "cluster_name" {
  description = "Name of the AKS Cluster"
  type        = string
  default     = "fake-news-aks"
}

variable "node_count" {
  description = "Number of AKS nodes"
  type        = number
  default     = 2
}
