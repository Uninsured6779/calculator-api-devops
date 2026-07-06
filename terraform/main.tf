resource "aws_cloudwatch_log_group" "calculator_logs" {
  name              = "/ecs/calculator-api"
  retention_in_days = 7
}
