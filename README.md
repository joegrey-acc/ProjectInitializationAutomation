# ProjectInitializationAutomation

## This will allow user to create a project in a specified folder and create a repo in GitHub and have it initialised with a ReadMe with the command :
### create <project_name>

## Instructions:
(ensure all folder path have forward slashes "/" - NOT back slashes "\")
1. CREATE .env file to project folder
2. Add FILEPATH = "< folder where you want to create new project >" to .ev
3. Add GITHUB_ACCESS_TOKEN = "< the access token that has all repo elements checked >" to .ev

### Creating functions / commands in terminals
#### WINDOWS
4. CREATE a create.bat file
5. ADD the following code to the bat file:
    ```
        start cmd /k "<folder where project is located>\create.py %1"
    ```
6. Add .bat file to PATH in the environmental variables
7. Now you can successfully create a new project from anywhere in a windows termainal using the command:
    ```
        create <project name>
    ```

#### BASH
4. OPEN ~/.bashrc in an editor, e.g.:
	(.bashrc folder should be located in C:\Users\<user>)
    ```
        code ~/.bashrc
    ```
    This file will run all alias' when bash is opened 
5. ADD the following command to the file:
    ```
        alias create="python <folder where project is located>/create.py $1"
    ```
6. Now you can successfully create a new project from anywhere in a bash termainal using the command:
    ```
        create <project name>
    ```

## Additional Feature:
### Easy switch between bash & windows terminals
#### Windows to Bash
1. CREATE bash.bat file
2. ENSURE folder in which .bat file is located is in PATH in the environmental variable
3. ADD the following code into bash.bat file:
    (Where your git folder is stored)
    ```
        "C:\Program Files\Git\bin\sh.exe" --login -i
    ```
4. NOW in a windows terminal when you type the command 'bash', the terminal will switch to a bash terminal

#### Bash to Windows
1. OPEN ~/.bashrc in an editor, e.g.:
    ```
        code ~/.bashrc
    ```
2. ADD the following command to the file:
    ```
        alias cmd="C:/WINDOWS/System32/cmd.exe"
    ```
3. NOW in a bash terminal when you type the command 'cmd', the terminal will switch to a windows terminal