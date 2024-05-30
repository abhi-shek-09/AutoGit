import re
import subprocess

def run_git_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
    else:
        print(result.stdout)

def push_to_branch(branch_name, commit_message):
    commands = [
        "git add .",
        f'git commit -m "{commit_message}"',
        f"git push origin {branch_name}"
    ]
    
    for command in commands:
        run_git_command(command)

def create_and_first_commit(branch_name, commit_message, repository_url):
    commands = [
        "git init",
        "git add .",
        f'git commit -m "{commit_message}"',
        f'git branch -M {branch_name}',
        f'git remote add origin {repository_url}',
        f"git push origin {branch_name}"
    ]
    
    for command in commands:
        run_git_command(command)

def push_to_new_branch(branch_name, commit_message):
    commands = [
        f'git checkout -b "{branch_name}"',
        "git add .",
        f'git commit -m "{commit_message}"',
        f"git push --set-upstream origin {branch_name}"
    ]
    
    for command in commands:
        run_git_command(command)

if __name__ == "__main__":
    while True:
        input_st = input('Enter your command (or type "exit" to quit): ')

        pattern_init = re.compile(
            r'^init\s'  # init
            r'[a-z_]+\s'  # branch_name: 
            r'"[a-zA-Z0-9\s\-_]*"\s'  # commit_message
            r'"https://github\.com/[A-Za-z0-9_-]+/[A-Za-z0-9_-]+\.git"$'  # url
        )

        pattern_commit = re.compile(
            r'^push\s'
            r'to\s'  # init
            r'[a-z_]+\s'  # branch_name: 
            r'"[a-zA-Z0-9\s\-_]*"'  # commit_message
        )

        pattern_branch = re.compile(
            r'^push\s'
            r'to\s'  # init
            r'new\s' # specifying its a new branch
            r'[a-z_]+\s'  # branch_name: 
            r'"[a-zA-Z0-9\s\-_]*"'  # commit_message

        )

        if input_st.lower() == "exit":
            print("Goodbye")
            break


        elif re.match(pattern_init, input_st):
            # init branch_name "commit_message" "https://github.com/abhi-shek-09/AutoGit.git"
            _, branch_name, commit_message, url = input_st.split(" ")
            commit_message = commit_message[1:-1]
            url = url[1:-1]
            create_and_first_commit(branch_name=branch_name, commit_message=commit_message, repository_url=url)
            print("Repository created and commits made")


        elif re.match(pattern_commit, input_st):
            # push to branch_name "commit_message"
            _, __, branch_name, commit_message = input_st.split(" ")
            commit_message = commit_message[1:-1]
            push_to_branch(branch_name, commit_message)
            print("Repository created and commits made")

        elif re.match(pattern_branch, input_st):
            # push to new branch_name "commit_message"
            _, __, ___, branch_name, commit_message = input_st.split(" ")
            commit_message = commit_message[1:-1]
            push_to_new_branch(branch_name, commit_message)


        #Code will be updated now