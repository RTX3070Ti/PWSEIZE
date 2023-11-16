from flask import Flask, render_template
import hashlib
import json
import random
from time import time






app = Flask(__name__)



@app.route('/')
def home():
    

    class Block_chain(object):
        def __init__(self):
            self.chain = []
            self.pendingTransactions = []
            #Blok 1

            self.newBlock(previousHash="Profielwerkstuk Informatica door Eize", blok=1)

        def newBlock(self, blok, previousHash=None):
            the_block = {
                'index': len(self.chain) + 1,
                'tijdsverloop': time(), #Unix tijd 1970 1 jan
                'transacties': self.pendingTransactions,
                'eitje': blok,
                'vorige_hash': previousHash or self.hash(self.chain[-1]),
            }
            self.pendingTransactions = []
            self.chain.append(the_block)
            return the_block

        @property
        def laatsteblok(self):
            return self.chain[-1]

        def newTransaction(self, verstuurder, ontvanger, waarde):
            transactie = {
                'verstuurder': verstuurder,
                'ontvanger': ontvanger,
                'waarde': waarde
            }
            self.pendingTransactions.append(transactie)
            return self.laatsteblok['index'] + 1

        def hash(self, blok):
            stringObject = json.dumps(blok, sort_keys=True)
            blockString = stringObject.encode()

            rawHash = hashlib.sha256(blockString)
            hexHash = rawHash.hexdigest()

            return hexHash
        
    namen = ["Eize", "Gert-Jan", "Henk", "Gerda", "Derk", "Berend", "Joost", "Jan", "Erik", "Jan-Pieter", "Jan-Willem", "Peter", "Abe", "Abel", "Auke", "Bart", "Benjamin", "Rik", "Barteld", "Axel", "Balthazar", "Gerrie", "Geert", "Emmanuel", "Destiny", "Rikie", "Hedwig", "Ludwig", "Ignas", "Hermen", "Jozef", "Jurriaan", "Karel", "Kees", "Nasser", "Jona", "Nikita", "Ezra", "Jofanna", "Diederik", "Enno", "Moris", "Achnes", "Lodewijk", "Jorrik", "Themus", "Patrick", "Ruud", "Siebren", "Stephan", "Johannes", "Sander", "Egbert-Jan"]
    
    def randomnaam(namen):
        if namen: 
            random_index = random.randint(0, len(namen) - 1)
            gekozen = namen[random_index]
            namen.pop(random_index)
            return gekozen
        else:
            "error"

    

    def naam():
        random_name = randomnaam(namen)
        return random_name
    
   
   
    block_chain = Block_chain()
    #Blok 2 

    transaction1 = block_chain.newTransaction(naam(), naam(), '50 EI') 
    transaction2 = block_chain.newTransaction(naam(), naam(), '20 EI')
    transaction3 = block_chain.newTransaction(naam(), naam(), '5 EI')
    transaction4 = block_chain.newTransaction(naam(), naam(),'4 EI')
    transaction5 = block_chain.newTransaction(naam(), naam(),'7 EI')
    block_chain.newBlock(2)
    print()
    #Blok 3
    transaction6 = block_chain.newTransaction(naam(), naam(), '3 EI')
    transaction7 = block_chain.newTransaction(naam(), naam(), '2 EI')
    transaction8 = block_chain.newTransaction(naam(), naam(), '4 EI')
    transaction9 = block_chain.newTransaction(naam(), naam(), '14 EI')
    transaction10 = block_chain.newTransaction(naam(), naam(), '5 EI')
    block_chain.newBlock(3)
    print()

    #Blok 4
    transaction11 = block_chain.newTransaction(naam(), naam(), '8 EI')
    transaction12 = block_chain.newTransaction(naam(), naam(), '2 EI')
    transaction13 = block_chain.newTransaction(naam(), naam(), '3 EI')
    transaction14 = block_chain.newTransaction(naam(), naam(), '17 EI')
    transaction15 = block_chain.newTransaction(naam(), naam(), '5 EI')
    block_chain.newBlock(4)
    print()

    #Blok 5
    transaction16 = block_chain.newTransaction(naam(), naam(), '3 EI')
    transaction17 = block_chain.newTransaction(naam(), naam(), '1 EI')
    transaction18 = block_chain.newTransaction(naam(), naam(), '2 EI')
    transaction19 = block_chain.newTransaction(naam(), naam(), '10 EI')
    transaction20= block_chain.newTransaction(naam(), naam(), '6 EI')
    block_chain.newBlock(5)
    print()

    
    
    
    return render_template('blockchain.html', blockchain=block_chain.chain)








if __name__ == "__main__":
    app.run(debug=True)
    
    
