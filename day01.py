# a.find the common letter of the word,without using inbuilt method
	
a=['flowing','flow','flame']
letters = []
x=0
common_letters = []
for y in a[0]:
    for i in y:
        letters.append(i)

for letter in letters:
    if letter in a[1] and letter in a[2]:
        common_letters.append(letter)
        x+=1
        letter = letters[x]

print(common_letters)



# -----------------------------------------------------------------------------------------------------------------
        


# b.print list of duplicate character in string and print character that has maximum number of occurence in string
# 	take input as string = "genrosysweeklytasks"

	# output:
	# [e,s,y,k]
	# maximum : s

string = "genrosysweeklytasks"
letters = []
duplicates = []
counter = 0
max_count = 0
max_repeat_letter = ''

for item in string:
    letters.append(item)

print(letters)

for i in range(0, len(letters)):
    counter = 0
    for j in range(i+1, len(letters)):
        if letters[j] == letters[i]:
            counter+=1

    if counter>=1 and letters[i] not in duplicates:
        duplicates.append(letters[i])
    
    if counter > max_count:
        max_count = counter
        max_repeat_letter = letters[i]

print(duplicates)
print(max_repeat_letter)


# -----------------------------------------------------------------------------------------------------------------

        
# c. sum = 9

# 	task : find all possible pairs which have sum equal to sum(9)
# 	example :
# 		3 + 6 = 9
# 		4 + 5 = 9
	
# 	note :	
# 		no repeat of pairs
# 		e.g :  4 + 5 = 9
# 			   and 
# 		       5 + 4 = 9
		       
# 	both pairs have same elements hence the pair should come only once in output

list_a = [3, 4, 5, 6, 1, 2, 7, 9, 8]
pairs = []
sum=0
for num1 in range(0, len(list_a)):
    for num2 in range(num1+1, len(list_a)):
        if list_a[num1] + list_a[num2]  == 9:
            num_pair_tuple = (list_a[num1], list_a[num2])
            pairs.append(num_pair_tuple)

print(pairs)
    