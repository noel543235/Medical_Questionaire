#Innovation Project
# Medical questions and surveys
#save to files
#use functions

#Remindor: this program cannot run in Thonny it has to run in the computers Terminal
#make sure to have python 3.9.7 downloaded to the terminal
#also sure to have the three items installed
#numpy, matploblib, and pillow

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
    

#Create the function for the first part of the program    
def mental_survey():
    
    #find an image and make sure to put the exact file name in the open statement
    #https://delamohospital.com/squashing-mental-illness-misconceptions
    image_open('Mental_health_intro.jpg')
    
    #get the amount of questions they want
    question_amount = int(amount_questions())
    amount = display_ratings_scale()
    
    #ask the first question this question should always be there
    question1 = input_validator("How was your mood today?: ")
    
    #open the file so the user can input their answers
    file = open('Survey','a')
    file.write(" ")
    
    #make a label so they know which section their answers are from
    file.write("Mental Health Survey")
    file.write(" ")
    file.write(question1)
    file.close()
    
    #if the question_amount is more than one use if and elif statements to go through the questions each time
    if question_amount > 1:
        
        #ask the second question
        question2 = input_validator("How did you sleep last night?: ")
        
        #open the file again so they can add a second input
        file = open('Survey','a')
        file.write(question2)
        file.close()
        
    if question_amount > 2:
        
        #ask question three
        question3 = input_validator("How was your stress level today?: ")
        
        #open the file so the user can add their thrird input
        file = open('Survey','a')
        file.write(question3)
        file.close()
        
    if question_amount > 3:
        
        #ask the fourth question
        question4 = input_validator("Did you accomplish what you wanted to do today?: ")
        
        #open the file so the users answer is saved into the file
        file = open('Survey','a')
        file.write(question4)
        file.close()
    if question_amount > 4:
        
        #add in question number five 
        question5 = input_validator("Do you think you ate enough today?: ")
        
        #open the file for the fifth input
        file = open('Survey','a')
        file.write(question5)
        file.close()
        
    #get the users thoughts of it by going to the function above
    review_questionair_questions()
    
    #open the file so the computer displays what they have addded so far
    print(open('Survey').read())


#Have the function for the second part of this questionaire 
def Physical_survey():
    
    #add in the second picture and put the right name in
    #https://www.quora.com/What-is-Physical-Health
    image_open('Physical_intro.jpg')
    
    #get the amount of questions
    question_amount = int(amount_questions())
    amount = display_ratings_scale()
    
    #get the first question and this should be asked every time they choose this section
    question1 = input_validator("How are you feeling?: ")
    
    #open the file and addd the first question in the file
    file = open('Survey','a')
    file.write(" ")
    
    #add a header for this section so they know what those answers were for
    file.write("Physical Health Survey")
    file.write(" ")
    file.write(question1)
    file.close()
    
    #add in an if and elif statement that runs depending on what the user enters
    if question_amount > 1:
        
        #get the second question from the user
        question2 = input_validator("How often do you go to the docter?: ")
        
        #open the file and add in the second question answer
        file = open('Survey','a')
        file.write(question2)
        file.close()
        
    if question_amount > 2:
        
        #add in the third question
        question3 = input_validator("Are you currently sick?: ")
        
        #input the users answers into the file
        file = open('Survey','a')
        file.write(question3)
        file.close()
        
    if question_amount > 3:
        
        #add in the fourth question of this section
        question4 = input_validator("Do you think your healthy?: ")
        
        #open the file and write in the users answer
        file = open('Survey','a')
        file.write(question4)
        file.close()
        
    if question_amount > 4:
        
        #add in the fifth question 
        question5 = input_validator("How are the Hospitals in your area?: ")
        
        #open the file and add their answers in
        file = open('Survey','a')
        file.write(question5)
        file.close()
        
    #open the review section so they can reflect on their answers
    review_questionair_questions()
    
    #print the file so they can see their answers
    print(open('Survey').read())

