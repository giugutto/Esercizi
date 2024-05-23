from User_1 import *
from PrivilegesandAdmin import *

privilegi1 = Privileges(["Can add post","Can delete post","Can ban user","Can change name of user"])
Amministratore1 = Admin("Pippo","Franco",32,1.67,6,privilegi1)

Amministratore1.privileges.show_privileges()