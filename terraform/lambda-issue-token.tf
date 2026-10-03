module "lambda_issue_token" {
  source  = "terraform-aws-modules/lambda/aws"
  version = "8.8.0"

  function_name  = "issue-token-${var.env_name}"
  description    = "Issue token lambda"
  handler        = "functions.identity.issue_token.handler"
  create_package = false
  publish        = true

  s3_existing_package = {
    bucket     = data.aws_s3_bucket.deployable_artifacts.id
    key        = aws_s3_object.app_jar.key
    version_id = aws_s3_object.app_jar.version_id
  }

  architectures = local.def_architectures

  cloudwatch_logs_retention_in_days = 1
  runtime                           = local.def_runtime
  memory_size                       = local.def_max_memory
  timeout                           = local.def_timeout
  include_default_tag               = false
  tags                              = local.common_tags
}