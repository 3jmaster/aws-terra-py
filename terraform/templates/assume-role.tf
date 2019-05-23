# Assumes a role into the target account so we can create resources there
{% for acct in accounts -%}

provider "aws" {
  alias  = "team-{{ acct.name }}-account"
  region = "ap-southeast-1"
  assume_role {
    role_arn     = "arn:aws:iam::{{ acct.number }}:role/{{ acct.rolename }}"
    session_name = "ROLE_SESSION_{{ acct.name }}"
  }
}

{% endfor %}

# add more provider blocks here to assume more roles
