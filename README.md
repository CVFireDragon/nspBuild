# nspBuild
Community Mod of rkk's nspBuild

Convert NCA to NSP Format using Python

# Note:
This tool is just for packing NCAs into NSP and it doesn't touch NCAs (if they don't run, it's not this tool's fault, just NCAs don't pass switch checks or they are corrupted)

# Documentation
This tool takes your NCA file and changes the header to a PFS0 format (also changes a few other things), then builds an NSP file from the changes it made.

# Usage
1. Download the compiled executable file (exe), or Python script (py)

2. Open CMD in the py/exe's directory and run ``nspBuild out.nsp main main.npdm``

Example: ``nspBuild out.nsp main main.npdm``

(obviously, replace the ()'s with whatever it says to)

# Credits

@lunalik2 for the .exe files (for people without Python) (#5) and working on a GUI. (#7)

@roothorick for making nspBuild usable in scripts. (#3)

@shchmue for porting it to Python 2. (#2)

# Compiling / Building the executable

See https://github.com/CVFireDragon/nspBuild/blob/master/HowToCompile.md
