import string

letters=dict()


for c in string.ascii_letters[:26]:
    letters[c]=0

#print(letters)

with open('american-english.txt', 'r') as f:
    for w in f:
        for char in string.ascii_letters[:26]:
            letters[char]+=w.lower().count(char)


    most_freq_char=sorted(letters.items(), key=lambda x: x[1] , reverse= True)  #sort the characters as per their occurence
    

    freq_char=[x for x, y in most_freq_char[:3]]  # print most 3 freqent characters in file      




print(letters)
print(freq_char)



