--[[
VPLanguage = lua
VPScriptMenuTitle = Insert Date
VPShortcutKey = J
VPShortcutMask = control
VPEndConfig
--]]

-- check out http://www.lua.org/pil/22.1.html for more formatting options.

textView = windowController:textView()
document = windowController:document()

dateFormat = os.date("%Y%m%d", os.time())

if textView ~= nil then
    textView:insertText(dateFormat)
end