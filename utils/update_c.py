#!/usr/bin/env python3
import boto3
import re
import sys
from pathlib import Path
import pyperclip as pc

'''
After capturing credentials from "Get credentials for AWSAdministratorAccess" option 2
Run this script and it will validate your clipboard entry and prompt you to replace your credential
file and then prompt you to test the credentials
'''

home = str(Path.home())

def get_user(cli=False):
    'Display user information (md)'
    response = boto3.client('sts').get_caller_identity()
    from rich.console import Console
    from rich.markdown import Markdown

    console = Console()

    md = f'''
     UserId    {response['UserId']}
     Account   {response['Account']}
     ARN       {response['Arn']}
    '''
    from rich.markdown import Markdown
    markdown = Markdown(md)
    console.print(markdown)

    if cli:
        print("aws sts get-caller-identity")

if __name__ == "__main__":
    target_file = f"{home}/.aws/credentials"

    # Insert clipboard contents
    # Validate content
    pastoid = pc.paste()

    # Quick check to validate content
    # Should have this form:
    # [.*]
    # aws_access_key_id=
    # aws_secret_access_key=
    # aws_session_token=

    # TODO Create util that matches a multiline template to a string 
    regex =r'^\[[^\]]+\]\naws_access_key_id=\w+\naws_secret_access_key=\w+\naws_session_token=\w+'
    if re.match(regex, pastoid, re.MULTILINE | re.DOTALL):
        print("Looks good")
    else:
        print("Maybe you did not capture the credentials")
        sys.exit(1)

    # Transform if desired
    pastoid = re.sub("\[\w+\]", "[default]", pastoid)

    answer = input(f"Paste the following into {target_file}:\n{pastoid}\n\nContinue [Y/n]? ")
    if answer.lower() == 'n':
        print("Did nothing for you")
        sys.exit()
    
    # Replace content
    with open(target_file, 'w') as f:
        f.write(pastoid)

    # Test the creds
    answer = input(f"Test credentials [Y/n]? ")
    if answer.lower() == 'n':
        print("No testing performed")
        sys.exit()
    
    # Test
    # Get the user
    get_user(True)
