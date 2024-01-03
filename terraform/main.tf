terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }

  required_version = ">= 1.2.0"
}

provider "aws" {
  region = "eu-west-1"
  profile = "default"
}

resource "aws_security_group" "recommendations" {
  name        = "recommendations-sg"
  
  ingress {
    from_port   = 8080
    to_port     = 8080
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_key_pair" "recommendations" {
  key_name   = "recommendations-key"
  public_key = "ssh-rsa recommendations_ssh_key"
}

# Create an EC2 instance
resource "aws_instance" "recommendations" {
  ami           = "ami-02cad064a29d4550c " 
  instance_type = "t2.micro"
  key_name      = aws_key_pair.recommendations.key_name
  security_groups = [aws_security_group.recommendations.name]

  user_data = <<-EOF
              #!/bin/bash
              sudo yum update -y
              sudo amazon-linux-extras install docker -y
              sudo service docker start
              sudo usermod -aG docker ec2-user
              EOF

  tags = {
    Name = "recommendations-instance"
  }
}
