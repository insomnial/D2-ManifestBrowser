from app.bungiemanifest import DestinyManifest
import PySimpleGUI as sg
import json

###############################################################################
#
# Functions
#
###############################################################################
def _loadJsonFileIntoDictionary(filePath : str):
    # load json file into dictionary
    with open(filePath) as json_file:
        data = json.load(json_file)
        json_file.close()
    return data

def _mapNamesToHashes(aDictionary : dict):
    # map names to hashes
    # get the name and hash from the json blob
    # return a dictionary of names to hashes
    nameHashDict = {}
    for item in aDictionary.keys():
        item = aDictionary[item]
        displayProperties = item['displayProperties']
        if 'name' not in displayProperties.keys():
            continue
        name = item['displayProperties']['name']
        hash = str(item['hash'])
        nameHashDict[name] = hash
    sortedKeys = sorted(nameHashDict.keys())
    return {name: nameHashDict[name] for name in sortedKeys}

def _convertJsonToTree(aJson : dict, aTree : sg.TreeData):
    for key in aJson.keys():
        item = aJson[key]
        if item is dict:
            # TODO keep going with dictionaries
            pass
        # ( PARENT, KEY, TEXT, VALUE)
        aTree.Insert("", key, key, item)
        

###############################################################################
#
# main()
#
###############################################################################
if __name__ == '__main__':
    # check manifest and load if out of date
    manifest = DestinyManifest().update()
    # build dictionaries of activity types and definitions
    activityTypeDict = _loadJsonFileIntoDictionary('./cache/DestinyActivityTypeDefinition')
    activityDefinitionDict = _loadJsonFileIntoDictionary('./cache/DestinyActivityDefinition')

    # build mapping of activity types to hashes
    mapActivityTypeNameToHash = _mapNamesToHashes(activityTypeDict)
    mapActivityDefinitionNameToHash = _mapNamesToHashes(activityDefinitionDict)

    # map activities to their type-hash
    # given a type of activity, get the names of the activities of that type
    mapTypehashToActivityHash = {}
    for key in activityDefinitionDict.keys(): # for each activity
        activity = activityDefinitionDict[key] # get activity properties
        activityTypeHash = str(activity['activityTypeHash']) # get activity type hash for this activity
        if activityTypeHash not in mapTypehashToActivityHash.keys(): # if the type hash is not in the map
            mapTypehashToActivityHash[activityTypeHash] = [] # create a new list for this type hash
        mapTypehashToActivityHash[activityTypeHash].append(str(activity['hash']))

    treedata = sg.TreeData()

    treedata.Insert("", '_A_', 'A', [1, 2, 3])
    treedata.Insert("", '_B_', 'B', [4, 5, 6])
    treedata.Insert("_A_", '_A1_', 'A1', ['can', 'be', 'anything'])
    treedata.Insert("_B_", '_B1_', 'B1', ['can', 'be', 'anything'])
    treedata.Insert("_A1_", '_A2_', 'A2', ['can', 'be', 'anything', 'even'])

    layout = [
        [
            sg.Combo([*mapActivityTypeNameToHash.keys()], enable_events=True, key="ac_type"),
            sg.Combo([*mapActivityDefinitionNameToHash.keys()], enable_events=True, key="ac_definition")
        ],
        # [
        #     sg.Multiline("Type", key="ml_type", size=(80,30)),
        #     sg.Multiline("Definitions", key="ml_definition", size=(100,30))
        # ],
        [
            sg.Tree(treedata, key="tr_type", headings=["1", "2", "3", "4", "5"], auto_size_columns=True),
            sg.Tree(treedata, key="tr_definition", headings=["1", "2", "3", "4", "5"], auto_size_columns=True)
        ],
        [sg.Button("Close", key="Close")]
    ]

    window = sg.Window(title="Destiny Manifest Viewer", layout=layout, finalize=True, resizable=True)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Close":
            break
        elif event == "OK":
            print("OK")
        elif event == "ac_type":
            filteredActivityHashes = mapTypehashToActivityHash[mapActivityTypeNameToHash[values[event]]]
            filteredActivityNames = [((activityDefinitionDict[item])['displayProperties'])['name'] for item in filteredActivityHashes]
            filteredActivityNames = sorted(filteredActivityNames)
            itemString = json.dumps(activityTypeDict[mapActivityTypeNameToHash[values[event]]], indent=2)
            print(itemString)
            itemJson = activityTypeDict[mapActivityTypeNameToHash[values[event]]]
            itemTree = _convertJsonToTree(itemJson, sg.TreeData())
            window["tr_type"].update(itemTree)
            # window["ml_type"].update(itemString)
            # window["ml_definition"].update("") # reset the definition text when the type changes
            # window["ac_definition"].update(value = '', values = [*filteredActivityNames]) # reset the definition combo when the type changes
        elif event == "ac_definition":
            itemString = json.dumps(activityDefinitionDict[mapActivityDefinitionNameToHash[values[event]]], indent=2)
            print(itemString)
            itemJson = activityDefinitionDict[mapActivityDefinitionNameToHash[values[event]]]
            itemTree = _convertJsonToTree(itemTree, sg.TreeData())
            window["tr_definition"].update(itemTree)
            # window["ml_definition"].update(itemString)
        else:
            print(event, values)
    window.close()
    