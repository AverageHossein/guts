variable "AWS_REGION" {
  type = string
}
variable "AWS_PIPELINE_NAME" { type = string }
variable "REPOSITORY_ID" { type = string }
variable "BRANCH_NAME" { type = string }
variable "AWS_CODEPIPELINE_S3_BUCKET_ARTIFACT" { type = string }
variable "CODE_STAR_CONNECTION_ARN" { type = string }
variable "CODEBUILD_NAME" { type = string }
variable "CLUSTER_NAME" { type = string }
variable "SERVICE_NAME" { type = string }