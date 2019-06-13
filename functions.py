
# coding: utf-8

# In[20]:


# the corresponding morse code of 26 letters, 10 numbers and some puncutation marks.
# based on the international morse code chart 
morse_code_dict = {'A':'.-','a':'.-',
                'B':'-...','b':'-...',
                'C':'-.-.','c':'-.-.',
                'D':'-..','d':'-..',
                'E':'.','e':'.',
                'F':'..-.','f':'..-.',
                'G':'--.','g':'--.',
                'H':'....','h':'....',
                'I':'..','i':'..',
                'J':'.---','j':'.---',
                'K':'-.-','k':'-.-',
                'L':'.-..','l':'.-..',
                'M':'--','m':'--',
                'N':'-.','n':'-.',
                'O':'---','o':'---',
                'P':'.--.','p':'.--.',
                'Q':'--.-','q':'--.-',
                'R':'.-.','r':'.-.',
                'S':'...','s':'...',
                'T':'-','t':'-',
                'U':'..-','u':'..-',
                'V':'...-','v':'...-',
                'W':'.--','w':'.--',
                'X':'-..-','x':'-..-',
                'Y':'-.--','y':'-.--',
                'Z':'--..','z':'--..',
                '1':'.----','2':'..---',
                '3':'...--','4':'....-',
                '5':'.....','6':'-....',
                '7':'--...','8':'---..',
                '9':'----.','0':'-----',
                ',':'--..--', '.':'.-.-.-', 
                '?':'..--..', '/':'-..-.', 
                '-':'-....-','(':'-.--.-', 
                ')':'-.--.-','-':'-....-',
                '=':'-...-',';':'-.-.-.',
                '+':'.-.-.','_':'..--.-',
                '@':'.--.-.',"'":'.----.',
                '"':'.-..-.','&':'.-...',
               '$':'...-..-','!':'-.-.--',' ':''}


# the list of signal words to terminate the translator
quit_list = ['quit', 'QUIT', 'Quit']

# the list of signal words to initiate the encoder mode in the translator
encoder_list = ['Encoder', 'ENCODER', 'encoder']

# the list of signal words to initiate the decoder mode in the translator
decoder_list = ['Decoder', 'DECODER', 'decoder']

# the list of signal words that can be processed in the mode choosing section, the combination of the three lists above
mode_list = quit_list + encoder_list + decoder_list


# In[15]:


# for encoding human language (English,numbers and some punctuations)
def morse_encoder(message):  
   
    """the structure of this code is extraced from A2, Q15"""
    
    encoded = ''
    
    for item in message:
        
        if item != ' ':
            
            # get() can match the morse code for each character in message 
            encoded = encoded + morse_code_dict.get(item)+ ' '
        
        else:
            encoded += ' '
            
    return encoded


# In[16]:


# for decoding morse code
def morse_decoder(code): 
    
    """this code is from a third party source: https://www.geeksforgeeks.org/morse-code-translator-python"""


    code += ' '
  
    decoded = '' 
    citext = '' 
    for char in code: 
   
        # to check the spaces
        if char != ' ': 
   
            # when there is no space, indicate one letter
            i = 0
   
            citext += char 
   

        # when there is space
        else:  
            i += 1
  
            # counter == 2 means two spaces, indicate the gap between two words
            if i == 2 : 
  
                decoded += ' '
            
           
            # to decode the code
            else: 
                
                # reverse the keys and values of the dictrionary of the morse code
                # index(citext) locates the code in the values of the dictrionary
                # values are corresponded to the keys, so the code is decoded into human language
                
                decoded += list(morse_code_dict.keys())[list(morse_code_dict 
                .values()).index(citext)] 
                
                citext = '' 
                
                # make the decoded message all lower case
                # then capitalize the decoded message
                
                decoded = decoded.lower()
                decoded = decoded.capitalize()
  

    return decoded


# In[17]:


def is_in_list(list_one, list_two):
    
    """to check if all the elements in list_one are in list_two """
    
    
    # use the mathmatical relationship between two sets: the first set is a subset of the latter
    # to turn the lists to the sets
    
    if set(list_one) <= set(list_two):
           
            return True
    
    return False


# In[18]:


def end_translator(input_1):
    
    """the structure of this code is subtracted from A3, Q16"""
    
    
    # split() turns the string input to a list that has each word of the input as an element
    # to check if the signal words for ending the translator appear in the input
    
    if is_in_list(input_1.split(), quit_list):
        output = True
    
    else:
        output = False
    
    return output


# In[19]:


def morse_code_translator():
    
    """the kernel of the final project, initiate the chatbot"""
    
    
    # the start of the translator
    chat = True
    while chat:
        
        
        # the mode choosing section
        msg_1 = input('Encoder or Decoder:\t')
        out_msg = None
        
        # if the signal words do not appear in the input, remind the user to type in valid message
        if not is_in_list(msg_1.split(),mode_list):
            
            print('Please choose your mode.')
        
        
        # if the signal words for ending appear, the translator ends
        if end_translator(msg_1):
            
            chat= False
            
            print('Mission Complete.')
       
        
        # if the signal words for encoder mode appear, enter the encoder mode
        if is_in_list(msg_1.split(),encoder_list):
            
            
            # remind the users to type in the message they want to encode 
            msg_2 = input('Original Message:\t')
            
            
            # if the input message contains any character that has no corresponding morse code, remind the users by an error
            if not is_in_list(msg_2, list(morse_code_dict.keys())):
                 
                    print('Input Error. #,%,^,*,`,{,},[,],|,\ do not have corresponding morse codes.')
            
            
            # if the input is valid, output the encoded message
            else:
                
                out_msg = morse_encoder(msg_2)
                
                
                print('Encoded Message:\t', out_msg)
               
        
        # if the signal words for decoder mode appear, enter the decoder mode
        if is_in_list(msg_1.split(),decoder_list):
            
            
            # remind users to type in the morse code they want to decode
            msg_3 = input('Original Code:\t\t')
            
            
            #if every code in the input codes is valid, then the decoder processes the input codes 
            if is_in_list(msg_3.split(), list(morse_code_dict.values())):
                
                out_msg = morse_decoder(msg_3)
                
                print('Decoded Message:\t',out_msg)
            
            
            #if any invalid input appears in the input codes, remind the users by an error
            else:
                
                print('Input Error. Please only type in valid codes.')


morse_code_translator()

