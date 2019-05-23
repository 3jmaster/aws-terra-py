# AWS ops

As a AWS operator, how do I create resources in multiple existing AWS accounts?

Inspired by: https://medium.com/slalom-engineering/aws-multi-account-architecture-with-terraform-yeoman-and-jenkins-7fd42ddcdda8

and also Terraform 0.12 does not have the feature of dynamically assuming multiple roles for multiple providers yet.

Jinja templating will help to populate the respective terraform files required to run the terraform modules. 

Use at your own risk!

## Requirements:
1. Existing Roles in the target accounts to assume into
2. Existing Permissions and Roles set up

## Steps
0. Ensure you have AWS credentials (as iam user control plane) in your env variables to assume these target accounts' roles

1. Update `target_accounts.json` with the list of targets you want to execute on

2. Populate all the terraform tf files dynamically for ALL AWS ACCOUNTS using python and jinja. run:

  `./populate_terraform.py`

3. Proceed to execute terraform init, plan and apply run:

  `terraform init ./terraform`

  `terraform plan ./terraform`
