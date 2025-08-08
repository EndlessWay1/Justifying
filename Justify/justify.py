
def main() -> None:
    c = Solution()
    
    with open("content_file.txt", "r") as Infile:
        row = Infile.readlines()
    with open("output.txt", "w") as Outfile:
        for i in row:
            i = i.split(" ")
            s = c.fullJustify(i, 125)
            for j in s:
                Outfile.writelines(j + "\n")


class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        arr =[]
        maximum = maxWidth
        spaces = []
        curr = []
        #len_space = 0
        #len_curr = 0
        r = 0
        while r < len(words):
            word_is = ""
            maximum = maxWidth
            #len_space = len_curr = 0
            spaces = []
            curr = []
            while r < len(words) and (maximum >= len(words[r]) + 1 or maximum == len(words[r])):
                spaces.append(" ")
                curr.append(words[r])
                #len_curr += len(words[r])
                #len_space += 1
                maximum -= len(words[r]) + 1
                r += 1
            spaces.pop(0)
            # len_space -= 1
            maximum += 1
            if r == len(words):
                for i,j in zip(curr,spaces):
                    word_is += i + j
                word_is += curr[len(spaces)] + " "*(maximum)
                arr.append(word_is)
                break
            
            if len(spaces) != 0:
                num_space_given_per_iteration = maximum // len(spaces)
            else:
                word_is = curr[0] + " "*maximum
                arr.append(word_is)
                continue

            the_rest = maximum - num_space_given_per_iteration*len(spaces)
            #print(f"{num_space_given_per_iteration=},{maximum=},{len_space=}, {the_rest=}")

            for i in range(len(spaces)):
                if the_rest != 0:
                    spaces[i] += " "*(num_space_given_per_iteration + 1)
                    #len_space += num_space_given_per_iteration + 1
                    the_rest -= 1
                else:
                    spaces[i] += " "*num_space_given_per_iteration
                    #len_space += num_space_given_per_iteration
                word_is += curr[i] + spaces[i]

            word_is += curr[len(spaces)]
            '''
            print(curr, len_curr)
            print(spaces, len_space)
            print(word_is)
            '''
            arr.append(word_is)
        return arr
    
if __name__ == "__main__":
    main()    