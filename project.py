#Innovation Project
# Medical questions and surveys
#save to files
#use functions

#Remindor: this program cannot run in Thonny it has to run in the computers Terminal
#make sure to have python 3.9.7 downloaded to the terminal 

#insert the installed functions from the terminal so Pictures can be used later on in the code
#make sure to have all of these installed or this program cannot run 
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

#make a list for section 6 with the multiple choicce quiz so i can append wrong answers into it and the user can see which ones they got wrong and which answer they chose that was incorrect
lst = []

#create the Main function that calls the other functions to run the program
def main():
    while True:
        menu()
        
        #see if the users choice was valid or not
        choice = choice_validator()
        
        #Go through the different options that the user can pick
        #call each of the functions for each section except for 6 since it just closes the program
        if choice == "6":
            print("Closing Medical Overview program")
            print("have a nice day")
            break
        elif choice == "1":
            mental_survey()
        elif choice == "2":
            Physical_survey()
        elif choice == "3":
            Joint_survey()
        elif choice == "4":
            Excersize_survey()
        elif choice == "5":
            Multiple_choice()
        
#The Function for displaying the Menu and showing the user the options      
def menu ():
    print("-----------------------------------------------------")
    print("-               Medical Overview                    -")
    print("-        Welcome to the overview questionaires      -")
    print("-----------------------------------------------------")
    print("-              Medical Overview options             -")
    print("-         1. Mental Health Survey                   -")
    print("-         2. Physical Health Survey                 -")
    print("-         3. Joint Survey                           -")
    print("-         4. Excersize Survey                       -")
    print("-         5. Medical Mutliple Choice Quiz           -")
    print("-         6. End This Overview                      -")
    print("-----------------------------------------------------")
   
#Make the function for the choice section so it can be checked if it is right
def choice_validator():
    
    #create a While loop just incase the answer inputed was incorrect so it can loop over again and ask them the question again
    while True:
        
        #Create the input statement so the user can insert their option
        choice = input("Please choose of of the options shown above (1-6): ")
        
        #using isdigit() check if the user inputed a digit and check if the input is inbetween 1-6
        if choice.isdigit() and (int(choice) > 0) and (int(choice) < 7):
            return choice
        else:
            print("Invalid option please try again ")
            
#create the function for the sections asking the user how many questions they want
def amount_questions():
    
    #create a While loop just incase the answer inputed was incorrect so it can loop over again and ask them the question again
    while True:
        
        #Make the input statement for the user to anwer 1-5 for how many questions they would like
        question_amount = input("How many questions would you like(1-5): ")
        
        #for this if statement it is similar to before checking if the input is a digit and it is between 1-5
        if question_amount.isdigit() and (int(question_amount) > 0 and int(question_amount) < 6):
            return question_amount
        else:
            print("Invalid option please try again")
            
#create the function to review their answers to whatever they chose 
def review_questionair_questions():
    
    #prompt the user with a question
    print("Please tell us how you feel about the answers you chose for the survey: ", end = "")
    
    #get the input
    review = input()
    
    #use the file code to open the file and write whatever they want in it using the review variable
    file = open('Survey','a')
    file.write(" ")
    file.write(review)
    
    #make sure to close the file after you are done inputing stuff in it
    file.close()

#for this function it is used to tell the user how to answer the questions    
def display_ratings_scale():
    print("For each question answer 1-5")
    print("1 is worst and 5 is best")
    

#Use a function to check to see if they entered in a digit and if it is between 1-5    
def input_validator(question: str):
    
    #use a while loop incase they enter an invalid option
    while True:
        choice = input(question)
        
        #use the if statement from above and make sure that the user inputs a digit between 1-5
        if choice.isdigit() and (int(choice) > 0) and (int(choice) < 6):
            return choice
        else:
            print("Invalid option please try again ")
            
