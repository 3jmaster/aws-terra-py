#!/usr/bin/env python3
from jinja2 import Template, Environment, FileSystemLoader
import json

# SET VARIABLES FOR POPULATION
templates_dir='terraform/templates'
role_to_assume='admin-role'
accounts = []
aws_accounts_json_file='target_accounts.json'

# sample_accounts = [
#     {'name': 'Andrej', 'number': 34, 'rolename': 'admin-role' },
#     {'name': 'Mark', 'number': 17, 'rolename': 'admin-role' },
#     {'name': 'Thomas', 'number': 44, 'rolename': 'admin-role' }
# ]

# GETS ALL AWS ACCOUNTS
with open(aws_accounts_json_file, "r") as read_file:
    data = json.load(read_file)
# print (data)

for key in data:
    account_entry = {'name': key, 'number': data[key], 'rolename': role_to_assume }
    accounts.append(account_entry)
# print (accounts)

# FUNCTION TO GENERATE THE TF FILES USING JINJA TEMPLATES
def generatesFile (templates_dir, template_filename, output_filename):
    file_loader = FileSystemLoader(templates_dir)
    env = Environment(loader=file_loader)
    template = env.get_template(template_filename)
    output = template.render(accounts=accounts)
    file = open(output_filename,"w")
    file.write(output)
    file.close()
    print (".tf File written to " + output_filename)
    return;

# GENERATES THE ASSUME ROLE terraform file from template
template_filename = 'assume-role.tf'
output_filename = "terraform/provider_assume_multiple_roles.tf"
generatesFile(templates_dir,template_filename,output_filename)

# GENERATES THE ASSUME ROLE terraform file from template
template_filename = 'module.tf'
output_filename = "terraform/assume_role_to_execute_modules.tf"
generatesFile(templates_dir,template_filename,output_filename)

print ("Go to the folder containing generated .tf files to run terraform init, etc.")
