import keyboard 
import pyperclip as clipboard
import re 
import time
import os

clipboardHist = [clipboard.paste()]

registers = { 'j' : [r'SAP\-\d+',['jira.com/SAP-999']]}

# register all abbreviation with v<register> followed by space paste last entry
for  key in registers.keys():
    abbbrev = keyboard.add_abbreviation('v'+str(key), registers[key][1][0]) 
    registers[key].append(abbbrev)


def updateRegisters(clipboardText):
    for key in registers.keys():
        findAll = re.findall(registers[key][0],clipboardText)
        if len(findAll) > 0:
            registers[key][1].insert(0,findAll[0])
            keyboard.remove_word_listener(registers[key][2])
            abbbrev = keyboard.add_abbreviation('v'+str(key), findAll[0])
            registers[key][2] = abbbrev
            return

def printRegisters():
    for r in registers:
        print('top 5 of',r)
        for i,e in enumerate(registers[r][1][:5]):
            print('\t',i,e)
while True:
    text = clipboard.paste()
    if text != clipboardHist[-1]:
        os.system('cls')
        clipboardHist.append(text)
        updateRegisters(text)
        printRegisters()
    time.sleep(0.1)

