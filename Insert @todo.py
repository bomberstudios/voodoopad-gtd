# -*- coding: utf-8 -*-

'''
:Title
Insert @todo

:Planguage
Python

:Requires
VoodooPad 3.5+

:Description
Inserts "@todo:" in front of the given text.

EOD
'''
VPScriptSuperMenuTitle = "GTD"
VPScriptMenuTitle = "Insert @todo"
VPShortcutMask = "control"
VPShortcutKey = "t"

import AppKit

def main(windowController, *args, **kwargs):
    textView = windowController.textView()
    document = windowController.document()

    if textView != None:
        textView.insertText_("@todo:")
