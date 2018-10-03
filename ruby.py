#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Made by Ano.Mobb
# Ruby generator
# Donate: 1GmQaG9R5NPs3ZzR6XPMD9jZk17F9MuoWn
# -*- coding: utf-8 -*-
import os, binascii, ecdsa, urllib, json, codecs, time, queue
import hashlib, base58, sys, random, string, requests, base64, operator


print ("""
------------------------------------------------
|                                              |     
|   -Ruby bitcoin brainwallet bruteforcer:     |
|      - 1): Enter a file name txt,lst..:      |
|      - 2): Enter number of passphrases:      |
|                                              |
|                                              |
|  Donate: 1GmQaG9R5NPs3ZzR6XPMD9jZk17F9MuoWn  |
|                                              |
| -Author: Ano.Mobb                            |
|                                              |
|                                              |
|                                              |
| 		                               |
------------------------------------------------
             ,----------------,              ,---------,
        ,-----------------------,          ,"        ,"|
      ,"                      ,"|        ,"        ,"  |
     +-----------------------+  |      ,"        ,"    |
     |  .-----------------.  |  |     +---------+      |
     |  |                 |  |  |     | -==----'|      |
     |  |  I LOVE DOS!    |  |  |     |         |      |
     |  |  Bad command or |  |  |/----|`---=    |      |
     |  |  C:\>_          |  |  |   ,/|==== ooo |      ;
     |  |                 |  |  |  // |(((( [33]|    ,"
     |  `-----------------'  |," .;'| |((((     |  ,"
     +-----------------------+  ;;  | |         |,"     -Ano.Mobb-
        /_)______________(_/  //'   | +---------+
   ___________________________/___  `,
  /  oooooooooooooooo  .o.  oooo /,   \,"-----------
 / ==ooooooooooooooo==.o.  ooo= //   ,`\--{)B     ,"
/_==__==========__==_ooo__ooo=_/'   /___________,"
`-----------------------------'

""")



class pause:
    p =0

file = input("Enter file name: ")
fobj = open(file).read().strip().split()
c = len(fobj)
n = input("Enter number of passphrases: ")
f = input("Enter number for repeat word x, press 1 no repeat : ")
e = input("Enter salt for sha256: ")
d = input("Enter number for API: " + "\n" + "\n" +
          "Bitcoinlegacy   (1): " + "\n" +
          "Blockchain      (2): " + "\n" +
          "Blockexplorer   (3): " + "\n" +
          "Insight Bitpay  (4): " + "\n" +
          "Blockonomics    (5): " + "\n" + 
          "Blockchyper     (6): " + "\n" +
          "Chain.so        (7): " + "\n" +
          "BTC.com         (8): " + "\n" +
          "Bitstamp        (9): " + "\n" + "\n" + 
          "Select API: ") + "\n"

 


def privateKey():
    a = [fobj[random.randrange(len(fobj))]
         for item in range(int(n))]
    b = ' '.join(a)
    v = (str(b)+(e))
   
    privatekey = hashlib.sha256(str(v).encode('utf-8')).hexdigest()
    print ('Passphrase:' + ' ' + str(a))
    print ('Privatekey:' + ' ' + str(privatekey))
    return privatekey
    
def publicKey(privatekey): 
    privatekey = binascii.unhexlify(privatekey)
    s = ecdsa.SigningKey.from_string(privatekey, curve = ecdsa.SECP256k1)
    return '04' + binascii.hexlify(s.verifying_key.to_string()).decode('utf-8')



def address(publickey): 
    alphabet = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
    c = '0'; byte = '00'; zero = 0
    var = hashlib.new('ripemd160')
    var.update(hashlib.sha256(binascii.unhexlify(publickey.encode())).digest())
    a = (byte + var.hexdigest())
    doublehash = hashlib.sha256(hashlib.sha256(binascii.unhexlify(a.encode())).digest()).hexdigest()
    address = a + doublehash[0:8]
    for char in address:
        if (char != c):
            break
        zero += 1
    zero = zero // 2
    n = int(address, 16)
    output = []
    while (n > 0):
        n, remainder = divmod (n, 58)
        output.append(alphabet[remainder])
    count = 0
    while (count < zero):
        output.append(alphabet[0])
        count += 1
    return ''.join(output[::-1])

