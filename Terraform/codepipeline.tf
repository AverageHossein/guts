resource "aws_codepipeline" "codepipeline" {
  name     = var.AWS_PIPELINE_NAME
  role_arn = aws_iam_role.codepipeline-iam-role.arn

  artifact_store {
    type     = "S3"
    location = aws_s3_bucket.codepipeline-s3-artifact.id
  }

  stage {
    name = "Source"

    action {
      name             = "Source"
      category         = "Source"
      owner            = "AWS"
      provider         = "CodeStarSourceConnection"
      version          = 1
      output_artifacts = ["source"]


      configuration = {
        ConnectionArn    = "${var.CODE_STAR_CONNECTION_ARN}"
        FullRepositoryId = "${var.REPOSITORY_ID}"
        BranchName       = "${var.BRANCH_NAME}"
      }
    }
  }

  stage {
    name = "Build"

    action {
      name             = "Build"
      category         = "Build"
      owner            = "AWS"
      provider         = "CodeBuild"
      version          = 1
      input_artifacts  = ["source"]
      output_artifacts = ["build"]

      configuration = {
        ProjectName = aws_codebuild_project.codebuild.name
      }
    }
  }

  stage {
    name = "Deploy"
    action {
      name            = "Deploy"
      category        = "Deploy"
      owner           = "AWS"
      provider        = "ECS"
      version         = "1"
      input_artifacts = ["build"]

      configuration = {
        ClusterName = "${var.CLUSTER_NAME}"
        ServiceName = "${var.SERVICE_NAME}"
        FileName    = "imagedefinitions.json"
      }
    }
  }
}
