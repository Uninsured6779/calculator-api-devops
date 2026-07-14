resource "aws_cloudwatch_log_group" "calculator_logs" {
  name              = "/ecs/calculator-api"
  retention_in_days = 7

  tags = {
    Project   = var.project_name
    ManagedBy = "Terraform"
  }
}

resource "aws_security_group" "calculator_tf_sg" {
  name        = "calculator-tf-sg"
  description = "Managed by Terraform"

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Project   = var.project_name
    ManagedBy = "Terraform"
  }
}