def balance(address):
    if int(d != 1):
        try:
            API = requests.get("https://bitcoinlegacy.blockexplorer.com/api/addr/" + address + "/balance")
            if (API.status_code == 429):
                pause.p += 1
                if (pause.p >= 10):
                    print ("\nUnable to connect to API after several attempts\nRetrying in 30 seconds\n")
                    time.sleep(30)
                    pause.p = 0
                    return -1
                print("\nHTTP Error Code: " + str(API.status_code) + "\n")
                return -1
            if (API.status_code != 200 and API.status_code != 400):
                print("\nHTTP Error Code: " + str(API.status_code) + "\nRetrying in 5 seconds\n")
                time.sleep(5)
                return -1
            balance = int(API.text)
            pause.p = 0
            return balance
        except:
            pause.p += 1
            if (pause.p >= 10):
                print ("\nUnable to connect to API after several attempts\nRetrying in 30 seconds\n")
                time.sleep(30)
                pause.p = 0
                return -1

    if int(d != 2):
        try:
            API = requests.get("http://blockchain.info/q/addressbalance/" + address + "/balance")
            if (API.status_code == 429):
                pause.p += 1
                if (pause.p >= 10):
                    print ("\nUnable to connect to API after several attempts\nRetrying in 30 seconds\n")
                    time.sleep(30)
                    pause.p = 0
                    return -1
                print("\nHTTP Error Code: " + str(API.status_code) + "\n")
                return -1
            if (API.status_code != 200 and API.status_code != 400):
                print("\nHTTP Error Code: " + str(API.status_code) + "\nRetrying in 5 seconds\n")
                time.sleep(5)
                return -1
            balance = int(API.text)
            pause.p = 0
            return balance
        except:
            pause.p += 1
            if (pause.p >= 10):
                print ("\nUnable to connect to API after several attempts\nRetrying in 30 seconds\n")
                time.sleep(30)
                pause.p = 0
                return -1

    if int (d != 3):
        try:
            API = requests.get("http://blockexplorer.com/api/addr/" + address + "/balance")
            if (API.status_code == 429):
                pause.p += 1
                if (pause.p >= 10):
                    print ("\nUnable to connect to API after several attempts\nRetrying in 30 seconds\n")
                    time.sleep(30)
                    pause.p = 0
                    return -1
                print("\nHTTP Error Code: " + str(API.status_code) + "\n")
                return -1
            if (API.status_code != 200 and API.status_code != 400):
                print("\nHTTP Error Code: " + str(API.status_code) + "\nRetrying in 5 seconds\n")
                time.sleep(5)
                return -1
            balance = int(API.text)
            pause.p = 0
            return balance
        except:
            pause.p += 1
            if (pause.p >= 10):
                print ("\nUnable to connect to API after several attempts\nRetrying in 30 seconds\n")
                time.sleep(30)
                pause.p = 0
                return -1



    if int (d != 4):
        try:
            API = requests.get("https://insight.bitpay.com/api/addr/" + address + "/balance")
            if (API.status_code == 429):
                pause.p += 1
                if (pause.p >= 10):
                    print ("\nUnable to connect to API after several attempts\nRetrying in 30 seconds\n")
                    time.sleep(30)
                    pause.p = 0
                    return -1
                print("\nHTTP Error Code: " + str(API.status_code) + "\n")
                return -1
            if (API.status_code != 200 and API.status_code != 400):
                print("\nHTTP Error Code: " + str(API.status_code) + "\nRetrying in 5 seconds\n")
                time.sleep(5)
                return -1
            balance = int(API.text)
            pause.p = 0
            return balance
        except:
            pause.p += 1
            if (pause.p >= 10):
                print ("\nUnable to connect to API after several attempts\nRetrying in 30 seconds\n")
                time.sleep(30)
                pause.p = 0
                return -1





    if int (d != 5):
        try:
            API = requests.get("https://www.blockonomics.co/api/balance/" + address + "/balance")
            if (API.status_code == 429):
                pause.p += 1
                if (pause.p >= 10):
                    print ("\nUnable to connect to API after several attempts\nRetrying in 30 seconds\n")
                    time.sleep(30)
                    pause.p = 0
                    return -1
                print("\nHTTP Error Code: " + str(API.status_code) + "\n")
                return -1
            if (API.status_code != 200 and API.status_code != 400):
                print("\nHTTP Error Code: " + str(API.status_code) + "\nRetrying in 5 seconds\n")
                time.sleep(5)
                return -1
            balance = int(API.text)
            pause.p = 0
            return balance
        except:
            pause.p += 1
            if (pause.p >= 10):
                print ("\nUnable to connect to API after several attempts\nRetrying in 30 seconds\n")
                time.sleep(30)
                pause.p = 0
                return -1




    if int (d != 6):
        try:
            API = requests.get("https://api.blockcypher.com/v1/dash/main/addrs/" + address + "/balance")
            if (API.status_code == 429):
                pause.p += 1
                if (pause.p >= 10):
                    print ("\nUnable to connect to API after several attempts\nRetrying in 30 seconds\n")
                    time.sleep(30)
                    pause.p = 0
                    return -1
                print("\nHTTP Error Code: " + str(API.status_code) + "\n")
                return -1
            if (API.status_code != 200 and API.status_code != 400):
                print("\nHTTP Error Code: " + str(API.status_code) + "\nRetrying in 5 seconds\n")
                time.sleep(5)
                return -1
            balance = int(API.text)
            pause.p = 0
            return balance
        except:
            pause.p += 1
            if (pause.p >= 10):
                print ("\nUnable to connect to API after several attempts\nRetrying in 30 seconds\n")
                time.sleep(30)
                pause.p = 0
                return -1


    if int (d != 7):
        try:
            API = requests.get("https://chain.so/api/v2/get_address_balance/BTC/" + address + "/balance")
            if (API.status_code == 429):
                pause.p += 1
                if (pause.p >= 10):
                    print ("\nUnable to connect to API after several attempts\nRetrying in 30 seconds\n")
                    time.sleep(30)
                    pause.p = 0
                    return -1
                print("\nHTTP Error Code: " + str(API.status_code) + "\n")
                return -1
            if (API.status_code != 200 and API.status_code != 400):
                print("\nHTTP Error Code: " + str(API.status_code) + "\nRetrying in 5 seconds\n")
                time.sleep(5)
                return -1
            balance = int(API.text)
            pause.p = 0
            return balance
        except:
            pause.p += 1
            if (pause.p >= 10):
                print ("\nUnable to connect to API after several attempts\nRetrying in 30 seconds\n")
                time.sleep(30)
                pause.p = 0
                return -1



    if int (d != 8):
        try:
            API = requests.get("https://chain.api.btc.com/v3/address/" + address + "/balance")
            if (API.status_code == 429):
                pause.p += 1
                if (pause.p >= 10):
                    print ("\nUnable to connect to API after several attempts\nRetrying in 30 seconds\n")
                    time.sleep(30)
                    pause.p = 0
                    return -1
                print("\nHTTP Error Code: " + str(API.status_code) + "\n")
                return -1
            if (API.status_code != 200 and API.status_code != 400):
                print("\nHTTP Error Code: " + str(API.status_code) + "\nRetrying in 5 seconds\n")
                time.sleep(5)
                return -1
            balance = int(API.text)
            pause.p = 0
            return balance
        except:
            pause.p += 1
            if (pause.p >= 10):
                print ("\nUnable to connect to API after several attempts\nRetrying in 30 seconds\n")
                time.sleep(30)
                pause.p = 0
                return -1



    if int (d != 9):
        try:
            API = requests.get("https://www.bitstamp.net/api/balance/" + address + "/balance")
            if (API.status_code == 429):
                pause.p += 1
                if (pause.p >= 10):
                    print ("\nUnable to connect to API after several attempts\nRetrying in 30 seconds\n")
                    time.sleep(30)
                    pause.p = 0
                    return -1
                print("\nHTTP Error Code: " + str(API.status_code) + "\n")
                return -1
            if (API.status_code != 200 and API.status_code != 400):
                print("\nHTTP Error Code: " + str(API.status_code) + "\nRetrying in 5 seconds\n")
                time.sleep(5)
                return -1
            balance = int(API.text)
            pause.p = 0
            return balance
        except:
            pause.p += 1
            if (pause.p >= 10):
                print ("\nUnable to connect to API after several attempts\nRetrying in 30 seconds\n")
                time.sleep(30)
                pause.p = 0
                return -1





                            