def Joint_survey():
    
    #print the header for the joint survey
    print("+++++ Joint Health ++++++")
    
    #get the amount of questions
    question_amount = int(amount_questions())
    amount = display_ratings_scale()
    
    #ask the first 
    question1 = input_validator("Do you have pain in your joints?: ")
    
    #enter their answer in the file
    file = open('Survey','a')
    file.write(" ")
    
    #label the section so the user knows what they put as their answers
    file.write("Joint Survey")
    file.write(" ")
    file.write(question1)
    file.close()
    
    #make if and elif statements that run based off of the users choice of how many questions they want
    if question_amount > 1:
        
        #enter the second question
        question2 = input_validator("Do you have trouble walking?: ")
        
        #put their answers in the file
        file = open('Survey','a')
        file.write(question2)
        file.close()
        
    if question_amount > 2:
        
        #ask the third question
        question3 = input_validator("Do you do any Joint excerisizes?: ")
        
        #put it in the file
        file = open('Survey','a')
        file.write(question3)
        file.close()
        
    if question_amount > 3:
        
        #ask the fourth question 
        question4 = input_validator("Do you have a hard time holding items?: ")
        
        #enter their answer into the file
        file = open('Survey','a')
        file.write(question4)
        file.close()
        
    if question_amount > 4:
        question5 = input_validator("Have you had any trouble stretching any joints?: ")
        file = open('Survey','a')
        file.write(question5)
        file.close()
        
    #get their input on what they thought about the survey
    review_questionair_questions()
    
    #print the file so they can see what they put
    print(open('Survey').read())
    
#create the function for the excersize portion of the questionaire     
def Excersize_survey():
    
    #enter the image that introduces the topic
    #https://cdn4.vectorstock.com/i/1000x1000/33/83/design-woman-fitness-exercise-logo-gymnastics-vector-26203383.jpg
    image_open('Excersize_intro.jpg')
    
    #get the amount of questions they want
    question_amount = int(amount_questions())
    amount = display_ratings_scale()
    
    #ask the first question 
    question1 = input_validator("On a scale of 1-5 how much do you excersize per week?: ")
    
    #put the answer in the file
    file = open('Survey','a')
    file.write(" ")
    
    # label it so they know what they answered for it
    file.write("Excersize Survey")
    file.write(" ")
    file.write(question1)
    file.close()
    
    #ask the questions after depending on what they chose
    if question_amount > 1:
        
        #ask the second question and enter it into the file
        question2 = input_validator("How much of aschedule do you have when you work out?: ")
        file = open('Survey','a')
        file.write(question2)
        file.close()
        
    if question_amount > 2:
        
        #ask the third question and enter it into the file
        question3 = input_validator("Do you play sports?: ")
        file = open('Survey','a')
        file.write(question3)
        file.close()
    if question_amount > 3:
        
        #ask the fourth question and enter it into the file
        question4 = input_validator("How physically active are you?: ")
        file = open('Survey','a')
        file.write(question4)
        file.close()
    if question_amount > 4:
        
        #ask the fifth question and enter it into the file
        question5 = input_validator("How much do you go to a gym?: ")
        file = open('Survey','a')
        file.write(question5)
        file.close()
        
    #get the users input on what they thought of their answers
    review_questionair_questions()
    
    #print the file so they know what they chose
    print(open('Survey').read())
    
