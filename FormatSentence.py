#functions to format sentences from all upper case.

def formatSentence(lineOfText, isBeginning):
    lineOfText = lineOfText.lower()
    lineOfText = capitolizeSentences(lineOfText, isBeginning)
    return lineOfText

def capitolizeSentences(lineOfText, isBeginning):
    for char in lineOfText:
        newString = ''
        if isBeginning == True and char != ' ':
            isBeginning = False
        if char == '.':
            isBeginning = True
      
    return lineOfText
    
            
        
        
