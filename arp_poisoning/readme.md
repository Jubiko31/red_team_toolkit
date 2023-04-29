# ARP Poisoning/Spoofing Attack & Detector

## Description
<i>DISCLAIMER: educational purposes only.</i>
ARP spoofing is the Man-in-The-Middle (MiTM) attack that allows to intercept communication between network devices. Thus, hacker can gain access to any sensitive data sent through network, or even execute more advanced attacks.
<ul>
    <li><b>arp_spoofer.py</b> - Execute ARP spoofing attack on target network.</li>
    <li><b>arpspoof_detector.py</b> - Monitor network to detect ARP spoofing.</li>
</ul>

## Attack Anatomy
The basic principle behind ARP spoofing is to exploit the lack of authentication in the ARP protocol by sending spoofed ARP messages onto the LAN. Attacker send fake ARP packets, saying to AP (Access Point) that his MAC address is X which actually is victim's one, and tells victim's device that Y is AP MAC address, which is attacker's device. Thus, we are in the middle of the connection. Just need to enable port forwarding so target will have normal internet access.
<p align="center">
  <img src="https://user-images.githubusercontent.com/53910160/235319476-e3edfe0d-f4b2-4765-879c-a3f0e13e9aae.png" width="700px"/>
</p>

### Requirements
Python v3

Scapy


## Run

## ARP Spoofer:
```sh
$ python arp_spoofer --interface <target_interface> --target <target_ip> <spoofing_ip>
```

![image](https://user-images.githubusercontent.com/53910160/235319666-656929cb-9886-4922-bc9d-640f834fa799.png)

Exit & Restore ARP tables:

![image](https://user-images.githubusercontent.com/53910160/235319672-703f3d04-8cd6-4e99-9fa2-f34197de2c01.png)



## ARP Spoofing Detector
```sh
$ python arpspoof_detector.py -i <interface>
```

![image](https://user-images.githubusercontent.com/53910160/235319679-250fb5bc-ee70-42e2-a401-de86eaffb798.png)
