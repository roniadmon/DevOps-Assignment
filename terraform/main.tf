provider "aws" {
  region  = "eu-west-1"
  profile = "default"
}

resource "aws_security_group" "recommendations_sg" {
  name = "recommendations-sg"

  ingress {
    from_port   = 8080
    to_port     = 8080
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_key_pair" "recommendations_kp" {
  key_name   = "recommendations-keypair"
  public_key = "ssh-rsa recommendations_ssh_key"
}

# Create an EC2 instance
resource "aws_instance" "recommendations_ec2" {
  ami             = "ami-02cad064a29d4550c "
  instance_type   = "t2.micro"
  key_name        = aws_key_pair.recommendations_kp.key_name
  security_groups = [aws_security_group.recommendations_sg.name]

  user_data = <<-EOF
              #!/bin/bash
              sudo yum update -y
              sudo amazon-linux-extras install docker -y
              sudo service docker start
              sudo usermod -aG docker ec2-user
              EOF

  tags = {
    Name = "recommendations"
  }
}

resource "aws_eip" "recommendations_eip" {
  vpc      = true
  instance = aws_instance.recommendations_ec2.id
}

resource "aws_route53_zone" "recommendations_zone" {
  name = "recommendations.com"
}

resource "aws_route53_record" "www-restaurants" {
  zone_id = aws_route53_zone.recommendations_zone.zone_id
  name    = "www.restaurants.recommendations.com"
  type    = "A"
  ttl     = 300
  records = [aws_eip.recommendations_eip.public_ip]
}