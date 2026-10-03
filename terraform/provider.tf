provider "aws" {
  region = var.aws_region
  assume_role {
    role_arn = var.deployer_role_arn
  }
}

terraform {
  required_version = ">= 1.15.9"

  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "6.63.0"
    }
  }

  backend "s3" {
    bucket               = "tfstate-resources-${data.aws_caller_identity.current.account_id}-${data.aws_region.current.id}-an"
    key                  = "terraform.tfstate"
    workspace_key_prefix = "pyserverless"
  }
}