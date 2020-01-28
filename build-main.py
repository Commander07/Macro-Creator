from cx_Freeze import setup, Executable

base = None    

executables = [Executable("main-copy.py", base=base)]

packages = ["idna","time","os"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "Macro Creator",
    options = options,
    version = "1.7",
    description = 'A Macro creating software',
    executables = executables
)