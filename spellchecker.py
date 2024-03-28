def setup_dictionary():
    with open('/Users/christianlung/SpellChecker/dictionary.txt', 'r') as file:
        return [line.strip() for line in file]

#wagner fisher approach
def wagner_fisher(w1,w2):
    len1 = len(w1)
    len2 = len(w2)
    current_row = [x for x in range(len1+1)]

    #iterate by row
    for i in range(1, len2+1):
        previous_row = current_row
        current_row = [i] + [0] * len1
        #iterate within a row
        for j in range(1, len1+1):
            closest_step = min(current_row[j-1], previous_row[j], previous_row[j-1])
            if w1[j-1] != w2[i-1]: #if letters are the same, proceed with the minimum
                closest_step += 1
            current_row[j] = closest_step
            if i==len2 and j==len1:
                return closest_step

def levanstein(w1,w2):
    if len(w1)==0: return len(w2)
    elif len(w2)==0: return len(w1)
    elif w1[0]==w2[0]: return levanstein(w1[1:], w2[1:])
    else:
        return 1 + min(levanstein(w1[1:], w2), levanstein(w1, w2[1:]), levanstein(w1[1:], w2[1:]))

def suggestion(word, database):   #implement support for LRU cache of size 1000 or dictionary
    corrections = []
    for correct_word in database:
        distance = wagner_fisher(word, correct_word)
        if distance<=5: corrections.append((correct_word, distance))
    corrections.sort(key=lambda x: x[1])
    return corrections[:3]

def clean_doc(document):
    with open(document, 'r') as file:
        raw_data = file.read()
    
    is_capital = False
    buffer = ""
    clean_data = ""
    for pointer in range(len(raw_data)):
        pass

def main():
    dictionary = setup_dictionary()


if __name__ == "__main__":
    main()


#todo:
#   implement document autocorrecter
        #unrecognized word on line 2
        #did you make an error? Fix to this, this, this, or leave it 1,2,3,4, print -------, output to a new file?
        #keep track of capital or not and punctuation
#   Things to improve: make file easier to load in, implement a LRU cache
#   Maybe make javascript frontend to display wagner-fisher approach