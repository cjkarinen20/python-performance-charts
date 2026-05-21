import threading 
from scapy.all import ICMP, IP, srl, sendp, Ether
import time
import statistics

# Global variables to hold measurement results
latency_results = []
packet_loss_count = 0
total_packets_sent = 0

def measure_latency(target_ip, count = 5):
    pass

def measure_bandwidth(target_ip, size = 1000, duration = 5):
    pass

def print_results():
    pass

def main(target_ip):
    pass

if __name__ == "__main__":
    target_ip = "8.8.8.8"
    main(target_ip)