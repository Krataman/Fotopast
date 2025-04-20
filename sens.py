from gpiozero import MotionSensor
from picamera2 import Picamera2
from PIL import Image
from time import sleep
from datetime import datetime
import os
import paramiko

# Funkce pro přenos souboru na server pomocí SFTP
def transfer_file(local_file, remote_file):
    try:
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        private_key_path = "/home/pi/.ssh/id_rsa"
        ssh_client.connect('79.98.75.116', port=1813, username='fotopast', key_filename=private_key_path)

        sftp = ssh_client.open_sftp()
        sftp.put(local_file, remote_file)
        print(f"Soubor {local_file} byl úspěšně přenesen na server.")

        sftp.close()
        ssh_client.close()
    except Exception as e:
        print(f"Chyba při přenosu souboru: {e}")

# PIR senzor na GPIO17
pir = MotionSensor(17)

# Inicializace kamery
camera = Picamera2()
camera.configure(camera.create_still_configuration())

# Adresář pro dočasné snímky
raw_dir = "/home/pi/raw"
os.makedirs(raw_dir, exist_ok=True)

try:
    camera.start()
    print("|| CAM is ready! ||")

    while True:
        if pir.motion_detected:
            print("MOTION detected!")

            for i in range(2):
                timestamp = datetime.now().strftime("%d_%m_%Y-%H_%M_%S")
                raw_filename = os.path.join(raw_dir, f"raw_snapshot_{timestamp}.jpg")
                remote_filename = f"/mnt/hdd-1tb/FOTOPAST/snapshot_{timestamp}.jpg"

                camera.capture_file(raw_filename)

                with Image.open(raw_filename) as img:
                    rotated_img = img.rotate(180, expand=True)
                    rotated_img.save(raw_filename)  # Přepíše původní soubor otočenou verzí

                transfer_file(raw_filename, remote_filename)
                os.remove(raw_filename)  # Smazání lokálního souboru po přenosu

               # sleep(0.1)  # Prodleva mezi snapshoty

        else:
            sleep(0.08)  # Malá prodleva pro šetření CPU

except KeyboardInterrupt:
    print("|| Program byl ukončen. ||")
finally:
    camera.stop()