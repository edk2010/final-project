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

data "archive_file" "mylambda" {
  type        = "zip"
  source_file = "./mylambda.py"
  output_path = "lambda_function_payload.zip"
}

data "aws_iam_role" "lambda_rw_s3"{

    name = "lambda_rw_s3"

}
resource "aws_lambda_function" "final-project" {
  # If the file is not in the current working directory you will need to include a
  # path.module in the filename.
  filename      = "lambda_function_payload.zip"
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
depends_on = [ aws_lambda_alias.test_alias ]

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


//resource "aws_lambda_invocation" "test_alias" {
//  function_name = "${aws_lambda_function.final-project.arn}:test"
//
//  triggers = {
//    redeployment = sha1(jsonencode([
//      aws_lambda_function.final-project.environment
//    ]))
//  }
//
//  input = jsonencode({
//    key1 = "value1"
//    key2 = "value2"
//  })
//}

//output "result_entry" {
//  value = jsondecode(aws_lambda_invocation.test_alias.result)
//}
//


resource "null_resource" "check_deploy" {
  provisioner "local-exec" {
      command = "python unitest_api.py ${data.aws_lambda_function_url.test_alias_url.function_url}"
  }

  depends_on = [aws_lambda_alias.test_alias]
}



data "aws_lambda_function" "final-project" {
  function_name = aws_lambda_function.final-project.arn
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

