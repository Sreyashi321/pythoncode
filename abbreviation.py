'''text = input('Enter a string: ')
#index of first space
space1 = text.find(' ')
#index of second space
space2 = text.find(' ',space1+1)
newtext = text[0] +'. '  + text[space1+1] +'. ' + text[space2+1] +'.'
print('New string:', newtext)'''

def abbre(name):
    abbreviation=""
    word=name.split()
    for i in word:
        abbreviation +=i[0].upper().lower()
    return abbreviation
name=input("Enter a name:")
print("Abbreviation is:\n",abbre(name))
        
    
