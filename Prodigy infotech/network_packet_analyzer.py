from scapy.all import sniff, TCP, UDP, ICMP, DNS, IP, wrpcap

captured_packets = []

def packet_callback(packet):
    if packet.haslayer(TCP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        src_port = packet[TCP].sport
        dst_port = packet[TCP].dport
        print(f"[TCP] {src_ip}:{src_port} -> {dst_ip}:{dst_port}")
    elif packet.haslayer(UDP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        src_port = packet[UDP].sport
        dst_port = packet[UDP].dport
        print(f"[UDP] {src_ip}:{src_port} -> {dst_ip}:{dst_port}")
        if packet.haslayer(DNS):
            dns_query = packet[DNS].qd.qname.decode('utf-8')
            print(f"[DNS Query] {dns_query}")
    elif packet.haslayer(ICMP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        print(f"[ICMP] {src_ip} -> {dst_ip}")
    elif packet.haslayer(TCP) and (packet[TCP].sport == 80 or packet[TCP].dport == 80):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        print(f"[HTTP] {src_ip} -> {dst_ip}")
    captured_packets.append(packet)

if __name__ == "__main__":
    print("Starting packet capture...")
    sniff(prn=packet_callback, count=0)
    pcap_filename = "captured_packets.pcap"
    wrpcap(pcap_filename, captured_packets)
    print(f"Packets saved to {pcap_filename}")
