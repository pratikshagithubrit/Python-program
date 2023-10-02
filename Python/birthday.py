import smtplib
import email
ms=smtplib.SMTP('smtp.gmail.com',587)

ms.starttls()

ms.login("pratikshabpawar581@gmail.com","Pawar@581")

message="Happy Birthday marvellous infosystem"
ms.sendemail("pratikshabpawar581@gmail.com","marvellousinfosystems@gmail.com",message)
ms.quit()