"""
Karl Michel Koerich , 1631968
420-LCU Computer Programming , Section 2
Sunday, November 26
R. Vincent , instructor
Assignment 4
"""

from string import ascii_uppercase, ascii_lowercase
        #Importing alphabet upper and lower case

### DO NOT MODIFY THIS FUNCTION ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a set of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    in_file = open(file_name, 'r') # in_file: file
    line = in_file.readline()      # line: string
    word_list = line.split()    # word_list: list of strings
    in_file.close()
    return set(word_list)

### DO NOT MODIFY THIS FUNCTION ###
def get_story_string():
    """
    Returns: a joke in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

WORDLIST_FILENAME = 'words.txt'
class Message(object):
    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
        '''
        self.message_text = text

    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    ### IMPLEMENT THIS METHOD
    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''

        #------- Work starts -------#

        shifted_upper = list(ascii_uppercase[shift:] + ascii_uppercase[:shift]) #Creates new list with the shifted upper
        shifted_lower = list(ascii_lowercase[shift:] + ascii_lowercase[:shift]) #Creates new list with the shifted lower
        
        shift_dic  = dict(zip(list(ascii_uppercase), shifted_upper)) #Creates dict (letter:encrypted)
        shift_dic.update(zip(list(ascii_lowercase), shifted_lower)) #Appends lower letter to dict

        return shift_dic

        #-------- Work ends --------#

    ### IMPLEMENT THIS METHOD
    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''

        #------- Work starts -------#

        shift_dic = self.build_shift_dict(shift)

        message_text_encrypted = list(self.message_text) #List from message_text

        for i in range(0, len(message_text_encrypted)): #For every position in the list
            for k, v in shift_dic.items():
                if message_text_encrypted[i] == k: #We check if this character can be found in the dictionary
                    message_text_encrypted[i] = v #If it can be found, we modify its value. 
                    break #The break is needed to avoid changing the character again
                                #For example: if shift=2,  a changes to c,
                                            # when it finds c it would change to e, etc.

        return "".join(message_text_encrypted) #Returns new string encrypted

        #-------- Work ends --------#

class PlaintextMessage(Message):
    ### IMPLEMENT THIS METHOD ###
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.shift (integer, determined by input shift)
            self.message_text_encrypted (string, created using shift)

        Hint: consider using the parent class constructor and the 
        set_shift method so no code is repeated.
        '''
        #------- Work starts -------#

        super().__init__(text)
        self.set_shift(shift)

        #-------- Work ends --------#

    ### DO NOT MODIFY THIS METHOD ###
    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift

    ### DO NOT MODIFY THIS METHOD ###
    def set_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift (ie. message_text_encrypted).
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        self.shift = shift
        self.message_text_encrypted = self.apply_shift(shift)

    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted


class CiphertextMessage(Message):
    ### IMPLEMENT THIS METHOD ###
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        #------- Work starts -------#

        super().__init__(text)
        self.valid_words = load_words("words.txt")

        #-------- Work ends --------#

    ### DO NOT MODIFY THIS METHOD ###
    def is_word(self, word):
        '''
        Determines if word is a valid word, ignoring
        capitalization and punctuation
        
        word (string): a possible word.
    
        Returns: True if word is in word_list, False otherwise

        Example:
        >>> ciphertext.is_word('bat') returns
        True
        >>> ciphertext.is_word('asdf') returns
        False
        '''
        garbage = " !@#$%^&*()-_+={}[]|\:;'<>?,./\""
        return word.strip(garbage).lower() in self.valid_words

    ### IMPLEMENT THIS METHOD ###
    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create 
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value.
        '''
        #------- Work starts -------#

        n_english_words = [0]*(26) #List of number of english words per shift

        for i in range(0, 26): #For every shift,

            list_words = self.apply_shift(i).split() #We apply the shift,

            for word in list_words: #And add 1 if it is an english word.
                if self.is_word(word):
                    n_english_words[i] += 1

        all_combinations = list(zip(n_english_words, list(range(0, 26)))) #(number of english words, shift)
        all_combinations.sort()
        #After the list of tuples is sorted, the last tuple cointains the ideal shift.
        best_option = all_combinations[-1] #Takes the last tuple.
        ideal_shift = best_option[1] #Gets the shift number

        return (ideal_shift, self.apply_shift(ideal_shift))

        #-------- Work ends --------#

# DO NOT CHANGE ANY CODE AFTER THIS LINE!!

# Unit test - just verify that build_shift_dict is properly implemented.

message = Message("testing")

n_errors = 0
for i in range(1, 26):
    shift_dict = message.build_shift_dict(i)
    for key in shift_dict:
        alt = shift_dict[key]
        if key.isupper():
            base = ord('A')
        elif key.islower():
            base = ord('a')
        org = chr(((ord(key) - base) + i) % 26 + base)
        if alt != org:
            n_errors += 1
        

if n_errors != 0:
    print("*** build_shift_dict is not correct!!")
else:
    print("*** build_shift_dict passed the tests!!")
assert n_errors == 0

# Integration test case (PlaintextMessage)

plaintext = PlaintextMessage('Hello', 2)
print('Expected Output: Jgnnq', end=' ')
print('Actual Output:', plaintext.get_message_text_encrypted())
assert 'Jgnnq' == plaintext.get_message_text_encrypted()

# Integration test case (CiphertextMessage)

ciphertext = CiphertextMessage('Jgnnq')
print('Expected Output:', (24, 'Hello'), end = ' ')
print('Actual Output:', ciphertext.decrypt_message())
assert (24, 'Hello') == ciphertext.decrypt_message()

# Actually try to decode the "story".

ciphertext = CiphertextMessage(get_story_string())
print(ciphertext.decrypt_message())
