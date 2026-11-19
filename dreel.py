from pyscript import document  # type: ignore[reportMissingImports]

# list of cadet officers over the rank of 2nd LT
gr_10cos = {"Julian Anaque", "Carlos Borromeo", "Jan Cabading", "Francis Fernandez", "Jacob Minguillo", "Darvine Mitchell"}
gr_9cos = {"Erich Garaza", "Georgina Gamponia", "Kevin Goda", "Kaitlyn Mediarito", "Venice Magdayao", "Ondrea Torres"}

def check_cos(e): # checks the officer function
    f_name = document.getElementById("Fname").value.strip().title() # grab first name
    l_name = document.getElementById("Lname").value.strip().title() # grab second name

    if f_name and l_name: # check if both names are okay
        offcandidates = f"{f_name} {l_name}" # = user input
        plebs = {offcandidates} # create name set
        
        cadetofficers = gr_10cos | gr_9cos| plebs # adds to roster

        document.getElementById("Fname").value = ""
        document.getElementById("Lname").value = ""
    else:
        all_members = gr_10cos | gr_9cos # combines only the predefined officer sets
    
# final sort of inputs and values
    countoff = "<br>".join(sorted(cadetofficers)) # sorts and joins the officers
    total_count = len(cadetofficers) # counts total officers in the set
            
    output_text = f"ALL MEMBERS:<br>{countoff}<br><br>TOTAL MEMBERS: {total_count}" # Format output
            
    document.getElementById("output1").innerHTML = output_text # Display final output