#!/usr/bin/python
# -*- coding: utf-8 -*-
import xbmcaddon
import xbmcplugin
import xbmcgui
import sys
import urllib, urllib2
import re

pluginhandle = int(sys.argv[1])

def index():
          addDir("UKF","","index1","")
          addDir("UKF Live","","index2","")
          addDir("UKF Drum & Bass","","index3","")
          addDir("UKF Dubstep","","index4","")
          addDir("UKF Mixes","","index5","")
          addDir("Drum&Bass TV","","index6","")
          addDir("GetDarker","","index7","")
          addDir("SubSoul","","index8","")
          xbmcplugin.endOfDirectory(pluginhandle)

def index1():
        xbmc.executebuiltin('Container.Update(plugin://plugin.video.youtube/channel/UC9UTBXS_XpBCUIcOG7fwM8A/)')

def index2():
        xbmc.executebuiltin('Container.Update(plugin://plugin.video.youtube/channel/UCpYkkFDnvHka9CBuwxPpqXw/)')

def index3():
        xbmc.executebuiltin('Container.Update(plugin://plugin.video.youtube/channel/UCr8oc-LOaApCXWLjL7vdsgw/)')

def index4():
        xbmc.executebuiltin('Container.Update(plugin://plugin.video.youtube/channel/UCfLFTP1uTuIizynWsZq2nkQ/)')

def index5():
        xbmc.executebuiltin('Container.Update(plugin://plugin.video.youtube/channel/UC-C1osqKCLSKUWhIMkSwt4w/)')

def index6():
        xbmc.executebuiltin('Container.Update(plugin://plugin.video.youtube/channel/UCMaoxh46hAsqlaVk2HcZkcg/)')

def index7():
        xbmc.executebuiltin('Container.Update(plugin://plugin.video.youtube/channel/UCi-bKESYc_sboCSqBjw43sg/)')

def index8():
        xbmc.executebuiltin('Container.Update(plugin://plugin.video.youtube/channel/UCO3GgqahVfFg0w9LY2CBiFQ/)')

def playVideo(youtubeID):
        fullData = "plugin://plugin.video.youtube/?path=/root/video&action=play_video&videoid=" + youtubeID
        listitem = xbmcgui.ListItem(path=fullData)
        return xbmcplugin.setResolvedUrl(pluginhandle, True, listitem)

def getUrl(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; rv:11.0) Gecko/20100101 Firefox/13.0')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        return link

def addLink(name,url,mode,iconimage,desc,date):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": desc, "Date": date} )
        liz.setProperty('IsPlayable', 'true')
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz)
        return ok

def addDir(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok

def parameters_string_to_dict(parameters):
    ''' Convert parameters encoded in a URL to a dict. '''
    paramDict = {}
    if parameters:
        paramPairs = parameters[1:].split("&")
        for paramsPair in paramPairs:
            paramSplits = paramsPair.split('=')
            if (len(paramSplits)) == 2:
                paramDict[paramSplits[0]] = paramSplits[1]
    return paramDict

params=parameters_string_to_dict(sys.argv[2])
mode=params.get('mode')
url=params.get('url')
if type(url)==type(str()):
  url=urllib.unquote_plus(url)

if mode == 'playVideo':
    playVideo(url)

elif mode == 'index1':
    index1()
elif mode == 'index2':
    index2()
elif mode == 'index3':
    index3()
elif mode == 'index4':
    index4()
elif mode == 'index5':
    index5()
elif mode == 'index6':
    index6()
elif mode == 'index7':
    index7()
elif mode == 'index8':
    index8()
else:
    index()