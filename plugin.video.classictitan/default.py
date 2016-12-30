# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Jesse Ventura Addon by coldkeys
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#
# Author: coldkeys
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.spinninrecords'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "PLX9_I-EOJPdFuOjcI2zkmTck55homHEBE"
YOUTUBE_CHANNEL_ID_2 = "PLlZ10h1bYswNr7BWSKrXlbfg5ByJV48xI"
YOUTUBE_CHANNEL_ID_3 = "PLZXL7dfsQQpbxDCjR_Clj1nliPOuFtK2L"



# Entry point
def run():
    plugintools.log("docu.run")
    
    # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    
    plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("docu.main_list "+repr(params))

    plugintools.add_item( 
        #action="", 
        title="Old Movies 1",
         url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="https://i.imgsafe.org/1d49e98da1.jpg",
        folder=True )  


    plugintools.add_item( 
        #action="", 
        title="Old Movies 2",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="https://i.imgsafe.org/1d49e98da1.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Bollywood Old Movies",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="https://i.imgsafe.org/1d371807da.jpg",
        folder=True )
		
		
run()
