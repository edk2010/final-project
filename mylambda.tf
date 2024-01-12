/*
data "aws_iam_policy_document" "assume_role" {
  statement {
    effect = "Allow"

    principals {
      type        = "Service"
      identifiers = ["lambda.amazonaws.com"]
    }

    actions = ["sts:AssumeRole"]
  }
}

resource "aws_iam_role" "iam_for_lambda" {
  name               = "iam_for_lambda"
  assume_role_policy = data.aws_iam_policy_document.assume_role.json
}

*/

data "archive_file" "lambda" {
  type        = "zip"
  source_file = "./mylambda.py"
  output_path = "lambda_function_payload.zip"
}

data "aws_iam_role" "lambda_rw_s3"{

    name = "lambda_rw_s3"

}
resource "aws_lambda_function" "test_lambda" {
  # If the file is not in the current working directory you will need to include a
  # path.module in the filename.
  filename      = "lambda_function_payload.zip"
  function_name = "lambda_function_name"
  role          = data.aws_iam_role.lambda_rw_s3.arn
  handler       = "mylambda.lambda_handler"

  source_code_hash = data.archive_file.lambda.output_base64sha256

  runtime = "python3.10"

 
}




resource "aws_lambda_function_url" "test_lambda" {
  function_name      = aws_lambda_function.test_lambda.function_name
  authorization_type = "NONE"
}


output "lambda_function_url"{

value = aws_lambda_function_url.test_lambda.function_url

}
  