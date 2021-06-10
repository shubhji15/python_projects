from getpass import getpass

l2 = []  # to store the toppers
# -------------------------
def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Quiz Time<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    for key in questions:
        print("-------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)

# -------------------------
def check_answer(answer, guess):

    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0

# -------------------------
def display_score(correct_guesses, guesses):
    print("-------------------------")
    print("RESULTS")
    print("-------------------------")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+"%")

# -------------------------
def play_again():

    response = input("Do you want to play again? (yes or no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False
# -------------------------
def quiz_setup():
    list_op = []
    question = input('Enter the question')
    answer = input('Provide the option which is correct')
    A = input("option A ")
    B = input("option B ")
    C = input("option C ")
    D = input("option D ")
    questions[question] = answer
    option_A = str('A. '+ A)
    list_op.append(option_A)
    option_B = str('B. '+ B)
    list_op.append(option_B)
    option_C = str('C. '+ C)
    list_op.append(option_C)
    option_D = str('D. '+ D)
    list_op.append(option_D)
    options.append(list_op)
    
    
#--------------------------
questions = {
 "Who created Python?: ": "A",
 "What year was Python created?: ": "B",
 "Python is tributed to which comedy group?: ": "C",
 "Is the Earth round?: ": "A"
}

options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
          ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
          ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
          ["A. True","B. False", "C. sometimes", "D. What's Earth?"]]



# ------------------------------------------------------------------------------------------------------------------------------

studentList = [['shubham15may','shubh#21'],['umesh21nov','shubh#211']]
admin = ['admin','admin123']


def admin_login():
    print('>>>>>>>>>>>>>Login<<<<<<<<<<<<<<<<<<')
    username = input('Please enter user name  :')
    password = getpass('Please enter the password   :')
    if username ==admin[0] and password == admin[1]:
        print('Admin Login')
    else:
        print('Invalid user_name or password')
        admin_login()
    
def student_login():
    l1 = []
    print('>>>>>>>>>>>>>Login<<<<<<<<<<<<<<<<<<')
    username = input('Please enter user name  :')
    password =  getpass('Please enter the password   :')
    for everything in studentList:       
        UserName = everything[0]
        PassWord = everything[1]

        if username == UserName and password == PassWord:
            print(username+ " Logged on.")
            #(l1.append(username, +str(display_score.score()) + "%"))
            print(l1)
            break
    else:
        print('Invalid user_name or password')
        student_login()
def registration():
    print('>>>>>>>>>>>>>Registration<<<<<<<<<<<<<<<<<<')
    l1 =[]
    username = input('Please enter user name  :')
    password = getpass('Please enter the password   :')
    l1.append(username)
    l1.append(password)
    studentList.append(l1)
    print(studentList)
#------------------------------------------------------------------------------------------------------------------------------

              
def play_settingQ():
        choice_2 = input("play/settingQuiz/exit")
        #choice_2 = choice_2.lower()
        for i in choice_2:
            if choice_2 == 'settingQuiz':
                    quiz_setup()
                    choice = input('add more/ exit')
                    if choice == 'add more':
                        quiz_setup()
                    else:
                        break            
            elif choice_2 == 'play':
                new_game()
                play_again()
                
                
            elif choice_2 == 'exit':
                break
        play_settingQ()
        
#         play_again()
#         while play_again():
#             new_game()
#         print("Byeeeeee!")

        

              
              
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------


choice = input('Login/Registration   :')
if choice == 'Login':
    choice_1 = input('admin/user   :')
    #choice_1 = choice.lower()
    if choice_1 == 'admin':
        admin_login()
        play_settingQ()            
    elif choice_1 == 'user':
        student_login()
        new_game()
        while play_again():
            new_game()
        print("Byeeeeee!")
        
elif choice == 'Registration':
    registration()
    student_login()
    new_game()
    while play_again():
        new_game()
    print("Byeeeeee!")
