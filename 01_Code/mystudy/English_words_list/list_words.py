import sys
import argparse
#import enchant



def is_english_word(word):
    #d_en = enchant.Dict("en_US")
    #return d_en.check(str(word))
    return True

    
def recursion_chars(f, word, level, count):
    if level + 1 > count :
        return
    word.append('')
    for i in range(26):
        word[level] = chr(ord('a') + i)
        recursion_chars(f, word, level + 1, count)
        if (level + 1 == count):
            if (is_english_word(word)):
                f.write("".join(word) + "\n")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('min', metavar='M', type=int, nargs=1,
                        help='Minimum count lettles for the English word.')
    parser.add_argument('max', metavar='N', type=int, nargs=1,
                        help='Maximum count lettles for the English word.')
    args = parser.parse_args()

    #print(args.min[0])
    #print(args.max[0])
    min = args.min[0]
    max = args.max[0]

    if (min > max or min < 1):
        print("Error, Please input M and N correctly.")
        sys.exit(1)

    with open('word.txt','w') as f:
        for x in range(min, max + 1):
            word_list = []
            recursion_chars(f, word_list, 0, x)


if __name__ == '__main__':
    main()