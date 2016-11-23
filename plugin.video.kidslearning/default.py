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

addonID = 'plugin.video.stockportcounty'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "UC56cowXhoqRWHeqfSJkIQaA"
YOUTUBE_CHANNEL_ID_2 = "UCKAqou7V9FAWXpZd9xtOg3Q"



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
        title="Bounce Patrol Kids",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="https://yt3.ggpht.com/-P3GrO-qDn8c/AAAAAAAAAAI/AAAAAAAAAAA/WGyon47JL38/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="LittleBabyBum ®",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="https://yt3.ggpht.com/-KLfbkE3zovQ/AAAAAAAAAAI/AAAAAAAAAAA/gMZ_6qxvEXw/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )
		
	
		
		

    
run()
