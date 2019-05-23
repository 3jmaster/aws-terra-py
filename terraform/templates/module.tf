# Runs all terraform using module, under 'source' folder

{% for acct in accounts -%}

module "team-{{ acct.name }}-module" {
  source = "./modules/team-account-roles"
  providers = {
    aws = "aws.team-{{ acct.name }}-account"
  }
}

{% endfor %}

# add more modules here to create more resouces
