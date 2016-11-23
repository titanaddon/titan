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

YOUTUBE_CHANNEL_ID_1 = "UCnplU6iJ1idANM6VpQuEm-w"
YOUTUBE_CHANNEL_ID_2 = "UCpVm7bg6pXKo1Pr6k5kxG9A"


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
        title="Documentary TV",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="https://i.ytimg.com/vi/JE6f4S_amfg/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="National Geographic",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="https://i.ytimg.com/vi/KpDghmRR68Y/hqdefault.jpg?custom=true&w=320&h=180&stc=true&jpg444=true&jpgq=90&sp=68&sigh=Mmj3gqqb4G-Zuacxiyw0Eb5iYiY",
        folder=True )

    
run()
