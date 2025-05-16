# Messing around with python GUI
Trying to get some GUI experience using python and Destiny manifest files.

## Prereq

### tkinter required by pysimplegui

#### linux
`sudo apt install python3-tk`

#### windows
`installed with python installer`

#### macos
Requires homebrew already installed.
`ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`
`brew install python3`
`brew install python-tk`

### PySimpleGUI
`python -m pip install --upgrade --extra-index-url https://PySimpleGUI.net/install PySimpleGUI`
### python requirements
`pip install -r requirements.txt`

## PySimpleGUI
Special things required by PySimpleGUI but should be included in `requirements.txt` during normal install. This is mostly for documentation. --
PySimpleGUI is now located on a private PyPI server.  Please add to your pip command: -i https://PySimpleGUI.net/install

The version you just installed should uninstalled:
   `python -m pip uninstall PySimpleGUI`
   `python -m pip cache purge`

Then install the latest from the private server:
`python -m pip install --upgrade --extra-index-url https://PySimpleGUI.net/install PySimpleGUI`

You can also force a reinstall using this command and it'll install the latest regardless of what you have installed currently
`python -m pip install --force-reinstall --extra-index-url https://PySimpleGUI.net/install PySimpleGUI`
