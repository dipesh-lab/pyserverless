data "aws_s3_bucket" "deployable_artifacts" {
  bucket = "app-artifacts-${var.env_name}-${data.aws_caller_identity.current.account_id}-${var.aws_region}-an"
}

resource "aws_s3_object" "app_jar" {
  bucket      = data.aws_s3_bucket.deployable_artifacts.id
  key         = "pyserverless"
  source      = var.artifacts["app_zip"]
  source_hash = filesha256(var.artifacts["app_zip"])
  tags        = local.common_tags
}