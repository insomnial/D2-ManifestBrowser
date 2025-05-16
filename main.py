from app.bungiemanifest import DestinyManifest
import PySimpleGUI as sg
import json
import os
import sys


###############################################################################
#
# main()
#
###############################################################################
if __name__ == '__main__':
    # check manifest
    manifest = DestinyManifest().update()
    activityDict = {}
    with open('./cache/DestinyActivityDefinition') as json_file:
        activityDict = json.load(json_file)
        json_file.close()
    

    layout = [
        [sg.Text("Hello World")],
        [sg.Button("OK"), sg.Button("Cancel")],
    ]

    window = sg.Window(title="Hello world", layout=layout, size=(300, 100), finalize=True)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Cancel":
            break
        elif event == "OK":
            print("OK")
        else:
            print(event, values)
    window.close()
    
    pass
