

data "archive_file" "mylambda" {
  type        = "zip"
  source_file = "./mylambda.py"
  output_path = "lambda_function_payload_v1.zip"
}

data "aws_iam_role" "lambda_rw_s3"{

    name = "lambda_rw_s3"

}
resource "aws_lambda_function" "final-project" {
  # If the file is not in the current working directory you will need to include a
  # path.module in the filename.
  filename      = "lambda_function_payload_v1.zip"
  function_name = "final-project"
  role          = data.aws_iam_role.lambda_rw_s3.arn
  handler       = "mylambda.lambda_handler"
  publish       = true
  source_code_hash = data.archive_file.mylambda.output_base64sha256

  runtime = "python3.10"

 
}


data "aws_lambda_alias" "test_version"{

  name = "test"
  function_name = aws_lambda_function.final-project.arn
  depends_on = [ aws_lambda_alias.test_alias ]

}

data "aws_lambda_function_url" "test_alias_url"{

function_name = "${aws_lambda_function.final-project.arn}:test"
depends_on = [ aws_lambda_function_url.test_alias_url ]


}


resource "aws_lambda_function_url" "prod_alias_url" {
  
  function_name      = "${aws_lambda_function.final-project.arn}:prod"
  authorization_type = "NONE"
  depends_on = [aws_lambda_alias.prod_alias]

}
resource "aws_lambda_function_url" "test_alias_url" {
  
  function_name      = "${aws_lambda_function.final-project.arn}:test"
  authorization_type = "NONE"
  depends_on = [aws_lambda_alias.test_alias]

}

resource "aws_lambda_function_url" "final-project" {
  
  function_name      = aws_lambda_function.final-project.arn
  authorization_type = "NONE"
}

resource "aws_lambda_alias" "prod_alias" {
  name             = "prod"
  description      = "Production alias"
  function_name    = aws_lambda_function.final-project.arn
  function_version = data.aws_lambda_alias.test_version.function_version //? data.aws_lambda_alias.prod_version.function_version : "$LATEST"
  
//depends_on = [aws_lambda_invocation.test_alias]
}


resource "aws_lambda_alias" "test_alias" {
  name             = "test"
  description      = "pred prod test alias"
  function_name    = aws_lambda_function.final-project.arn
  function_version = "$LATEST"
}





resource "null_resource" "check_deploy" {
  provisioner "local-exec" {
      command = "python unitest_api.py ${data.aws_lambda_function_url.test_alias_url.function_url} | tee output.json"
      
  }

  depends_on = [aws_lambda_alias.test_alias]
}



data "aws_lambda_function" "final-project" {
  function_name = aws_lambda_function.final-project.arn
}

output "lambda_check_deploy" {
  value = null_resource.check_deploy
}

output "lambda_function_versions" {
  value = data.aws_lambda_function.final-project.version
}


output "lambda_function_prod_version" {
  value = data.aws_lambda_alias.test_version.function_version

}

output "lambda_function_url"{

value = aws_lambda_function_url.final-project.function_url

}
  
output "prod_lambda_function_url"{

value = aws_lambda_function_url.prod_alias_url.function_url

}
output "test_lambda_function_url"{

value = aws_lambda_function_url.test_alias_url.function_url

}

