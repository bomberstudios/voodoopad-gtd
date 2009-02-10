--[[
VPLanguage = lua
VPScriptSuperMenuTitle = GTD
VPScriptMenuTitle = Insert @done
VPShortcutKey = d
VPShortcutMask = control
VPEndConfig
--]]

-- check out http://www.lua.org/pil/22.1.html for more formatting options.

textView = windowController:textView()
document = windowController:document()

if textView ~= nil then
    textView:insertText("@done:")
end