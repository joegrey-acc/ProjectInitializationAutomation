# ProjectInitializationAutomation

### This will allow user to create a project in a specified folder and create a repo in GitHub and have it initialised with a ReadMe
### (create <project_name>)


1. CREATE .ev file to project folder
2. Add FILEPATH = "< folder where you want to create new project >" to .ev
3. Add GITHUB_ACCESS_TOKEN = "< the access token that has all repo elements checked >" to .ev

4. CREATE a .bat file
5. ADD the following code to the bat file:
    ```
        start cmd /k "<folder where project is located>\create.py %1"
    ```
6. Add .bat file to PATH in the environmental variables
7. Now you can successfully create a new project from anywhere in a command termainal using the command:
    ```
        create <project name>
    ```
