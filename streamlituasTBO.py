import streamlit as st

class EnglishCourseFSA:
    def __init__(self):
        self.state = st.session_state.get('state', 'start')
        self.name = st.session_state.get('name', None)
        self.email = st.session_state.get('email', None)
        self.program = st.session_state.get('program', None)
        self.score = st.session_state.get('score', 0)

    def start_registration(self):
        if self.state == 'start':
            st.title("English Course Registration")
            st.session_state.state = 'waiting_for_name'
            self.get_name()
        else:
            st.error("Invalid operation. Already in progress or completed.")
    
    def get_name(self):
        if self.state == 'waiting_for_name':
            self.name = st.text_input("Please enter your name:", key='name')
            if st.button('Next', key='name_next'):
                if self.name:
                    st.session_state.state = 'waiting_for_email'
                    st.session_state.name = self.name
                    st.experimental_rerun()
        else:
            st.error("Invalid operation. Name is already provided or in incorrect state.")

    def get_email(self):
        if self.state == 'waiting_for_email':
            self.email = st.text_input("Please enter your email:", key='email')
            if st.button('Next', key='email_next'):
                if self.email:
                    st.session_state.state = 'waiting_for_program'
                    st.session_state.email = self.email
                    st.experimental_rerun()
        else:
            st.error("Invalid operation. Email is already provided or in incorrect state.")
    
    def choose_program(self):
        if self.state == 'waiting_for_program':
            st.subheader("Choose a Program")
            self.program = st.radio("Select Program:", options=['Grammar', 'Writing'], key='program')
            if st.button('Next', key='program_next'):
                if self.program:
                    st.session_state.state = 'program_chosen'
                    st.session_state.program = self.program
                    st.experimental_rerun()
        else:
            st.error("Invalid operation. Program is already chosen or in incorrect state.")
    
    def start_program(self):
        if self.state == 'program_chosen':
            st.write(f"Starting the {self.program} program!")
            st.session_state.state = 'taking_quiz'
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

            if self.program not in questions:
                st.error("Invalid operation. Program is not chosen yet or in incorrect state.")
                return
            
            selected_questions = questions[self.program]
            self.score = 0
            for i, q in enumerate(selected_questions):
                st.write(q["question"])
                answer = st.radio("Your answer:", options=["a", "b"], key=f'quiz_{i}')
                if answer == q["answer"]:
                    self.score += 1
            if st.button('Submit Quiz'):
                st.session_state.state = 'quiz_completed'
                st.session_state.score = self.score
                st.experimental_rerun()
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
            st.session_state.state = 'completed'
        else:
            st.error("Invalid operation. Registration not yet completed or in incorrect state.")

# Create an instance of the EnglishCourseFSA
registration = EnglishCourseFSA()

# Function to run the registration process
def run_registration():
    state = st.session_state.get('state', 'start')
    if state == 'start':
        registration.start_registration()
    elif state == 'waiting_for_name':
        registration.get_name()
    elif state == 'waiting_for_email':
        registration.get_email()
    elif state == 'waiting_for_program':
        registration.choose_program()
    elif state == 'program_chosen':
        registration.start_program()
    elif state == 'taking_quiz':
        registration.take_quiz()
    elif state == 'quiz_completed':
        registration.complete_registration()

run_registration()
