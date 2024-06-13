import streamlit as st

class EnglishCourseFSA:
    def __init__(self):
        self.state = 'start'
        self.name = None
        self.email = None
        self.program = None
        self.score = 0

    def start_registration(self):
        if self.state == 'start':
            st.title("English Course Registration")
            self.state = 'waiting_for_name'
            self.get_name()
        else:
            st.error("Invalid operation. Already in progress or completed.")
    
    def get_name(self):
        if self.state == 'waiting_for_name':
            self.name = st.text_input("Please enter your name:", key='name')
            if self.name:
                self.state = 'waiting_for_email'
                self.get_email()
        else:
            st.error("Invalid operation. Name is already provided or in incorrect state.")

    def get_email(self):
        if self.state == 'waiting_for_email':
            self.email = st.text_input("Please enter your email:", key='email')
            if self.email:
                self.state = 'waiting_for_program'
                self.choose_program()
        else:
            st.error("Invalid operation. Email is already provided or in incorrect state.")
    
    def choose_program(self):
        if self.state == 'waiting_for_program':
            st.subheader("Choose a Program")
            self.program = st.radio("Select Program:", options=['Grammar', 'Writing'], key='program')
            if self.program:
                self.state = 'program_chosen'
                self.start_program()
        else:
            st.error("Invalid operation. Program is already chosen or in incorrect state.")
    
    def start_program(self):
        if self.state == 'program_chosen':
            st.write(f"Starting the {self.program} program!")
            self.state = 'taking_quiz'
            self.take_quiz()
        else:
            st.error("Invalid operation. Program is not chosen yet or in incorrect state.")
    
    def take_quiz(self):
        if self.state == 'taking_quiz':
            questions = {
                'Grammar': [
                    {"question": "Choose the correct sentence: (a) She go to school. (b) She goes to school.", "answer": "b"},
                    {"question": "Choose the correct word: He (is/are) a teacher.", "answer": "is"},
                    {"question": "Choose the correct sentence: (a) They is happy. (b) They are happy.", "answer": "b"}
                ],
                'Writing': [
                    {"question": "Choose the correct form: (a) I has a book. (b) I have a book.", "answer": "b"},
                    {"question": "Choose the correct sentence: (a) She were here. (b) She was here.", "answer": "b"},
                    {"question": "Choose the correct word: The cat (sit/sits) on the mat.", "answer": "sits"}
                ]
            }
            selected_questions = questions[self.program]
            self.score = 0
            for i, q in enumerate(selected_questions):
                st.write(q["question"])
                answer = st.radio("Your answer:", options=["a", "b"], key=f'quiz_{i}')
                if answer == q["answer"]:
                    self.score += 1
            self.state = 'quiz_completed'
            self.complete_registration()
        else:
            st.error("Invalid operation. Quiz is already completed or in incorrect state.")
    
    def complete_registration(self):
        if self.state == 'quiz_completed':
            st.write(f"Thank you {self.name}!")
            if self.score == 3:
                membership_level = "Advanced"
            elif self.score == 2:
                membership_level = "Intermediate"
            else:
                membership_level = "Beginner"
            st.write(f"You have been registered with the email {self.email}.")
            st.write(f"You have completed the {self.program} program with a score of {self.score}/3.")
            st.write(f"You have been awarded a {membership_level} membership card.")
            self.state = 'completed'
        else:
            st.error("Invalid operation. Registration not yet completed or in incorrect state.")

# Create an instance of the EnglishCourseFSA
registration = EnglishCourseFSA()

# Run Streamlit app
if 'state' not in st.session_state:
    st.session_state.state = 'start'
if 'name' in st.session_state:
    registration.name = st.session_state.name
if 'email' in st.session_state:
    registration.email = st.session_state.email
if 'program' in st.session_state:
    registration.program = st.session_state.program
if 'score' in st.session_state:
    registration.score = st.session_state.score

registration.state = st.session_state.state

# Function to run the registration process
def run_registration():
    if registration.state == 'start':
        registration.start_registration()
    elif registration.state == 'waiting_for_name':
        registration.get_name()
    elif registration.state == 'waiting_for_email':
        registration.get_email()
    elif registration.state == 'waiting_for_program':
        registration.choose_program()
    elif registration.state == 'program_chosen':
        registration.start_program()
    elif registration.state == 'taking_quiz':
        registration.take_quiz()
    elif registration.state == 'quiz_completed':
        registration.complete_registration()

run_registration()

# Update session state to persist across interactions
st.session_state.state = registration.state
if registration.name:
    st.session_state.name = registration.name
if registration.email:
    st.session_state.email = registration.email
if registration.program:
    st.session_state.program = registration.program
st.session_state.score = registration.score