import itertools as it
import string as st

# :::::::::::::::::::UNTERPROGRAMM:::::::::::::::::::

def versch(echt, tri, x):
    for k in range(len(echt)+1):                                  # +1 Weil er sonst zu früh aufhört |
        for ch in it.product(x, repeat=k):                        # nimmt basically st.ascii_uppercase mal k, d.h. "ABC..." x (k*"ABC...") -> A,A A,B ... | Das braucht man weil man nachdem er einmal ch durch "ABC.." gerunt hat ja möchte das er ch durch "ABC..." erster Stelle und dann "ABC..." zweiter Stelle, etc. runt. Und weil man nur so strings multiplizieren kann
            ch = "".join(ch)                                      # Macht einen str aus ch |
            tri += 1
            if ch == echt: return ch, tri                         # Wenn der guess dem gesuchten Wort entspricht | gibt er den guess und die benötigten Versuche wieder |
            print(ch, tri)                                        # Nur für's Anschauliche |

# :::::::::::::::::::HAUPTPROGRAMM:::::::::::::::::::

zsm = st.ascii_uppercase + st.digits + st.ascii_lowercase 
tries = -1                                                        
print(versch("A b 1", tries, zsm))