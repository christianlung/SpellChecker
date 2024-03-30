database = None

def setup_dictionary():
    global database
    if database is None:
        with open('/Users/christianlung/SpellChecker/dictionary.txt', 'r') as file:
            database = [line.strip() for line in file]

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
            insert, remove, change = previous_row[j]+1, current_row[j-1]+1, previous_row[j-1]
            if w1[j-1] != w2[i-1]: #if letters are the same, proceed with the minimum
                change += 1
            closest_step = min(insert, remove, change)
            current_row[j] = closest_step
            if i==len2 and j==len1:
                return closest_step

def suggestion(word, n_suggestions=5):   #implement support for LRU cache of size 1000 or dictionary
    setup_dictionary()
    corrections = []
    for correct_word in database:
        distance = wagner_fisher(word, correct_word)
        if distance<=5: corrections.append((correct_word, distance))
    corrections.sort(key=lambda x: x[1])
    return [c[0] for c in corrections[:n_suggestions]]

def clean_doc(document):
    #what if last word is mispelled
    setup_dictionary()
    with open(document, 'r') as file:
        raw_data = file.read().strip()
    buffer = ""
    clean_data = ""
    n_suggests = 5

    for pointer in range(len(raw_data)+1):
        if pointer==len(raw_data): #to handle if the last word is mispelled
            character = ""
        else:
            character = raw_data[pointer]
        if character.isalpha() or character == "'":
            buffer += character
        else:
            #what if you come across 2 non-letters in a row
            if len(buffer)>0 and buffer.lower() not in database:
                #get user input as to what the word should be
                #optimizations, if mistake is less than 1, autocorrect it
                #if there are ties, base on side of keyboard
                #option to enter your own word?
                suggestions = suggestion(buffer, n_suggestions=n_suggests)
                print(f"Spelling error: {buffer}")
                print("Did you mean: ")
                for idx in range(n_suggests):
                    print(f"{idx+1}. {suggestions[idx]} \t", end="")
                print(f"{n_suggests+1}. (Leave as is)")

                valid = False
                while not valid:
                    try:
                        option = int(input("Enter an option: "))
                        print("\n")
                    except ValueError:
                        print("Please enter a valid integer.")
                    if option>=1 and option<=n_suggests+1:
                        valid = True
                    else:
                        print(f"Invalid option. Please enter a number 1 to {n_suggests}.")
                if option!=(n_suggests+1):
                    buffer = (suggestions[option-1][0].upper() + suggestions[option-1][1:]) if buffer[0].isupper() else suggestions[option-1]
                    #catch exception where word is not a number? then can you accept words starting with number?
            clean_data += buffer + character
            buffer = ""
    return clean_data 
        

def main():
    print(clean_doc('document.txt'))


if __name__ == "__main__":
    main()


#todo:
    
#   make test cases for where word is not number, if last word is mispelled
#   output to a new file?
#   Things to improve: make file easier to load in, implement a LRU cache
#   maybe include most popular proper nouns like brands and places
#   Maybe make javascript frontend to display wagner-fisher approach
    
    #store list as pickle file

    #make dictionary into class, with serial, and deserial, create new list
    #search dictionary, query for suggestions

    #past or plural? fix it yourself option