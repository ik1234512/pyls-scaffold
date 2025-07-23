# Imports make the mentioned "modules" accessible to the code within
# this file, which is itself a "module".
import argparse
import os
import time 


def main() -> None:
    parser = argparse.ArgumentParser(prog="pyls", description="A baby version of ls.")

    # We now add descriptions for the expected arguments for our program.
    parser.add_argument(
        "dirname",
        nargs="?",  # Indicates that either 0 or one directory name can be given.
        default=".",  # Gives the default value to use when this argument is not given.
        # '.' means "current directory".
        help="The name of the directory whose contents are to be listed.",
    )
    parser.add_argument(
        "-l",
        "--longform",
        action="store_true",  # Indicates that the value is a boolean and no further
        # values need to be supplied on the command line.
        default=False,  # This is not really needed as False is the default already
        # when -l is not given on the command line. Including it
        # for illustration.
        help="Prints details about each file in the format -\n"
        "<timestamp> <filesize> <filename>",
    )
    parser.add_argument(
        "-F",
        "--formatted",
        action="store_true",
        default=False,
        help="Adds a character to tell you whether its a file or a directory.",
    )

    # Now we ask argparse to use the above information to interpret the
    # arguments and give us an object which will have `.dirname`,
    # `.longform` and `/.formatted` attributes we can access instead of
    # having to check for all the combinations ourselves.
    # Furthermore, if you call your program with either the `-h` or `--help``
    # flag, it will print out all of the specification above in a nice format
    # as help. This is a convention employed by most command line programs.
    args = parser.parse_args()
    pyls(args.dirname, args.longform, args.formatted)
    



def pyls(dirname: str, longform: bool, formatted: bool) -> None:
    """
    PURPOSE
    -------
    Prints the contents of the given directory.

    - :param dirname: The path to the directory whose contents are to be listed.
    - :param longform: If True, show detailed file info like modification time and size.
    - :param formatted: If True, append '/' to directories and '*' to executable files.

    EXAMPLES    
    --------
    pyls(".", False, False)
    pyls("myfolder", True, False)
    pyls("/usr", False, True)
    pyls(".", True, True)
    """

    entries = os.listdir(dirname)
    for entry in sorted(entries):
        path = os.path.join(dirname, entry)

        marker = ""
        if formatted:
            if os.path.isdir(path):
                marker = "/"
            elif os.access(path, os.X_OK):
                marker = ""

        elif longform:
            stats = os.stat(path)
            timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(stats.st_mtime))
            size = stats.st_size
            print(f"last accessed{timestamp}, size {size:>10} {entry}{marker}")
        else:
            print(f"{entry}{marker}")



# A python module may be loaded in one of two ways --
# 1. `python myfile.py`: In this case, the python file/module is considered to be
#    a "main program" and is named "__main__" within. So if you want to run code
#    only in this mode, you check whether __name__ is "__main__" and run that code.
# 2. `import myfile`: (within some other python file). In this mode, it is a pure
#    "module" that exposes functions and values via `myfile.` notation within the
#    importing python file. In this case, __name__ will be "myfile" and not "__main__".
if __name__ == "__main__":
    main()

