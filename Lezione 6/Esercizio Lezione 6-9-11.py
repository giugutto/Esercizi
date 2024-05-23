from User import *

#9-11. Imported Admin: Start with your work from Exercise 9-8. 
# Store the classes User, Privileges, and Admin in one module. 
# Create a separate file, make an Admin instance, and call show_privileges() to show that everything is working correctly.
privilegi = Privileges(["Can add post","Can delete post","Can ban user","Can change name of user"])
Amministratore3 = Admin("Filippo","Filippi", 41, 1.77,12,privilegi)
Amministratore3.privileges.show_privileges()