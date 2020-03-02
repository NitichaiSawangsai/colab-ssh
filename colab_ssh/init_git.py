from colab_ssh._command import run_command as _run_command
import os
import sys


def parse_folder_name(array):
    import re
    sys.path.insert(0, "./"+re.search("'(.*?)'", array[0]).groups(1)[0])

def init_git(repositoryUrl, branch="master", personal_token=""):
    _run_command("git clone {}".format(
            repositoryUrl.replace("github.com", personal_token+"@github.com")if personal_token else repositoryUrl) ,
            callback=parse_folder_name
    )
    _run_command("git checkout {}".format(branch))


    

    os.system("mkdir -p ~/.ssh && curl -L -f {} {}/{}/.colab_ssh/authorized_keys >> ~/.ssh/authorized_keys".format(
        ("-H 'Authorization: token {}'".format(personal_token)) if personal_token else "",
        repositoryUrl.rstrip(".git").replace("github.com", "raw.githubusercontent.com"), 
        branch))

    print("Successfully cloned the repository")