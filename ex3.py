# Хэрэгцээтэй python сангуудыг оруулж ирнэ.
import getpass                        
import telnetlib

# Гараас IP хаягийг авч IP хувьсагчан дотор хадгална.
IP=input("Enter the IP address: ")

# Гараас хэрэглэгчийн нэрийг аван user хувьсагчан дотор хадгална.
user=input("Enter your username: ")

# Хэрэглэгч нууц үгийг getpass санг ашиглан prompt дээр авна.
password=getpass.getpass()

# Гараас авсан IP хаяг руу Telnet ашиглан нэвтэрнэ
tn=telnetlib.Telnet(IP)

# Свич хэрэглэгчийн нэрийг унших боломжтой болно.
tn.read_until(b"Username: ")
tn.write(user.encode("ascii") + b"\n")

# Нууц үгийг уншин ascii-руу энкод хийн switch руу command бичнэ. 
if password:
  tn.read_until(b"Password: ")
  tn.write(password.encode("ascii")+b"\n")


tn.write(b"enable\n")              # Свичийн тохиргооны горимыг идэвхжүүлнэ.
tn.write(b"cisco\n")  
tn.write(b"conf t\n")              # Свичийн глобал тохиргооны горимд шилжинэ.
tn.write(b"vlan 20\n")             # VLAN интерфейс үүсгэнэ.
tn.write(b"name Data_VLAN_20\n")   # VLAN 20-д нэр өгнө.
tn.write(b"int vlan 20\n")         # VLAN 20 руу хандана.

# VLAN 20-д IP хаяг оноож өгнө.
tn.write(b"IP address 10.20.30.40 255.255.255.0\n")
tn.write(b"no sh\n")               # Интерфейсийг асаана.
tn.write(b"end\n")                 # Тохиргооноос гарна.