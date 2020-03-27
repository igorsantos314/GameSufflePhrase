from random import sample
import os

class phrase:

    def __init__(self):
        self.currentRoad = '/home/igor/Área de trabalho/GameEnglish'

        #lista de frases Ordenadas e Deseordenadas
        self.listPhrasesD = []
        self.listPhrasesO = []

        #pegar frases e armazenar na listPhrasesD
        self.getPhrasesArq()

        #embaralha a lista
        self.orderList()

        #guarda a nova lista embaralhada
        self.listPhrasesO = self.getlistPhrasesD().copy()

        #modifcar as palavras da listaOrdenada
        self.modifyWords()

    def setlistPhrasesD(self, newPhrase):
        #adiciona uma nova frase a ListaD
        self.listPhrasesD.append(newPhrase)

    def getlistPhrasesD(self):
        #retorna a listPhrasesD
        return self.listPhrasesD

    def setlistPhrasesO(self, newPhrase):
        #adiciona uma nova frase a ListaO
        self.listPhrasesO.append(newPhrase)

    def getlistPhrasesO(self):
        #retorna a listPhrasesO
        return self.listPhrasesO

    def changeListPhrase(self, newList):
        #seta a ListaD com as palavras embaralhadas
        self.listPhrasesD = newList
        
    def orderList(self):
        #mistura as frases da lista
        numberElements = len(self.getlistPhrasesD())
        self.changeListPhrase( sample(self.getlistPhrasesD(), numberElements) )
    
    def orderWords(self, Phrases):
        #embaralha as palavras da frase
        numberWords = len(Phrases)
        return sample(Phrases, numberWords)

    def getWords(self, Phrase, typeWords):

        posInit = 0
        listWords = []

        #varrer frases da lista
        for pos,i in enumerate(Phrase):
            word = ''

            #verrifica onde esta o espaco e varrer de posInit ate Pos
            if i == ' ':
                
                #adiona letras da palavra
                for i in range(posInit, pos):
                    word += Phrase[i]
                    
                #adiciona as palavras a lista
                listWords.append(word)
                posInit = pos+1

        #vefirica se deseja adcionar ja embaralhada
        if typeWords:
            return self.orderWords(listWords)
        
        return listWords
    
    def getLanguageArq(self):
        dictLanguage = {1:'English', 2:'Italian', 3:'Spanish', 4:'Franch'}

        ArqLanguage = open('{}/Language.txt'.format(self.currentRoad))

        pos = 0

        #get id language
        for i in ArqLanguage:
            pos = int(i)

        ArqLanguage.close()

        #return dir of Language
        currentRoad = '/home/igor/Área de trabalho/GameEnglish/{}/Phrases.txt'.format(dictLanguage[pos])

        return currentRoad

    def getPhrasesArq(self):
        #Arquivo com as frases
        ArqPhrases = open('{}'.format(self.getLanguageArq()), 'r', encoding='latin-1')

        for i in ArqPhrases:
            if i == '' or i == '\n':
                pass

            else:
                #adiciona frase a ListaD
                self.setlistPhrasesD(i)
                
        ArqPhrases.close()

    def modifyWords(self):

        newList = []

        #lista de frase e desordenar
        for i in self.getlistPhrasesD():
            i = i.replace('\n', ' ')

            #retorna frase desordenada
            element = self.getWords(i, True)

            newList.append(element)
        
        #modifica a lista anterior
        self.changeList(newList)

    def changeList(self, newList):
        #modifica a listaD por uma com palavras embaralhadas
        self.listPhrasesD = newList.copy()

P = phrase()
lista = P.getlistPhrasesD()
