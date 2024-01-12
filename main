provider "aws" {
  region = "us-west-2"
}

resource "aws_iam_role" "lambda_role" {
  name = "lambda_role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Action = "sts:AssumeRole",
        Effect = "Allow",
        Principal = {
          Service = "lambda.amazonaws.com"
        },
      },
    ],
  })
}

data "archive_file" "lambda_zip" {
    type        = "zip"
    source_file = "./lambda.py"
    output_path = "./lambda.zip"
}


resource "aws_lambda_function" "my_lambda" {
  filename      = data.archive_file.lambda_zip.output_path
  function_name = "finalproject"
  role          = aws_iam_role.lambda_role.arn
  handler       = "index.handler"
  runtime       = "python3.10" 

  source_code_hash = filebase64sha256(data.archive_file.lambda_zip.output_path) # Update the path to your ZIP file
}

resource "aws_api_gateway_rest_api" "my_api" {
  name        = "project-tl"
  description = "project-tl"
}

resource "aws_api_gateway_resource" "api_resource" {
  rest_api_id = aws_api_gateway_rest_api.my_api.id
  parent_id   = aws_api_gateway_rest_api.my_api.root_resource_id
  path_part   = "myresource" # The URL path part
}

resource "aws_api_gateway_method" "api_method" {
  rest_api_id   = aws_api_gateway_rest_api.my_api.id
  resource_id   = aws_api_gateway_resource.api_resource.id
  http_method   = "GET" # Change to your preferred HTTP method
  authorization = "NONE"
}

resource "aws_api_gateway_integration" "lambda_integration" {
  rest_api_id = aws_api_gateway_rest_api.my_api.id
  resource_id = aws_api_gateway_resource.api_resource.id
  http_method = aws_api_gateway_method.api_method.http_method
  integration_http_method = "POST"
  type        = "AWS_PROXY"
  uri         = aws_lambda_function.my_lambda.invoke_arn
}

resource "aws_lambda_permission" "allow_api_gateway" {
  statement_id  = "AllowExecutionFromAPIGateway"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.my_lambda.function_name
  principal     = "apigateway.amazonaws.com"

  # Source ARN for API Gateway
  source_arn = "${aws_api_gateway_rest_api.my_api.execution_arn}/*/${aws_api_gateway_method.api_method.http_method}${aws_api_gateway_resource.api_resource.path}"
}

resource "aws_api_gateway_deployment" "api_deployment" {
  depends_on = [aws_api_gateway_integration.lambda_integration]

  rest_api_id = aws_api_gateway_rest_api.my_api.id
  stage_name  = "dev" # Change to your preferred stage name
}

output "api_invoke_url" {
  value = "${aws_api_gateway_deployment.api_deployment.invoke_url}/${aws_api_gateway_resource.api_resource.path}"
}


