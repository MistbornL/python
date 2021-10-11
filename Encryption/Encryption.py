data = [
['A', 'B', 'C', 'D', 'E'],
['F', 'G', 'H', 'IJ', 'K'],
['L', 'M', 'N', 'O', 'P'],
['Q', 'R', 'S', 'T', 'U'],
['V', 'W', 'X', 'Y', 'Z']
]

def polybius(word):
    List = []
    string_to_number =""
    IJ = ""
    word = str(word)
    # If input is String    
    if not word[0].isdigit():
        for item in data:
            for letter in word:
                try:
                    letter = letter.upper()
                    if letter in item:
                        string_to_number = f"{data.index(item) + 1}{item.index(letter) + 1}"
                        List.append(string_to_number)

                    # Checks If letter equals to  Third Index of item and if third index of item equals to i same goes for j           
                    if letter == item[3][0] and item[3][0] == "I" or letter == item[3][1] and item[3][1] == "J" :
                        IJ = "24"
                        List.append(IJ)     
                except:
                    pass  
        # Output                                                      
        for i in List:
            print(i, end="")
        print("\n")    
    # If input is Number           
    else:
        number_to_string = ""
        List = []
        n = 2
        split_string = [word[i:i+n] for i in range(0, len(word), n)]

        for item in data:
            for each in split_string:
                number_to_string = data[int(each[0]) - 1][int(each[1])-1]
                if number_to_string in item and number_to_string != "IJ":
                    List.append(number_to_string)
                elif number_to_string in item and number_to_string =="IJ":
                    List.append("I")
        # Output            
        for letter in List:
            print(letter, end="")           


polybius("abcij")   
polybius(11121324)             