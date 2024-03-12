import sqlite3
from hashlib import sha256
 # Connect to the SQLite database (will create it if it doesn't exist)
conn = sqlite3.connect('user_credentials.db')

        # Create a cursor object to execute SQL queries
cursor = conn.cursor()


def __init__(self) :
            self.Ui_Infopage = Ui_Infopage()
            self.newwindow = QtWidgets.QMainWindow()
            self.Ui_Infopage.setupUi(self.newwindow)
            self.Ui_Infopage.muscle_choice_combobox.currentIndexChanged.connect(self.Ui_Infopage.chosenMuscle)
            # Create a table to store usernames, hashed passwords, and measurements
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS me (
                    id INTEGER PRIMARY KEY,
                    username TEXT NOT NULL UNIQUE,
                    password TEXT NOT NULL,
                    measurement INTEGER
            )
            ''')

# Function to get the maximum measurement for a given username
def get_max(self,username):
        cursor.execute('SELECT measurement FROM me WHERE username = ?', (username,))
        result = cursor.fetchone()
        return result[0] if result else 0
# Function to hash a password
def hash_password(self, password):
        return sha256(password.encode()).hexdigest()

def add_user(self,username, password, measurement):
        hashed_password = self.hash_password(password)
        cursor.execute('INSERT INTO me (username, password, measurement) VALUES (?, ?, ?)', (username, hashed_password, measurement))
        conn.commit()
        print("User added successfully!")
        
                
def start_app(self, main):
        name = self.username.text()
        password = self.password.text()
        self.Ui_Infopage.welcome_name_label.setText(name)
        max = self.Ui_Infopage.maximum_muscle_strength_value_label.text()
        #self.add_user(name,password, max)
        if self.password.text() != "":
                self.newwindow.show()
                new_max = self.get_max(name)
                self.Ui_Infopage.previous_muscle_strength_value_label.setText(str(new_max))
                #main.close()