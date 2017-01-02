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

YOUTUBE_CHANNEL_ID_1 = "PLU12uITxBEPEoCeVvq344LJGtNQxrqyTJ"
YOUTUBE_CHANNEL_ID_2 = "PL8fVUTBmJhHIegh7kgk6KsyLJ7miRBKpO"
YOUTUBE_CHANNEL_ID_3 = "PL57quI9usf_uLyWHLNz5yGH2qfbn8HMFo"



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
        title="live Most Vieved",
         url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="https://yt3.ggpht.com/BQSIiLDxZiZpzR4C6pK-NKkKOv3fsPsWuKVJxpmYCnEASI8W5pglXP1vF30D98doHzsP_JwPLycrfd-FFnw=s100-nd-c-c0xffffffff-rj-k-no",
        folder=True )  


    plugintools.add_item( 
        #action="", 
        title="Live Now  Sports",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="https://yt3.ggpht.com/BQSIiLDxZiZpzR4C6pK-NKkKOv3fsPsWuKVJxpmYCnEASI8W5pglXP1vF30D98doHzsP_JwPLycrfd-FFnw=s100-nd-c-c0xffffffff-rj-k-no",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Live Now Technology",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="https://yt3.ggpht.com/BQSIiLDxZiZpzR4C6pK-NKkKOv3fsPsWuKVJxpmYCnEASI8W5pglXP1vF30D98doHzsP_JwPLycrfd-FFnw=s100-nd-c-c0xffffffff-rj-k-no",
        folder=True )
		
		
run()
