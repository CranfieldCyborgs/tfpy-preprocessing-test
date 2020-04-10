import subprocess as sp
import argparse as ap

# NOTE: This was a test, and this project does not fully function. Conda does not easily permit the use of scripting languages to create, enter and manage environments. The only thing that works is the list() function.

# Todo: At the moment this is only tested on windows. Extend to mac if necessary.
# Todo: Check for environment. I.e. bash, powershell, cmd.exe, etc.


def create_env():
    """
    This is for setting up the environment.
    This runs the command:
    conda env create -f .\environment.yml -p .\envs

    Todo: Error handling.
    Todo: Check if the .yml is UTF-8 encoded.
    """
    print("Creating the environment...")

    sp.run(["conda", "env", "create", "-f", ".\environment.yml", "-p", ".\envs"])

    print("Environment created.")


def enter_env():
    """
    This runs the command to enter the environment.
    conda activate .\envs
    CALL conda.bat activate
    """
    print("Entering...")
    res = sp.run(["conda", "activate", ".\envs"])
    print(res)
    if res.returncode == 1:
        sp.run(["conda", "init", "powershell"])
        sp.run(["conda.bat", "activate", ".\envs"])
    print("Entered.")


def update_env():
    """
    This is for updating the environment and installing any implementing anything that's missing.
    This runs the command:
    conda env update -f .\environment.yml -p .\envs
    """
    print("Updating the environment...")

    sp.run(["conda", "env", "update", "-f",
            ".\environment.yml", "-p", ".\envs", "--prune"])

    print("Environment updated.")


def list():
    print("Listing environments...")
    res = sp.run(["conda", "env", "list"])
    print(res)
    print("Completed.")


def deactivate():
    res = sp.run(["conda", "deactivate"])


parser = ap.ArgumentParser()

# arguments
parser.add_argument("command")

args = parser.parse_args()

options = {"list": list, "create": create_env,
           "update": update_env, "enter": enter_env, "deactivate": deactivate}


if args.command in options:
    command = options[args.command]
    command()
else:
    print("No other functions implemented yet.")
