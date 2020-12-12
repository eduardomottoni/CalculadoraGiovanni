import PySimpleGUI as sg
sg.theme('DarkBrown6')
#layout
layout = [
    [sg.Text('números a serem calculados'), sg.Input('0',key='box', size=(20,1))],
    [sg.Button(' AC ',key='limpar'), sg.Button('Quad ',key='quad'), sg.Button('Raiz',key='raiz'), 
    sg.Button('apaga',key='apagar')],  
    [sg.Button(' 1  ',key='um'),sg.Button(' 2  ',key='dois'),sg.Button(' 3  ',key='tres'),
    sg.Button(' +  ',key='mais'),sg.Button(' -  ',key='menos')], 
    [sg.Button(' 4  ',key='quatro'),sg.Button(' 5  ',key='cinco'),sg.Button(' 6  ',key='seis'),
    sg.Button(' =  ',key='igual'),sg.Button(' *  ',key='mult')],
    [sg.Button(' 7  ',key='sete'),sg.Button(' 8  ',key='oito'),sg.Button(' 9  ',key='nove'),
    sg.Button(' 0  ',key='zero'),sg.Button(' /  ',key='div')],
    []
]

#janela
class Appnovo():
    def _init_(self):
        self.window = sg.Window('Calculadora', layout=layout,resizable=True,)
        self.result = 0
        self.oper =''
        self.window.read(timeout=1)
        for i in range(1,5):
            for Button in layout[i]:
                Button.expand(expand_x=True,expand_y=True)
#ler eventos
    def resulter(self):
        if oper == '+':
            return float(result) + float(values['box'])
        if oper == '-':
            return float(result) - float(values['box'])
        if oper == '*':
            return float(result) * float(values['box'])
        if oper == '/':
            return float(result) / float(values['box'])
        if oper == '**':
            return float(result) / float(values['box'])
        if oper == '//':
            return float(result) / float(values['box'])



#Manter programa rodando
    while True:
        eventos, values = sg.Windows.read()
        if eventos in (None, sg.WINDOW_CLOSED):
            break  
        if eventos in ('um'):
            if values['box']=='0':
                window['box'].update(value='1')
            else:
                window['box'].update(value=values['box'] + '1')
        if eventos in ('dois'):
            if values['box']=='0':
                window['box'].update(value='2')
            else:
                window['box'].update(value=values['box'] + '2')
        if eventos in ('tres'):
            if values['box']=='0':
                window['box'].update(value='3')
            else:
                window['box'].update(value=values['box'] + '3')
        if eventos in ('quatro'):
            if values['box']=='0':
                window['box'].update(value='4')
            else:
                window['box'].update(value=values['box'] + '4')
        if eventos in ('cinco'):
            if values['box']=='0':
                window['box'].update(value='5')
            else:
                window['box'].update(value=values['box'] + '5')
        if eventos in ('seis'):
            if values['box']=='0':
                window['box'].update(value='6')
            else:
                window['box'].update(value=values['box'] + '6')
        if eventos in ('sete'):
            if values['box']=='0':
                window['box'].update(value='7')
            else:
                window['box'].update(value=values['box'] + '7')
        if eventos in ('oito'):
            if values['box']=='0':
                window['box'].update(value='8')
            else:
                window['box'].update(value=values['box'] + '8')
        if eventos in ('nove'):
            if values['box']=='0':
                window['box'].update(value='9')
            else:
                window['box'].update(value=values['box'] + '9')
        if eventos in ('zero'):
            if values['box']=='0':
                window['box'].update(value='0')
            else:
                window['box'].update(value=values['box'] + '0')
        if eventos in ('limpar'):
            result = 0
            window['box'].update(value= result)
        if eventos in ('apaga'):
            window['box'].update(value= values['box'[:-1]]) 
        if eventos in ('mais'):
            oper != ''
            result=resulter()
        else:
            oper='+'
            result=values['box']
        window['box'].update(value='')
        if eventos in ('menos'):
            oper != ''
            result=resulter()
        else:
            oper='-'
            result=values['box']
        window['box'].update(value='')
        if eventos in ('mult'):
            oper != ''
            result=resulter()
        else:
            oper='*'
            result=values['box']
        window['box'].update(value='')
        if eventos in ('div'):
            oper != ''
            result=resulter()
        else:
            oper='/'
            result=values['box']
        window['box'].update(value='')
        if eventos in ('quad'):
            oper != ''
            result=resulter()
        else:
            oper='**'
            result=values['box']
        window['box'].update(value='')
        if eventos in ('raiz'):
            oper != ''
            result=resulter()
        else:
            oper='//'
            result=values['box']
        window['box'].update(value='')
        if eventos in ('igual'):
            result= resulter()
            window['box'].update(value=result)
            result=0
            oper= ''
