# ProjectInitializationAutomation

### create <project_name>

1. CREATE .ev file to project folder
2. Add FILEPATH = "< folder where you want to create new project >" to .ev
3. Add GITHUB_ACCESS_TOKEN = "< the access token that has all repo elements checked >" to .ev

4. CREATE my_commands.sh file in project folder
5. Add the following to the my_commands.sh shell script file:
    ```
    #!/bin/bash

    function create() {
        python <folder where project folder is>/create.py $1
    }
    ```

6. In cmd run the command (to allow script to be called in cmd):
    ```
        source <folder where project folder is>/my_commands.sh
    ```