#for this fuction use the installed functions on the Terminal to insert the necessary images you want 
# from: https://stackoverflow.com/questions/32286566/python-image-pop-up-for-5-seconds    
def image_open(filepath):
    
    #make a variable that opens an image using the parameter
    images = Image.open(filepath)
    
    #The image needs to be formated 
    imageformat = np.asarray(images)
    
    #use the formatted image and show it
    plt.imshow(imageformat)
    
    #this line draws the image you want to show
    plt.draw()
    
    #make a line that makes the image appear for only a certain amount of time for example 3 seconds
    plt.pause(3)
    
    #close the image
    plt.close()
    

    
def mental_survey():
    #https://delamohospital.com/squashing-mental-illness-misconceptions
    image_open('Mental_health_intro.jpg')
    question_amount = int(amount_questions())
    amount = display_ratings_scale()
    question1 = input_validator("How was your mood today?: ")
    file = open('Survey','a')
    file.write(" ")
    file.write("Mental Health Survey")
    file.write(" ")
    file.write(question1)
    file.close()
    if question_amount > 1:
        question2 = input_validator("How did you sleep last night?: ")
        file = open('Survey','a')
        file.write(question2)
        file.close()
    if question_amount > 2:
        question3 = input_validator("How was your stress level today?: ")
        file = open('Survey','a')
        file.write(question3)
        file.close()
    if question_amount > 3:
        question4 = input_validator("Did you accomplish what you wanted to do today?: ")
        file = open('Survey','a')
        file.write(question4)
        file.close()
    if question_amount > 4:
        question5 = input_validator("Do you think you ate enough today?: ")
        file = open('Survey','a')
        file.write(question5)
        file.close()
    review_questionair_questions()
    print(open('Survey').read())

    
def Physical_survey():
    #https://www.quora.com/What-is-Physical-Health
    image_open('Physical_intro.jpg')
    question_amount = int(amount_questions())
    amount = display_ratings_scale()
    question1 = input_validator("How are you feeling?: ")
    file = open('Survey','a')
    file.write(" ")
    file.write("Physical Health Survey")
    file.write(" ")
    file.write(question1)
    file.close()
    if question_amount > 1:
        question2 = input_validator("How often do you go to the docter?: ")
        file = open('Survey','a')
        file.write(question2)
        file.close()
    if question_amount > 2:
        question3 = input_validator("Are you currently sick?: ")
        file = open('Survey','a')
        file.write(question3)
        file.close()
    if question_amount > 3:
        question4 = input_validator("Do you think your healthy?: ")
        file = open('Survey','a')
        file.write(question4)
        file.close()
    if question_amount > 4:
        question5 = input_validator("How are the Hospitals in your area?: ")
        file = open('Survey','a')
        file.write(question5)
        file.close()
    review_questionair_questions()
    print(open('Survey').read())

def Joint_survey():
    print("+++++ Joint Health ++++++")
    question_amount = int(amount_questions())
    amount = display_ratings_scale()
    question1 = input_validator("Do you have pain in your joints?: ")
    file = open('Survey','a')
    file.write(" ")
    file.write("Joint Survey")
    file.write(" ")
    file.write(question1)
    file.close()
    if question_amount > 1:
        question2 = input_validator("Do you have trouble walking?: ")
        file = open('Survey','a')
        file.write(question2)
        file.close()
    if question_amount > 2:
        question3 = input_validator("Do you do any Joint excerisizes?: ")
        file = open('Survey','a')
        file.write(question3)
        file.close()
    if question_amount > 3:
        question4 = input_validator("Do you have a hard time holding items?: ")
        file = open('Survey','a')
        file.write(question4)
        file.close()
    if question_amount > 4:
        question5 = input_validator("Have you had any trouble stretching any joints?: ")
        file = open('Survey','a')
        file.write(question5)
        file.close()
    review_questionair_questions()
    print(open('Survey').read())
    
