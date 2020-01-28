from cx_Freeze import setup, Executable

base = None    

executables = [Executable("main.py", base=base)]

packages = ["idna","time","ahk"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "Macro",
    options = options,
    version = "1.0",
    description = 'A User created macro',
    executables = executables
)