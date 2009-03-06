# A Python plugin for VoodooPad.
# It searches for tag_name appearances in your document and adds the text after it to
# a new list_page page.

VPScriptSuperMenuTitle = "GTD"
VPScriptMenuTitle = "Update @later list"
VPShortcutKey = "L"
VPShortcutMask = "control"

import time

tag_name = "@later"

def main(windowController, *args, **kwargs):
  theList = ""
  document = windowController.document()
  for key in document.keys():
    page = document.pageForKey_(key)
    if page.uti() == "com.fm.page":
      attString = page.dataAsAttributedString()
      for line in attString.mutableString().splitlines():
        if line.find(tag_name) >= 0:
          theList = theList + page.displayName() + line.partition(tag_name)[2] + "\n"
  theList = theList + "\n\n--\nUpdated at " + time.strftime("%d %b %Y %H:%M",time.localtime())
  page = document.createNewPageWithName_(tag_name)
  page.setDataAsString_(theList)
  document.openPageWithTitle_(tag_name)