# template.py
from models.index import user_data
from views.index import validate_f_name, validate_l_name, validate_password, validate_age, validate_username
welcome_message = """
Welcome to Your system You can do this ,
Please choose what you want to do ! 
1. sign up
2. retrieve your data 
3. retrieve all users 
4. update your data 
5. delete your data
6. close program 

"""

def authenticate_user(username , password) : 
    for user in user_data : 
        if user.get("username") == username and user.get("password") == password : 
            return user 
    return None


def login_required(operation) : 
    def out_func() : 
        username = input("Please, enter your username : ")  
        password = input("Please, enter your password : ")
        user = authenticate_user(username , password)
        if user : 
            operation(user)
        else :
            print("Please, Signup first :) ")
    return out_func


def signup():
    first_name = input("Enter your first name : ")
    last_name = input("Enter your last name : ")
    user_name = input("Enter your user name : ")
    age = input("Enter your age : ")
    password = input("Enter your password : ")
    f_name = validate_f_name(first_name)
    l_name = validate_l_name(last_name)
    userName = validate_username(user_name)
    aGe = validate_age(age)
    passWord = validate_password(password)

    
@login_required                
def retrieve_your_data(user) :
    print(f'UserName : {user["username"]}') 
    print(f'First Name : {user["first_name"]}') 
    print(f'Last Name : {user["last_name"]}') 
    print(f'Age : {user["age"]}') 


def start() :
    while True :
        print(welcome_message)
        choice = input("Please enter your choice : ")
        match choice  :
            case "1" :
                signup()
                # pass
            case "2" : 
                retrieve_your_data()
            case "3" :
                # retrieve_all_users()
                pass 
            case "4" :
                pass 
                # update_your_data() 
            case "5" :
                # delete_your_data()
                pass 
            case  "6" : 
                break
            case _ :
                print("Please enter a valid choice")
            
    print("We will miss you")

