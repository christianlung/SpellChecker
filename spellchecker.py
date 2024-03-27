import random
import time

def setup_dictionary():
    with open('/Users/christianlung/SpellChecker/words.txt', 'r') as file:
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

def compare(dictionary):
    wagner_avg = 0
    levanstein_avg = 0
    n_trials = 10000
    for _ in range(n_trials):
        idx_1 = random.randint(0,466549)
        idx_2 = random.randint(0,466549)

        #adjust words to feasible range for runtime testing
        while((idx_2 - idx_1) > 30000 or len(dictionary[idx_1])>5 or len(dictionary[idx_2])>5):
            idx_1 = random.randint(0,466549)
            idx_2 = random.randint(0,466549)

        word_1 = dictionary[idx_1]
        word_2 = dictionary[idx_2]

        w_start = time.time()
        wagner_fisher(word_1, word_2)
        w_end = time.time()
        wagner_avg += w_end - w_start

        l_start = time.time()
        levanstein(word_1, word_2)
        l_end = time.time()
        levanstein_avg += l_end - l_start

    wagner_avg /= n_trials
    levanstein_avg /= n_trials
    print("Comparing Average Computing Time...")
    print(f"Wagner-fisher: {wagner_avg}")
    print(f"Levanstein: {levanstein_avg}")

def main():
    dictionary = setup_dictionary()
    compare(dictionary)

if __name__ == "__main__":
    main()


#do i make a javascript frontend to display the data

#unrecognized word on line 2
#did you make an error? Fix to this, this, this, or leave it 1,2,3,4, print -------, output to a new file?