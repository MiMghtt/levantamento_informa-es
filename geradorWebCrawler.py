import requests
from bs4 import BeautifulSoup
import operator
from collections import Counter

def start(url):
    #lista para armazenar o conteudo do site
    wordlist = []

    #requisição dos dados da url
    source_code = requests.get(url).text
    #transforma os dados em html
    soup = BeautifulSoup(source_code, 'html.parser')

    #procure tudo o que existe no código em div e classe
    for each_text in soup.findAll('div',{'class': 'entry-content'}):
        #armazena no content como string
        content = each_text.text

        #transformar cada conteudo em uma linha
        words = content.lower().split()

        for each_word in words:
            wordlist.append(each_word)
        clean_wordlist(wordlist)

#função para remover simbolos indesejados 
def clean_wordlist(wordlist):
    clean_list = []
    for word in wordlist:
        symbols = '!@#$%^&*()_-+={}[]|\/;:<>?.,'

        #for para percorrer o array clean list substituindo simbolos indesejados por espaços em branco
        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], '')
    
        if len(word) > 0:
            clean_list.append(word)
    create_dictionary(clean_list)

#dicionario com as palavras mais utilizadas
def create_dictionary(clean_list):
    word_count = {}

    for word in clean_list:
        if word in word_count:
            word_count[word] += 1

        else: 
            word_count[word] = 1

    #contador
    for key, value in sorted(word_count.items(),
                                key = operator.itemgetter(1)):
        print( " % s : % s " % ( key, value))

    c = Counter(word_count)

    top = c.most_common(10)
    print(top)

if __name__ == '__main__':
    start("https://www.geeksforgeeks.org/python-programming-language/?ref=leftbar")