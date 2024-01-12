provider "aws" {
  region = "eu-west-1"
}

resource "aws_s3_bucket" "project-tl" {
  bucket = "project-tl"

  tags = {
    Name        = "project-tl"
    Environment = "prod"
  }
}


resource "aws_s3_object" "data" {
    bucket = aws_s3_bucket.project-tl.id
    key    = "data.json"
    acl    = "private"  
    source = "./data.json"
    etag = filemd5("./data.json")
  

}


