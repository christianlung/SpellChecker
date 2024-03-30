from spellchecker import database, wagner_fisher, setup_dictionary
import random
import time

def levanstein(w1,w2):
    if len(w1)==0: return len(w2)
    elif len(w2)==0: return len(w1)
    elif w1[0]==w2[0]: return levanstein(w1[1:], w2[1:])
    else:
        return 1 + min(levanstein(w1[1:], w2), levanstein(w1, w2[1:]), levanstein(w1[1:], w2[1:]))

def compare():
    database = setup_dictionary()
    wagner_avg = 0
    levanstein_avg = 0
    n_trials = 10000
    for _ in range(n_trials):
        idx_1 = random.randint(0,466549)
        idx_2 = random.randint(0,466549)

        #adjust words to feasible range for runtime testing
        while((idx_2 - idx_1) > 30000 or len(database[idx_1])>5 or len(database[idx_2])>5):
            idx_1 = random.randint(0,466549)
            idx_2 = random.randint(0,466549)

        word_1 = database[idx_1]
        word_2 = database[idx_2]

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
    compare()

if __name__ == "__main__":
    main()