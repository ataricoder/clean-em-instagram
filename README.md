# clean-em-instagram
Clean 'Em Bot for Instagram

Document all dependencies and libraries/modules installed here. If you can, add a link to it.

If using a virtual environment with Python, document the Py version here.

If any (weird) steps need to be taken, document them here.

Keep this repo private, and add all credentials to the main program.

-dany

##Pre-Requisites
Minimum:
* 1 GB RAM 
* Python 2.7
* Unix 64-bit
* Python Package Index (PIP)

## Libraries/Dependencies
Clean 'Em Bot for Instagram uses [Instapy](https://github.com/timgrossmann/InstaPy "Instapy Repo") as the backend library that drives the Instagram Bot.

Python3 is recommended inside a python environment via pyenv but is not required. (Python 2.7+)

The main program is called **'massive**\_**follow**\_**then**\_**unfollow**\_**works-non-stop.py'**

And you can run it by typing `sudo python3 massive_follow_then_unfollow_works-non-stop.py`in a Unix terminal.

The `sudo` may or may not be necessary if you have administrative privileges, but to err on the safe side  include it.

## Running on a Server
To leave the process running after logging out of a server use the `nohup` command.
`nohup` ignores the Hang Up (HUP) signal that the terminal sends when logging out.

**E.g.**
`nohup sudo python3 massive_follow_then_unfollow_works-non-stop.py &`

To see the output of the script before or after logging out use: `tail -f nohup.out`

## Logs

The InstaPy output for several iterations is logged in **nohup.out**

Information like number of likes, follows and comments is stored in this file for each run of the script.