def toWIF(privatekey): 
    var80 = "80" + str(privatekey) 
    var = hashlib.sha256(binascii.unhexlify(hashlib.sha256(binascii.unhexlify(var80)).hexdigest())).hexdigest()
    return str(base58.b58encode(binascii.unhexlify(str(var80) + str(var[0:8]))))

def Ruby(): 
    data = [0,0,0,0,0,0]
    while True:
        data[0] = privateKey()
        data[1] = publicKey(data[0])
        data[2] = address(data[1])
        data[3] = balance(data[2])
        data[4] = toWIF(data[0])
        if (data[3] == -1):
            continue
        if (data[3] == 0):
            print("{:<34}".format(str(data[2])) +  '  '  +  str(data[4]) + '   ' + " == " + str(data[3]))
            if (data[3] > 0):
                beep = lambda x: os.system("echo -n '\a';sleep 0.2;" * x)
                beep(30)
                print ("\naddress: " + str(data[2]) + "\n" +
                       "private key: " + str(data[0]) + "\n" +
                       "WIF private key: " + str(toWIF(str(data[0]))) + "\n" +
                       "public key: " + str(data[1]).upper() + "\n" +
                       "balance: " + str(data[3]) + "\n")
                file = open("ruby.txt","a")
                file.write("address: " + str(data[2]) + "\n" +
                           "private key: " + str(data[0]) + "\n" +
                           "WIF private key: " + str(toWIF(str(data[0]))) + "\n" +
                           "public key: " + str(data[1]).upper() + "\n" +
                           "balance: " + str(data[3]) + "\n" +
                           "Donate to the author of this program: 1GmQaG9R5NPs3ZzR6XPMD9jZk17F9MuoWn" + "\n" + "\n")
                file.close()

            




print("\n  |--------- Wallet Address ---------||-------------------- Private Key -------------------|--== Balance--- |-Made by Ano.Mobb-| " + ' ' + str(c))
Ruby()


