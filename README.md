# ClipboardRegisters
Enhacement of windows Clipboard

## idea
Like nvim have registers defined in the background of windows. 
Everytime something gets copied into the clipboard ClipboardRegisteres descides on regular expressions to store give string in a "register".
A datastore is formed were data from the clipboard is order within registers ex.:
* Reg_J : all jira urls
* Reg_C : all confluence urls
* Reg_P : all python code

later on last entry from regster can be pasted via some command.
