# Restaurant Recommendation System

This repository has a system manages a list of restaurants and their properties with an API for querying with a subset of these parameters and return a recommendation for a restaurant that answers the criteria, including the time of the request to check if its open.

## Features

- Query restaurants based on parameters like style, vegetarian options, and opening hours.
- Return a JSON object with the recommended restaurant and its properties.
- Cloud-native architecture with support for Azure, GCP, or AWS.
- Infrastructure as Code (IaC) setup using Terraform.
- Backend storage for recording the history of all requests and responses.
- Secure system design with consideration for the confidentiality of stored data.
- Continuous Integration and Continuous Deployment (CI/CD) pipeline for automatic deployment.

## Requirements
[X] The assignment submission should be done in a GIT repo that we can access.
[ ] Please include all code required to set up the system
[ ] The system has to be cloud native, with a preference for Azure, but also GCP or AWS are an option, with a simple architecture that will require minimal amount of maintenance.
[ ] The system should be written in full IaC style, I should be able to fully deploy it on my own cloud instance without making manual changes. Use Terraform for configuring the required cloud resources.
[X] There should be some backend storage mechanism that holds the history of all requests and returned responses. Consider that the backend data stored is highly confidential.
[X] Make sure the system is secure. However there is no need for the user to authenticate with the system (Assume its a free public service)
[ ] The system code should be deployed using an automatic CI CD pipeline following any code change, including when adding or updating restaurants.

## Setup Instructions

1. **Clone this repository:**
   ```bash
   git clone https://github.com/roniadmon/DevOps-Assignment.git

2. **Configure the provider
3. **Create the infrastructure
   ```bash
   cd restaurant-recommendation/terraform
   terraform init
   terraform apply

4. ** Run the CI and then the CD pipeline
 