# author Void(subhan ahmed)

# file = open('input_data/a_an_example.in.txt', 'r')
# file = open('input_data/b_basic.in.txt', 'r')
# file = open('input_data/c_coarse.in.txt', 'r')
file = open('input_data/d_difficult.in.txt', 'r')
# file = open('input_data/e_elaborate.in.txt', 'r')
lines = []
# reading file
for w in file.readlines():
    lines.append(w.strip())

customerNo = 1
likeIngredients = {}
dislikeIngredients = {}
while customerNo <= len(lines) - 1:
    # taking out likes
    currentLikes = lines[customerNo].split(' ')
    # scoring likes and storing them in dictionary
    noOfLikes = int(currentLikes[0])
    for i in range(1, noOfLikes + 1):
        if currentLikes[i] in likeIngredients.keys():
            likeIngredients[str(currentLikes[i])] = int(likeIngredients[str(currentLikes[i])]) + 1
        else:
            likeIngredients["" + currentLikes[i]] = 1

    # dislikes
    currentDislikes = lines[customerNo + 1].split(' ')

    noOfDislikes = int(currentDislikes[0])
    for i in range(1, noOfDislikes + 1):
        if currentDislikes[i] in dislikeIngredients.keys():
            dislikeIngredients[str(currentDislikes[i])] = int(dislikeIngredients[str(currentDislikes[i])]) + 1
        else:
            dislikeIngredients["" + currentDislikes[i]] = 1

    customerNo = customerNo + 2

print("like items with score")
print(likeIngredients)
print("dislike items with score")
print(dislikeIngredients)
# removing those dislike Ingredients which are more disliked than liked
resultIngredients = likeIngredients.copy()
for key_of_dislikes in dislikeIngredients.keys():
    for key_of_likes in likeIngredients.keys():
        if key_of_likes == key_of_dislikes:
            if likeIngredients[key_of_likes] < dislikeIngredients[key_of_dislikes]:
                resultIngredients.pop(key_of_likes)

resultIngredients = list(resultIngredients.keys())
resultIngredients.insert(0, len(resultIngredients))
resultIngredientsString = ' '.join([str(elem) for elem in resultIngredients])
# print(resultIngredientsString)

file.close()
# creating output file
outputFile = open('output.txt', 'w')
outputFile.write(resultIngredientsString)
outputFile.close()


#  for scoring output file locally
def sim_result_score(inputData, resultItems):
    noOfCustomers = inputData[0]
    customers = []
    itemNo = 1
    while itemNo <= len(inputData) - 1:
        # taking out likes
        currentLike = inputData[itemNo].split(' ')
        inputData[itemNo + 1].split(' ').pop(0)
        currentDislike = inputData[itemNo + 1].split(' ')
        currentLike.pop(0)
        currentDislike.pop(0)
        customers.append([currentLike, currentDislike])
        itemNo = itemNo + 2

    # separating each result item
    resultItems = resultItems.split(" ")
    resultItems.pop(0)
    score = 0
    for customer in customers:
        n = 0
        while n < len(customer):
            # for likes
            likeFlag = False
            dislikeFlag = False
            counter = 0
            for likeInfo in customer[n]:
                for item in resultItems:
                    if item == likeInfo:
                        counter = counter + 1
                if counter == len(customer[n]):
                    likeFlag = True

            # for dislikes
            if len(customer[n + 1]) == 0:
                dislikeFlag = True
            else:
                for dislikeInfo in customer[n + 1]:
                    if dislikeInfo not in resultItems:
                        dislikeFlag = True
                    else:
                        dislikeFlag = False
                        break
            if likeFlag and dislikeFlag:
                score = score + 1
            n = n + 2

    return int(score)


# reading from output file for scoring
file = open("output.txt", "r")
line = file.readline()
file.close()
print("score " + str(sim_result_score(lines, str(line))))
