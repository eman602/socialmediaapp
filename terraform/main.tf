provider "aws" {
    
    region = "eu-west-1"
}

resource "aws_instance" "example" {
    ami = "ami-09b49c48928db765c"
    instance_type = "t2.micro"
}

