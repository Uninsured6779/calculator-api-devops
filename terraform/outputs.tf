output "log_group_name" {
  value = aws_cloudwatch_log_group.calculator_logs.name
}

output "security_group_id" {
  value = aws_security_group.calculator_tf_sg.id
}
