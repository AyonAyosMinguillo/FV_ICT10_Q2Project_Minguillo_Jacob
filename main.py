from pyscript import display, document  # type: ignore

co1 = ['Jacob Minguillo', 'Julian Anaque', 'Carlos Borromeo', 'Francis Fernandez', 'Jan Cabading', 'Darvine Mitchell'] # LIST OF CADET OFFICERS IN GRADET 10

def check_cos(e): # For the system's name textbox
    fname = document.getElementById('Fname').value.strip()
    lname = document.getElementById('Lname').value.strip()

    cofname = f"{fname} {lname}".strip().title() # Combines the First and Last Name then|

    checkmember = cofname in co1 # verifies if what the user has added in the system is true to the list of cadet officers in grade 10.
# Please note, Now even if you type e.g. Jacob or jacob minguillo, the system will still consider it.
    message = {
        True: f"{cofname} is an official member of the Cadet Corps of OB Montessori", # Message will display if the checkmember code verifies that the individual is listed in the system
        False: f"{cofname}, is not an official member of the Cadet Corps of OB Montessori" # Message will display if the checkmember code verifies that the individual is not listed in the system
    }

    document.getElementById('output1').innerText = message[checkmember] # Then the code is displayed in HTML