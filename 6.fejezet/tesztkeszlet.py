from unitTestSaját import teszt
from feladatok import fordulj_orajarasi_iranyba
from feladatok import nap_nev

if False:
    teszt(fordulj_orajarasi_iranyba("É") =="K")
    teszt(fordulj_orajarasi_iranyba("D") =="NY")
    teszt(fordulj_orajarasi_iranyba("K") =="D")
    teszt(fordulj_orajarasi_iranyba("NY") =="É")
    teszt(fordulj_orajarasi_iranyba("X") ==None)
    
    
if True:
    teszt(nap_nev(0)== "Hétfő")
    teszt(nap_nev(1)== "Kedd")
    teszt(nap_nev(2)== "Szerda")
    teszt(nap_nev(3)== "Csütörtök")
    teszt(nap_nev(4)== "Péntek")
    teszt(nap_nev(5)== "Szombat")
    teszt(nap_nev(6)== "Vasárnap")
    teszt(nap_nev(7)== None)