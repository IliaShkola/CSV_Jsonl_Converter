# my_app.spec

# -----------------------------------------------------------------------------
# PyInstaller Spec File for "CSV-JSONL Converter" with PyQt5
# Optimizations included (onefile, UPX, excludes, etc.)
# -----------------------------------------------------------------------------

# Import PyInstaller building blocks
import PyInstaller.__main__
from PyInstaller.utils.hooks import collect_submodules
from PyInstaller.utils.hooks import collect_data_files
from PyInstaller.building.build_main import Analysis, PYZ, EXE, COLLECT
from PyInstaller.building.datastruct import TOC
from PyInstaller.compat import is_win, is_darwin, is_linux

# -----------------------------------------------------------------------------
# App/Main file configuration
# -----------------------------------------------------------------------------
app_name = "CSV_JSONL_Converter"
main_script = "app.py"   # replace with the actual name of your main script
icon_file = None            # e.g. "icon.ico" for Windows, if you have an icon

# -----------------------------------------------------------------------------
# Gather hidden imports if needed (e.g., PyQt5 submodules)
# If you run into "ModuleNotFoundError" for certain PyQt5 submodules,
# you can add them here or use auto-collection like below.
# -----------------------------------------------------------------------------
hidden_imports = collect_submodules('PyQt5')  # Attempt to handle hidden Qt modules

# -----------------------------------------------------------------------------
# Collect any data files you might need (icons, resources, etc.)
# For basic usage, you might not need this. If so, leave it empty or comment out.
# -----------------------------------------------------------------------------
datas = []

# -----------------------------------------------------------------------------
# Excludes for optimization (remove libraries you don't need)
# -----------------------------------------------------------------------------
excludes = [
    'numpy',
    'matplotlib',
    'tkinter',
    'scipy',
    'pandas',
    'unittest',
    'distutils',
    'setuptools',
    'pytest',
    # Add more that are not used in your project to reduce size
]

# -----------------------------------------------------------------------------
# Analysis: main step that inspects your script, dependencies, etc.
# -----------------------------------------------------------------------------
a = Analysis(
    scripts=[main_script],
    pathex=[],                    # Additional paths if needed
    binaries=[],
    datas=datas,
    hiddenimports=hidden_imports,
    hookspath=[],
    runtime_hooks=[],
    excludes=excludes,
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=None,
    noarchive=False
)

# -----------------------------------------------------------------------------
# PYZ: Creates the .pyz archive with your Python bytecode
# -----------------------------------------------------------------------------
pyz = PYZ(a.pure, a.zipped_data, cipher=None)

# -----------------------------------------------------------------------------
# EXE: Build the final executable
# -----------------------------------------------------------------------------
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    name=app_name,
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,            # On Windows, strip=True can break certain packages, try carefully
    upx=True,               # Enable UPX compression (make sure UPX is installed)
    console=False,          # Set to True if you want a console window
    icon=icon_file
)

# -----------------------------------------------------------------------------
# COLLECT: (Optional) sometimes used in one-folder mode, but we are aiming for onefile
# If using onefile, we only need to produce the EXE above.
# -----------------------------------------------------------------------------
