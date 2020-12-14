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

          addDir("Kliemannsland","","index1","")

          addDir("Fynn Kliemann","","index2","")

          addDir("fimbim","","index3","")

          xbmcplugin.endOfDirectory(pluginhandle)



def index1():

        xbmc.executebuiltin('Container.Update(plugin://plugin.video.youtube/channel/UCLKPfqBGqL4gaEvegb_If0Q/)')



def index2():

        xbmc.executebuiltin('Container.Update(plugin://plugin.video.youtube/channel/UCa_MF1hIC-oCTsEJDegmaIQ/)')



def index3():

        xbmc.executebuiltin('Container.Update(plugin://plugin.video.youtube/channel/UCnmLEDLAhktj4IKDce64N_w/)')




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

else:

    index()