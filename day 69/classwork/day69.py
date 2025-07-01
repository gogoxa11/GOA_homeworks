def dawere_pirveli_asoebi(sentence):
    words = sentence.split()  
    result = ''             

    for word in words:      
        first_letter = word[0].upper()      
        rest = word[1:]  
        new_word = first_letter + rest 
        result += new_word  

    return result
