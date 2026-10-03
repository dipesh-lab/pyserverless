variable "env_name" {
  description = "dev/prod"
  type        = string
  default     = "dev"
}
variable "aws_region" {
  description = "Target AWS region"
  type        = string
}
variable "deployer_role_arn" {
  description = "Assume role arn for deployment"
  type        = string
}
variable "artifacts" {
  description = "Dictionary of artifacts name and its package name"
  type        = map(string)
  default     = {
    "app_zip": "../build/pyserverless.zip"
  }
}

locals {
  common_tags = {
    project = "pyserverless"
    env     = var.env_name
  }
  def_runtime       = "python3.14"
  def_max_memory    = 256
  def_timeout       = 30
  def_architectures = ["arm64"]
}