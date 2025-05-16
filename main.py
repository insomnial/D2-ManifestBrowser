from app.bungiemanifest import DestinyManifest

###############################################################################
#
# main()
#
###############################################################################
if __name__ == '__main__':
    # check manifest
    manifest = DestinyManifest().update()
