import threading 
from scapy.all import ICMP, IP, sr1, sendp, Ether
import time
import statistics

# Global variables to hold measurement results
latency_results = []
packet_loss_count = 0
total_packets_sent = 0

def measure_latency(target_ip, count = 5):
    global latency_results
    for _ in range(count):
        start_time = time.time()
        reply = sr1(IP(dst = target_ip) / ICMP(), verbose = 0, timeout = 2)
        
        if reply:
            round_trip_time = (time.time() - start_time) * 1000 # Convert to milliseconds
            latency_results.append(round_trip_time)
        else:
            global packet_loss_count
            packet_loss_count += 1
            
        time.sleep(1) # Wait for a second before the next ping

def measure_bandwidth(target_ip, size = 1000, duration = 5):
    pass

def print_results():
    pass

def main(target_ip):
    pass

if __name__ == "__main__":
    target_ip = "8.8.8.8"
    main(target_ip)