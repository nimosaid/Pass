# Pass

## Built By [NIMO SAID](https://github.com/nimosaid/)

## Description
Password Locker is a terminal run python application that allows users to store details i.e. usernames and passwords of their various accounts.

## User Stories
These are the behaviors/features that the application implements for use by a user.

As a user I would like:
* To create an account with my details - log in and password
* Store my existing login credentials
* Generate a password for a new credential/account
* Copy my credentials to the clipboard

## Specifications
| Behavior | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Display codes for navigation | **In terminal: $./password_locker.py** | Welcome, choose an option: ca-Create Account, li-Log In, ex-Exit |
| Display prompt for creating an account | **Enter: ca** | Enter your first name, last name and password |
| Display prompt for login in | **Enter: li** | Enter your account name and password |
| Display codes for navigation | **Successful login** | Choose an option: cc - Create Credentials, dc - Display Credentials, copy - Copy Credentials, ex - exit |
| Display prompt for creating a credential | **Enter: cc** | Enter the site name, your username and password |
| Display a list of credentials | **Enter: dc** | Prints a list of saved credentials |
| Display prompt for which credential to copy | **Enter: copy** | Enter the site name of the credential you wish to copy. |
| Exit application | **Enter: ex** | Exit the current navigation stage |

## SetUp / Installation Requirements
### Prerequisites
* python3.6
* pip
* pyperclip

### Cloning
* In your terminal:

        $ git clone https://github.com/nimosaid/Pass/
        $ cd Pass

## Running the Application
* To run the application, in your terminal:

        $ chmod +x password_locker.py
        $ ./password_locker.py

## Testing the Application
* To run the tests for the class file:

        $ python3.6 user_credentials_test.py

## Technologies Used
* Python3.6

## License
MIT &copy;2019 [Nimo Said](https://github.com/nimosaid/)
