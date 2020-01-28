from cx_Freeze import setup, Executable

base = None    

executables = [Executable("output.py", base=base)]

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
    description = 'User created macro',
    executables = executables
)