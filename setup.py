import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["scenarios", "texture"], "excludes": ["tkinter"], "optimize": 1, "compressed": True}


setup(  name = "zoe_speech",
        version = "0.1.0",
        description = "El discurso de Zoe",
        options = {"build_exe": build_exe_options},
        executables = [Executable("game.py", base=None)])