def Excersize_survey():
    #https://cdn4.vectorstock.com/i/1000x1000/33/83/design-woman-fitness-exercise-logo-gymnastics-vector-26203383.jpg
    image_open('Excersize_intro.jpg')
    question_amount = int(amount_questions())
    amount = display_ratings_scale()
    question1 = input_validator("On a scale of 1-5 how much do you excersize per week?: ")
    file = open('Survey','a')
    file.write(" ")
    file.write("Excersize Survey")
    file.write(" ")
    file.write(question1)
    file.close()
    if question_amount > 1:
        question2 = input_validator("How much of aschedule do you have when you work out?: ")
        file = open('Survey','a')
        file.write(question2)
        file.close()
    if question_amount > 2:
        question3 = input_validator("Do you play sports?: ")
        file = open('Survey','a')
        file.write(question3)
        file.close()
    if question_amount > 3:
        question4 = input_validator("How physically active are you?: ")
        file = open('Survey','a')
        file.write(question4)
        file.close()
    if question_amount > 4:
        question5 = input_validator("How much do you go to a gym?: ")
        file = open('Survey','a')
        file.write(question5)
        file.close()
    review_questionair_questions()
    
    print(open('Survey').read())
    

def Multiple_choice():
    print("****** Multiple Choice******")
    correct = 0
    question_amount = int(amount_questions())
    print("When someone sprains their ankle which part of the joint gets injured?: ")
    print("A. Bone               B. Ligaments")
    print("C. Tendons            D. Skin")
    answer = input("Enter your answer here: ")
    if answer == "B" or answer == "b":
        #https://media.makeameme.org/created/well-done-7v7e6g.jpg
        image_open('welldone1.jpg')
        print("Correct!")
        correct = correct + 1
    else:
        print("Incorrect the correct answer is B")
        lst.append("1.")
        lst.append(answer)
    if question_amount > 1:
        print("Which excersize equiptment will help make your biceps stronger?: ")
        print("A. Barbell curl         B. Bicicle")
        print("C. Leg Press            D. Treadmill")
        answer = input("Enter your answer here: ")
        if answer == "A" or answer == "a":
            #https://i.pinimg.com/originals/6d/db/c5/6ddbc58b4f26c54cae47652f6f5966a7.jpg
            image_open('welldone2.jpg')
            print("Correct!")
            correct = correct + 1
        else:
            print("Incorrect the correct answer is A")
            lst.append("2.")
            lst.append(answer)
    if question_amount > 2:
        print("Which of the following is something that causes stress?: ")
        print("A. Exams               B. Fights")
        print("C. School              D. All of the Above")
        answer = input("Enter your answer here: ")
        if answer == "D" or answer == "d":
            #https://www.memesmonkey.com/images/memesmonkey/9e/9e31d79351b38c2abb06b798ad7c5d00.jpeg
            image_open('welldone3.jpeg')
            print("Correct!")
            correct = correct + 1
        else:
            print("That is only partly Correct the Correct answer is D")
            lst.append("3.")
            lst.append(answer)
    if question_amount > 3:
        print("Which of the following is a good carbohydrate?: ")
        print("A. Pasta               B. Fries")
        print("C. Apples              D. Bread")
        answer = input("Enter your answer here: ")
        if answer == "C" or answer == "c":
            #https://memegenerator.net/img/instances/73278580.jpg
            image_open('welldone4.jpg')
            print("Correct!")
            correct = correct + 1
        else:
            print("Incorrect the correct answer is C")
            lst.append("4.")
            lst.append(answer)
    if question_amount > 4:
        print("Which of these excersizes is a cardio excersize?: ")
        print("A. swimming               B. Planks")
        print("C. weight lifting         D. leg curls")
        answer = input("Enter your answer here: ")
        if answer == "A" or answer == "a":
            #https://www.google.com/url?sa=i&url=https%3A%2F%2Fsayingimages.com%2Fgood-job-meme%2F&psig=AOvVaw09xoBJPDK-JUg9oQ__yN40&ust=1638931948973000&source=images&cd=vfe&ved=0CAgQjRxqGAoTCMii_8_X0PQCFQAAAAAdAAAAABCDAQ
            image_open('welldone5.jpg')
            print("Correct!")
            correct = correct + 1
        else:
            print("Incorrect the correct answer is A")
            lst.append("5.")
            lst.append(answer)
        
    
    print("Hope you had fun with this Quiz!")
    print("You got {} out of {} correct".format(correct,question_amount))
    print("if you got any wrong they will sho up here")
    print(lst)

main()

