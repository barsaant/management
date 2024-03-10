# Хэрэгцээтэй python сангуудыг оруулж ирнэ.
import getpass
import telnetlib

# Гараас IP хаягийг авч IP хувьсагчан дотор хадгална.
IP=input("Enter the IP address: ")

# Гараас хэрэглэгчийн нэрийг аван user хувьсагчан дотор хадгална.
user=input("Enter your Username: ")

# Хэрэглэгч нууц үгийг getpass санг ашиглан prompt дээр авна.
password=getpass.getpass()

# Гараас авсан IP хаяг руу Telnet ашиглан нэвтэрнэ
tn=telnetlib.Telnet(IP)

# Свич хэрэглэгчийн нэрийг унших боломжтой болно.
tn.read_until(b"Username: ")
tn.write(user.encode("ascii") + b"\n")

# Нууц үгийг уншин ascii-руу энкод хийн switch руу command бичнэ. 
if password:
  tn.read_until(b"password")
  tn.write(password.encode("ascii") + b"\n")

tn.write(b"enable\n")                # Свичийн тохиргооны горимыг идэвхжүүлнэ.
tn.write(b"cisco\n")               
tn.write(b"conf t\n")                # Свичийн глобал тохиргооны горимд шилжинэ.

# Шинэ user нэмж өгнө.
tn.write(b"username barsbold password 1234 1\n")  
tn.write(b"end \n")                  # Тохиргооноос гарна.
tn.write(b"exit \n")   