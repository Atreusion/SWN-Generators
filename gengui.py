import sys  
if sys.version_info[0] >= 3:  
    import PySimpleGUI as sg  
else:  
    import PySimpleGUI27 as sg  
  
layout = [[sg.Text('Choose generator:')],  
          [sg.InputCombo(('NPC', 'Problem', 'Urban', 'Wilderness'), size=(20, 1), key='_IN_')],
          [sg.Multiline('Generator info', size=(45,10), key='_OUTPUT_')]
          [sg.Button('Roll'), sg.Button('Exit')]]  
  
window = sg.Window('SWN Generator').Layout(layout)  
  
while True:                 # Event Loop  
    event, values = window.Read()  
    print(event, values)
    if event is None or event == 'Exit':  
        break  
    if event == 'Roll' and values['_IN_'] == ['NPC']:
        output = npcgen()
    if event == 'Roll' and values['_IN_'] == ['Problem']:
        output = problemgen()
    if event == 'Roll' and values['_IN_'] == ['Urban']:
        output = urbangen()
    if event == 'Roll' and values['_IN_'] == ['Wilderness']:
        output = wildernessgen()
    window.FindElement('_OUTPUT_').Update(output)

window.Close()
