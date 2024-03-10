# Хэрэгцээтэй python сангуудыг оруулж ирнэ.
import getpass
import telnetlib

# IP хаягийг хувьсагчид хадгална.
IP="192.168.122.20"

# Гараас хэрэглэгчийн нэрийг аван user хувьсагчан дотор хадгална.
user=input("Enter your username")

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
  tn.write(password.encode("ascii") + b"\n")

  
tn.write(b"enable\n")              # Свичийн тохиргооны горимыг идэвхжүүлнэ.
tn.write(b"cisco\n")          
tn.write(b"conf t\n")              # Свичийн глобал тохиргооны горимд шилжинэ.
tn.write(b"hostname CoreSW\n")     # Хостын нэрийг CoreSW болгон өөрчилнө. 
tn.write(b"end \n")                # Тохиргооноос гарна.
tn.write(b"write memory\n")        # Төхөөрөмжид хийсэн тохиргоог хадгална