import argparse, time, os, csv
from sniffndetect import SniffnDetect


#Taking input from the user for the interface and the victim ip
parser = argparse.ArgumentParser(description="DoS detection simulation")
parser.add_argument("--iface", default="lo")
parser.add_argument("--victim-ip", default="127.0.0.1")
args = parser.parse_args()


#Making the detector and telling it which interface to listen on and who the victim is
d = SniffnDetect()
d.INTERFACE = args.iface
d.MY_IP = args.victim_ip

#creating the first row once if the csv does not exist
if not os.path.exists(d.CSV_FILE):
    with open(d.CSV_FILE, "w", newline="") as f:
        csv.writer(f).writerow(["timestampp", "attack_type", "source_ip", "length"])


#Starting the detector and keeping it running until i stop it
d.start()
print(f"Detecting it on {d.INTERFACE}, the victim IP {d.MY_IP}")
while True:
    time.sleep(1)
