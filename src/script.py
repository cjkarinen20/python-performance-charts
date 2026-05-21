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

# Measure bandwidth by sending packets and measuring the return rate
def measure_bandwidth(target_ip, size = 1000, duration = 5):
    start_time = time.time()
    packets_sent = 0
    while time.time() - start_time < duration:
        sendp(Ether() / IP(dst = target_ip) / ('X' * size), verbose = 0)
        packets_sent += 1
        time.sleep(0.1) # Send 10 packets per second
    global total_packets_sent
    total_packets_sent = packets_sent

def print_results():
    if latency_results:
        print(f"Average Latency: {statistics.mean(latency_results):.2f} ms")
        print(f"Average Latency: {min(latency_results):.2f} ms")
        print(f"Average Latency: {max(latency_results):.2f} ms")
    print(f"Packet Loss: {(packet_loss_count / (len(latency_results) + packet_loss_count) * 100):.2f}%")
    if total_packets_sent > 0:
        print(f"Estimated Bandwidth: {total_packets_sent * 1000 * 8 / 5 / 1024:.2f} Kbps")
        
def main(target_ip):
    threads = []
    threads.append(threading.Thread(target = measure_latency, args = (target_ip,)))
    threads.append(threading.Thread(target = measure_bandwidth, args = (target_ip,)))

    # Start all threads
    for thread in threads:
        thread.start()
    
    # Wait for all threads to complete
    for thread in threads:
        thread.join()
        
    print_results

if __name__ == "__main__":
    target_ip = "8.8.8.8"
    main(target_ip)