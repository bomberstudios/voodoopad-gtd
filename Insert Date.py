# -*- coding: utf-8 -*-

'''
:Title
Insert Date

:Planguage
Python

:Requires
VoodooPad 3.5+

:Description
Inserts Date

EOD
'''
VPScriptSuperMenuTitle = "GTD"
VPScriptMenuTitle = "Insert Date"
VPShortcutMask = "control"
VPShortcutKey = "J"

import AppKit
import time

def main(windowController, *args, **kwargs):
    textView = windowController.textView()
    document = windowController.document()

    if textView != None:
        dateFormat = time.strftime("%Y%m%d")
        textView.insertText_(dateFormat)

