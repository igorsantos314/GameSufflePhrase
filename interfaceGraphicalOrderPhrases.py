from tkinter import *
from tkinter import messagebox
from OrderPhrases import phrase

class interfaceGraphPhrases:

    def __init__(self, P):
        self.P = P
        self.listPhrasesD = P.getlistPhrasesD()
        self.listPhrasesO = P.getlistPhrasesO()

        self.createWindowMain()

    def createWindowMain(self):
        #print(self.P.street)

        #window to menu
        self.window = Tk()
        
        self.window.resizable(False, False)
        self.window.geometry("{0}x{1}+0+0".format(self.window.winfo_screenwidth(), self.window.winfo_screenheight()))
        self.window.title('Game to Learn English')

        #Button Start
        btStart = Button(text='Start Game',  width=25, height=4, font='Arial 15 bold', bg='black', fg='white', command=self.startGame)
        btStart.pack(padx= "10", pady="10")

        #button for choose lange
        btLanguage = Button(text='Choose Language', width=25, height=4, font='Arial 15 bold', bg='black', fg='white', command=self.chooseLanguage)
        btLanguage.pack(padx= "10", pady="10")

        #button exit
        btExit = Button(text='EXIT', width=25, height=4, font='Arial 15 bold', bg='black', fg='white', command=self.window.destroy)
        btExit.pack(padx= "10", pady="10")

        self.window.mainloop()

    def getWindow(self):
        return self.window

    def getPhrasesD(self):
        return self.listPhrasesD

    def getPhrasesO(self):
        return self.listPhrasesO

    def chooseLanguage(self):
        #destroy window
        self.getWindow().destroy()
        
        #functions
        def chLanguage(codLanguage):
            ArqLanguage = open('{}/Language.txt'.format(self.P.currentRoad), 'w')
            ArqLanguage.write(str(codLanguage))
            
            ArqLanguage.close()

        windowLanguage = Tk()
        windowLanguage.title('CHOOSE LANGUAGE')

        #size of Buttons
        sizeWidth = 15
        sizeHeight = 2

        #buttons to choose language
        btEnglish = Button(text='ENGLISH', width=sizeWidth, height=sizeHeight, font='Arial 15 bold', bg='black', fg='white', command=lambda : chLanguage(1))
        btEnglish.pack(padx= "10", pady="5")

        btItalian = Button(text='ITALIAN', width=sizeWidth, height=sizeHeight, font='Arial 15 bold', bg='black', fg='white', command=lambda : chLanguage(2))
        btItalian.pack(padx= "10", pady="5")

        btSpanish = Button(text='SPANISH', width=sizeWidth, height=sizeHeight, font='Arial 15 bold', bg='black', fg='white', command=lambda : chLanguage(3))
        btSpanish.pack(padx= "10", pady="5")

        btFranch = Button(text='FRANCH', width=sizeWidth, height=sizeHeight, font='Arial 15 bold', bg='black', fg='white', command=lambda : chLanguage(4))
        btFranch.pack(padx= "10", pady="5")

        windowLanguage.mainloop()

        #create menu again
        self.createWindowMain()

    #principal window of game
    def startGame(self):
        
        global cont
        cont = 0

        #lista de frase
        currentList = self.getPhrasesD()

        #lista ordenada
        listOrder = self.getPhrasesO()

        #destroy window
        self.getWindow().destroy()
        
        #janela temporaria
        windowTemp = Tk()
        windowTemp.title('Umount the Phrase')
        windowTemp['bg'] = 'black'
        windowTemp.geometry("{0}x{1}+0+0".format(windowTemp.winfo_screenwidth(), windowTemp.winfo_screenheight()))
        
        #new phrase surffle
        lblNewPhrase = Label(text='', font='Arial 30 bold', bg='black', fg='orange')
        lblNewPhrase.pack(padx= "80", pady="50")

        #caixa de texto
        lblYourAnswer = Label(text='Rewrite the Phrase:', font='Arial 15 bold', fg='white', bg='black')
        lblYourAnswer.pack(padx= "10", pady="10")    

        #campo de resposta
        entryAnswer = Entry(font='Arial 30 bold', bg='black', fg='orange')
        entryAnswer.pack(padx= "10", pady="10")

        #funcao de comparação de reposta
        def compareAnswer():
            global cont

            completeWord = ''
            phraseUser = entryAnswer.get().replace(' ','')

            for w in listOrder[cont-1]:
                completeWord += w

            #save complete to show
            msg = 'It was not this time\n -------------------- \nThe correct would be:\n>> {}'.format(completeWord)

            #todas as frases em minusculo para comparar
            completeWord = completeWord.lower().replace(' ','').replace('\n','')
            phraseUser = phraseUser.lower()

            #comparar Respotas
            if completeWord == phraseUser:
                messagebox.showinfo('', 'YOU ARE RIGHT !!')

            else:
                #show mensage
                messagebox.showinfo('', msg)

            entryAnswer.delete(0, END)
            getNewPhrase()

        #voltar para o menu
        def backToMenu():
            windowTemp.destroy()

        def getNewPhrase():
            global cont
            newPhrase = ''

            p = currentList[cont]

            for word in p:
                newPhrase += '{} '.format(word)
            
            lblNewPhrase['text'] = newPhrase.upper()

            cont += 1

        #botao de confirmação
        btConfirmation = Button(text='COMPARE PHRASES', width=25, height=4, font='Arial 15 bold', bg='black', fg='orange', command=compareAnswer)
        btConfirmation.pack(padx= "10", pady="10")

        #botao de back to menu
        btConfirmation = Button(text='BACK TO MENU', width=25, height=4, font='Arial 15 bold', bg='black', fg='white', command=backToMenu)
        btConfirmation.pack(padx= "10", pady="10")

        #pegar primeira frase
        getNewPhrase()
        
        #fecha janela apois fechar a outra
        windowTemp.mainloop()

        self.createWindowMain()

    def setlistPhrasesD(self):
        pass

P = phrase()
interfaceGraphPhrases(P)