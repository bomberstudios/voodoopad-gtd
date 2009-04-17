# -*- coding: utf-8 -*-

'''
:Title
Insert @later

:Planguage
Python

:Requires
VoodooPad 3.5+

:Description
Inserts "@later:" in front of the given text.

EOD
'''
VPScriptSuperMenuTitle = "GTD"
VPScriptMenuTitle = "Insert @later"
VPShortcutMask = "control"
VPShortcutKey = "l"

import AppKit

def main(windowController, *args, **kwargs):
    textView = windowController.textView()
    document = windowController.document()

    if textView != None:
        textView.insertText_("@later:")
