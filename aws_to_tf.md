## How to transform AWS resources to usable terraform

Simple process that can be extended and automated:

This example is using a streaming application as its target:

 - Visit your AWS management console
 - Under Amazon Kinesis > Analytics applications > Streaming applications, copy the ARN (there is a convenience copy icon)
 - Back up and move `terraform.tfstate` file somewhere safe
 - Create a `main.tf` file similar to:

```terraform
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.0"
    }
  }
}

# Configure the AWS Provider
provider "aws" {
  shared_credentials_file = "<credentials file location>"
  profile = "default"
  region = "<region of choice>"
}


resource "aws_kinesisanalyticsv2_application" "example" {
}
```
 - In the same directory, `terraform import aws_kinesisanalyticsv2_application.example <ARN>`
 - This will create a new `terraform.tfstate` file with the current state found in AWS
 - Perform `terraform state list` which should print your resource: `aws_kinesisanalyticsv2_application.example`
 - Finally perform `terraform state show aws_kinesisanalyticsv2_application.example` which will provide you with the full terraform configuration, this can be used to write much better terraform artifacts that build your pipeline incrementally (using variables, and existing artifact references)
