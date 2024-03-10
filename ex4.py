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
  tn.read_until(b"Password: ")
  tn.write(password.encode("ascii") + b"\n")

tn.write(b"enable\n")                # Свичийн тохиргооны горимыг идэвхжүүлнэ.
tn.write(b"cisco\n")               
tn.write(b"conf t\n")                # Свичийн глобал тохиргооны горимд шилжинэ.
tn.write(b"interface loopback 1\n")  # Интерфейс дээр loopback үүсгэнэ.

# Интерфейсд хаяг оноож өгнө.
tn.write(b"ip addr 10.20.30.41 255.255.255.0\n")
tn.write(b"no sh\n")                 # Интерфейсийг асаана.
tn.write(b"end \n")                  # Тохиргооноос гарна.
tn.write(b"show ip int brief")       # Интерфейсийн жагсаалтыг харна.
tn.write(b"exit \n")