#make the function for the multiple choice quiz
def Multiple_choice():
    
    #introduce the section
    print("****** Multiple Choice******")
    
    #create the variable for correct so it counts how many they got right 
    correct = 0
    
    #ask how many questions they would like
    question_amount = int(amount_questions())
    
    # question 1
    print("When someone sprains their ankle which part of the joint gets injured?: ")
    
    #print the answer options 
    print("A. Bone               B. Ligaments")
    print("C. Tendons            D. Skin")
    
    #make the answer variable so that they can enter their answer
    answer = input("Enter your answer here: ")
    
    #make the if statement that determines if they got it right or not
    if answer == "B" or answer == "b":
        
        #if they got it right enter a well done image
        #https://media.makeameme.org/created/well-done-7v7e6g.jpg
        image_open('welldone1.jpg')
        print("Correct!")
        
        #add to the correct variable
        correct = correct + 1
    else:
        print("Incorrect the correct answer is B")
        
        #append the number and their answer to the list
        lst.append("1.")
        lst.append(answer)
        
    # if and elif statements that are determined by how many questions the user would like   
    if question_amount > 1:
        
        #question 2
        print("Which excersize equiptment will help make your biceps stronger?: ")
        
        #the answer options
        print("A. Barbell curl         B. Bicicle")
        print("C. Leg Press            D. Treadmill")
        
        #the answer option input 
        answer = input("Enter your answer here: ")
        
        #the if statement determining if they got it right or wrong
        if answer == "A" or answer == "a":
            
            #if they get it right add in the image and add 1 to the correct variable
            #https://i.pinimg.com/originals/6d/db/c5/6ddbc58b4f26c54cae47652f6f5966a7.jpg
            image_open('welldone2.jpg')
            print("Correct!")
            correct = correct + 1
        else:
            print("Incorrect the correct answer is A")
            
            #if they got it wrong append the number and their answer to the list
            lst.append("2.")
            lst.append(answer)
            
    if question_amount > 2:
        
        #question 3
        print("Which of the following is something that causes stress?: ")
        
        #print the answer options
        print("A. Exams               B. Fights")
        print("C. School              D. All of the Above")
        
        #the input statement for the answer
        answer = input("Enter your answer here: ")
        
        #the if statement determining whter they got it right or not
        if answer == "D" or answer == "d":
            
            #make the image and add one to the correct variable
            #https://www.memesmonkey.com/images/memesmonkey/9e/9e31d79351b38c2abb06b798ad7c5d00.jpeg
            image_open('welldone3.jpeg')
            print("Correct!")
            correct = correct + 1
        else:
            print("That is only partly Correct the Correct answer is D")
            
            #append the number and the users answer
            lst.append("3.")
            lst.append(answer)
    if question_amount > 3:
        
        #question four
        print("Which of the following is a good carbohydrate?: ")
        
        #print the answer the options
        print("A. Pasta               B. Fries")
        print("C. Apples              D. Bread")
        answer = input("Enter your answer here: ")
        
        #the if statement that determines if they got the answer right or wrong
        if answer == "C" or answer == "c":
            
            #well done image and add one to the correct variable
            #https://memegenerator.net/img/instances/73278580.jpg
            image_open('welldone4.jpg')
            print("Correct!")
            correct = correct + 1
        else:
            print("Incorrect the correct answer is C")
            
            #append the wrong answer if they get it wrong
            lst.append("4.")
            lst.append(answer)
            
    if question_amount > 4:
        
        #question number 5
        print("Which of these excersizes is a cardio excersize?: ")
        
        #answer options
        print("A. swimming               B. Planks")
        print("C. weight lifting         D. leg curls")
        
        #answer input
        answer = input("Enter your answer here: ")
        
        #if statement determining if the answer is right or wrong
        if answer == "A" or answer == "a":
            
            #add image and add 1 to the correct variable
            #https://www.google.com/url?sa=i&url=https%3A%2F%2Fsayingimages.com%2Fgood-job-meme%2F&psig=AOvVaw09xoBJPDK-JUg9oQ__yN40&ust=1638931948973000&source=images&cd=vfe&ved=0CAgQjRxqGAoTCMii_8_X0PQCFQAAAAAdAAAAABCDAQ
            image_open('welldone5.jpg')
            print("Correct!")
            correct = correct + 1
        else:
            print("Incorrect the correct answer is A")
            
            #append the wrong answer to the list
            lst.append("5.")
            lst.append(answer)
        
    #complete the main function and show them which ones they got wrong and how many they got right
    print("Hope you had fun with this Quiz!")
    print("You got {} out of {} correct".format(correct,question_amount))
    print("if you got any wrong they will sho up here")
    print(lst)

#call the main function to run everything
main()


