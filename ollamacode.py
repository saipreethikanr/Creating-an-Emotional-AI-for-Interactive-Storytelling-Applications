# to run this cope 1st save it the code with a .py extension and install ollama 
# open the file in VS code or any other code editor 
# click terminal and write (ollama serve) to run the server 
# then add a new terminal and write (cd Documents) ie ur python code's location 
# then enter (python file_name.py) 

#Code 
import ollama

class AI_Model:
    client = None
    model = None

    emotions = [
        "happy",
        "angry",
        "sad",
        "not feeling good",
        "feeling low",
        "sarcasm",
        "excited"
    ]

    def init(self):
        print("Starting the application ...")

        # Initialize the Ollama client
        # self.client = ollama.Client()

        # Load a model
        self.model = 'phi3.5'
        print("Loading an LLM model...")

    def get_result(self, prompt):
        stream = ollama.chat(
            model='phi3.5',
            messages=[{'role': 'user', 'content': prompt}], 
            stream=True,
        )

        print("Here is your story...")

        for chunk in stream:
            print(chunk['message']['content'], end='', flush=True)

def ask_name():
    print("Hi, how are you doing? May I know your name?")
    user_name = input("> ")
    print("Name saved as " + user_name)
    print("Hello, " + user_name + ". I am a bot who loves to generate stories based on your mood.")
    return user_name

def modify_prompt(name, prompt):
    prompt= prompt + ". Also utilise the name " + name + " as a main character in the story."
    return prompt

def run(model, name):
    print("What would you like to ask me ?")
    prompt = input("> ")

    if "story" in prompt: 
        if any(emotion in prompt for emotion in model.emotions):
            modified_prompt = modify_prompt(name, prompt)
            model.get_result(modified_prompt)
        else:
            print("This is not a relevent prompt. You can only ask me to generate story based on your feelings or mood.")
    else:
        print("This is not a relevant prompt. You can only ask me to generate a story based on your mood.")

# Initialize the model and ask for user's name
my_model = AI_Model()
my_model.init()
name = ask_name()

# Infinite loop to handle continuous user interactions
while True:
    run(my_model, name)
