class STACK:
    def __init__(self, length):
        self.length = length
        self.stack = []
    
    #This method is to add or insert a new element
    def pushStack(self, append_value):
        print(f"[COMPLETED] The Number {append_value} is pushed on the stack")
        self.stack.append(append_value)#To append the new value that the user inserted in the main program
    
    #This method is to delete an element from the top of the stack
    def popStack(self):
        #If the stack has lesser value than one, it will print stack underflow
        if len(self.stack) < 1:
            print("[ERROR] Stack Underflow!!!")
            return
        print(f"[COMPLETED] The Popped element is: {self.stack[-1]}")
        #-1 because we need to delete the last element, and negative one stands for last element
        del self.stack[-1]
    
    #This method is to display the elements inside the list
    def displayStack(self):
        #If the stack has no value the stack underflow will display
        if not self.stack:
            print("[ERROR] Stack Underflow!!!")
            return
        #To iterate through the list and print it in a vertical manner
        for elements_stack in self.stack:
            print(f"|{elements_stack}|")
    
class STACKPROGRAM:
    def main(self):
        try:#try and catch mechanism
            #It will ask first the size of the stack
            main_stack = STACK(int(input("what is the length of stack: ")))
            while True:
                stack_choice = input(""" 
************ S  T  A  C  K   M  E  N  U  *************
*      Programmed by: Kyne Domerei N. Laggui         *
*                    BSCOE 2-1                       *
*                                                    *
*              (1) PUSH                              *
*              (2) POP                               *
*              (3) DISPLAY STACK CONTENTS            *                               
*              (4) EXIT                              *                
*                                                    *                                     
******************************************************
Select an Option: """)
                if stack_choice == "1":
                    #The user will keep on inputting the element until it reach the limit that the user has set
                    if main_stack.length > len(main_stack.stack):
                            new_append_value = int(input("Enter the number of elements:: "))
                            for i in range(new_append_value):
                                new_append_value = input("Enter your choice:: ")
                                main_stack.pushStack(new_append_value)
                    else:
                        #If you wish to Push but the stack already reaches its limit this will display
                        print("Stack Overflow!!!")
                elif stack_choice == "2":
                    main_stack.popStack()
                    main_stack.displayStack()
                elif stack_choice == "3":
                    main_stack.displayStack()
                elif stack_choice == "4":
                    quit("Thank you for using my Program\nKyne Domerei N. Laggui")
        except ValueError:
            print("[ERROR] Enter a valid length of the Stack")

#The driver of the program
stackProgram =  STACKPROGRAM()
stackProgram.main()

