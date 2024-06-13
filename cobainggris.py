class EnglishCourseFSA:
    def __init__(self):
        self.state = 'start'
        self.name = None
        self.email = None
        self.program = None
        self.score = 0

    def start_registration(self):
        if self.state == 'start':
            print("Welcome to the English course registration!")
            self.state = 'waiting_for_name'
            self.get_name()
        else:
            print("Invalid operation. Already in progress or completed.")
    
    def get_name(self):
        if self.state == 'waiting_for_name':
            self.name = input("Please enter your name: ")
            self.state = 'waiting_for_email'
            self.get_email()
        else:
            print("Invalid operation. Name is already provided or in incorrect state.")

    def get_email(self):
        if self.state == 'waiting_for_email':
            self.email = input("Please enter your email: ")
            self.state = 'waiting_for_program'
            self.choose_program()
        else:
            print("Invalid operation. Email is already provided or in incorrect state.")
    
    def choose_program(self):
        if self.state == 'waiting_for_program':
            print("Please choose a program: Grammar or Writing")
            self.program = input("Enter your choice: ").strip().lower()
            if self.program in ['grammar', 'writing']:
                self.state = 'program_chosen'
                self.start_program()
            else:
                print("Invalid choice. Please choose either 'Grammar' or 'Writing'.")
                self.choose_program()
        else:
            print("Invalid operation. Program is already chosen or in incorrect state.")
    
    def start_program(self):
        if self.state == 'program_chosen':
            print(f"Starting the {self.program.capitalize()} program!")
            self.state = 'taking_quiz'
            self.take_quiz()
        else:
            print("Invalid operation. Program is not chosen yet or in incorrect state.")
    
    def take_quiz(self):
        if self.state == 'taking_quiz':
            questions = {
                'grammar': [
                    {"question": "Choose the correct sentence: (a) She go to school. (b) She goes to school.", "answer": "b"},
                    {"question": "Choose the correct word: He (is/are) a teacher.", "answer": "is"},
                    {"question": "Choose the correct sentence: (a) They is happy. (b) They are happy.", "answer": "b"}
                ],
                'writing': [
                    {"question": "Choose the correct form: (a) I has a book. (b) I have a book.", "answer": "b"},
                    {"question": "Choose the correct sentence: (a) She were here. (b) She was here.", "answer": "b"},
                    {"question": "Choose the correct word: The cat (sit/sits) on the mat.", "answer": "sits"}
                ]
            }
            selected_questions = questions[self.program]
            self.score = 0
            for q in selected_questions:
                print(q["question"])
                answer = input("Your answer: ").strip().lower()
                if answer == q["answer"]:
                    self.score += 1
            self.state = 'quiz_completed'
            self.complete_registration()
        else:
            print("Invalid operation. Quiz is already completed or in incorrect state.")
    
    def complete_registration(self):
        if self.state == 'quiz_completed':
            print(f"Thank you {self.name}!")
            if self.score == 3:
                membership_level = "Advanced"
            elif self.score == 2:
                membership_level = "Intermediate"
            else:
                membership_level = "Beginner"
            print(f"You have been registered with the email {self.email}.")
            print(f"You have completed the {self.program.capitalize()} program with a score of {self.score}/3.")
            print(f"You have been awarded a {membership_level} membership card.")
            self.state = 'completed'
        else:
            print("Invalid operation. Registration not yet completed or in incorrect state.")

# Create an instance of the EnglishCourseFSA
registration = EnglishCourseFSA()

# Start the registration process
registration.start_registration()
