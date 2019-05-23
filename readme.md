# AWS ops

As a AWS operator, how do I create resources in multiple existing AWS accounts?

## Requirements:
1. Existing Roles in the target accounts to assume into


## Steps
0. Ensure you have AWS credentials (as iam user control plane) in your env variables. or you can get it via `login_iam.sh` in the aws-security-iam repo

1. Update `target_accounts.json` with the list of targets you want to execute on

2. Populate all the terraform tf files dynamically for ALL AWS ACCOUNTS using python and jinja run:

  `./populate_terraform.py`

3. Proceed to to execute terraform init, plan and apply run:
  `terraform init ./terraform`

  `terraform plan ./terraform`
