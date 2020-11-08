import sys
import os
from github import Github
from dotenv import load_dotenv

load_dotenv()

path = os.getenv("FILEPATH")
githubAccessToken = os.getenv("GITHUB_ACCESS_TOKEN")
g = Github(githubAccessToken)

# This function checks if a Repo in GitHub or folder on PC shares the same name with the project you are trying to create
def canCreate():
    repo_exists = False
    for repo in g.get_user().get_repos():
        if str(repo.name).upper() == str(sys.argv[1]).upper():
            repo_exists = True
            print("Cannot create project because a REPO with the same name exists in GitHub")

    folder_exists = False
    for filename in os.listdir(path):
        if str(filename).upper() == str(sys.argv[1]).upper():
            folder_exists = True
            print("Cannot create project because a FOLDER with the same name exists in the path")

    if repo_exists == True or folder_exists == True:
        print("ERROR cannot create Project")
    else:
        createRepo()

# Creates Repo in GitHub
def createRepo():
    try:
        g.get_user().create_repo(sys.argv[1])
    except Exception as e:
        print("ERROR IN CREATING REPO")
        print(e)
    else:
        print("REPO CREATED")
        createFolder()

# Creates folder on PC in specified location
def createFolder():
    try:
        os.makedirs(path + "\\"+str(sys.argv[1]), 0o777)
    except Exception as e:
        print("ERROR IN CREATING FOLDER")
        print(e)
    else:
        print("FOLDER CREATED")
        initFolder()

# Initialises teh folder & pushes it up to GitHub
def initFolder():
    command_to_execute = 'cd ' + str(path) + '\\' + str(sys.argv[1]) + ' && echo # '+ str(sys.argv[1]) + ' >> README.md' + ' && git init && git remote add origin https://github.com/' + g.get_user().login + '/' + str(sys.argv[1]) + ' && git add * && git commit -m "Initial commit" && git push -u origin master'
    os.system(command_to_execute)
    print(str(sys.argv[1]) + ' folder initialised')
    os.system('code ' + str(path) + '\\' + str(sys.argv[1]))   


if __name__ == "__main__":
    canCreate()
    #deletion()

'''
# Deletes repo in GitHub - Access Token needs to allow deletion
def deletion():
    try:
        g.get_user().get_repo(str(sys.argv[1])).delete()
    except Exception as e:
        print("ERROR IN DELETING REPO: ")
        print(e)
    else:
        print("REPO DELETED")
'''