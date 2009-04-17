# -*- coding: utf-8 -*-

'''
:Title
Update @later List

:Planguage
Python

:Requires
VoodooPad 3.5+

:Description
Searches for @later appearances in your document and adds the text after it to a new page listing them.

EOD
'''
VPScriptSuperMenuTitle = "GTD"
VPScriptMenuTitle = "Update @later List"
VPShortcutKey = "L"
VPShortcutMask = "control"

import AppKit
import time

tag_name = "@later"

def main(windowController, *args, **kwargs):
    theList = ""
    document = windowController.document()
    for key in document.keys():
        page = document.pageForKey_(key)
        if page.uti() == "com.fm.page":
            attString = page.dataAsAttributedString()
            if attString.mutableString().find(tag_name) >= 0:
                for line in attString.mutableString().splitlines():
                    if line.find(tag_name) >= 0:
                        theList += page.displayName() + line.partition(tag_name)[2] + "\n"
    theList += "\n\n--\nUpdated at " + time.strftime("%d %b %Y %H:%M",time.localtime())
    page = document.createNewPageWithName_(tag_name)
    page.setDataAsString_(theList)
    document.openPageWithTitle_(tag_name)
