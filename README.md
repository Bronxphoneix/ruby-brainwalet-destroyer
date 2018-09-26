
# Made by Ano.mobb

'''
# Ruby brainwallet destroyer
'''
Bitcoin Brainwallet Brute Forcer
'''
Donate to the author of this program: 1GmQaG9R5NPs3ZzR6XPMD9jZk17F9MuoWn
```

#

# Installation

<b> Python 3.4.0 Required </b> 

<b>A Constant Internet Connection Is Required</b>

Installation: 

```
$ git clone https://github.com/mobb111/ruby-brainwallet-destroyer

$ cd ruby-brainwallet-destroyer

$ pip install -r requirements.txt 
```

#

# Usage
'''
$ cd ruby-brainwallet-destroyer

$ python ruby.py

"Enter number of passphrases:
"Enter number for repeat word x, press 1 no repeat : "
"Enter salt for sha256: "
"Enter number for API: "
"Bitcoinlegacy   (1): "
"Blockchain      (2): "
"Blockexplorer   (3): "
"Insight Bitpay  (4): "
"Blockonomics    (5): "
"Blockchyper     (6): "
"Chain.so        (7): "
"BTC.com         (8): "
"Bitstamp        (9): "
"Select API: "


```
<br>
'''
# Proof of Concept

This program is meant to analyze possible ways Bitcoin could be stolen. Because it is impossible to convert a wallet address back into its private key, this program goes from passphrases and generates a privatekey, then converts it into its respective Bitcoin address. It then queries the calculated address for a balance and <a href="#expected-outputs">prints the result</a> to the user.

This program does this in a brute-force style, repeatedly generating and converting private keys, and querying balances. The ultimate goal is to randomly find a wallet with a balance out of the 2<sup>160</sup> possible wallets in existence. In the event that a wallet with a balance is found, the wallet's private key, public key, wallet address, and balance is stored in a text file `rubygen.txt` for later use.

Although this project can be used maliciously, it is simply an exploration into the Bitcoin protocol and advanced encryption and hashing techniques using Python.
'''

#

# How it Works

Private keys are generated from passphrases to create 32 byte hexidecimal string using the cryptographically secure `sha256()` function.

The private keys are converted into their respective public keys. Then the public keys are converted into their Bitcoin wallet addresses using the `binascii`, `ecdsa`, and `hashlib` Python modules.

The wallet addresses are queried using <a 

1) "https://bitcoinlegacy.blockexplorer.com/api-ref" 
2) "http://blockchain.info/q/addressbalance/"
3) "http://blockexplorer.com/api/addr/"
4) "https://insight.bitpay.com/api/addr/"
5) "https://www.blockonomics.co/api/balance/"
6) "https://api.blockcypher.com/v1/dash/main/addrs/"
7) "https://chain.so/api/v2/get_address_balance/BTC/"
8) "https://chain.api.btc.com/v3/address/"
9) "https://www.bitstamp.net/api/balance/"




Explorer API</a> to collect balance details.

If the wallet contains a balance, then the private key, public key, wallet address, and balance are saved to a text file `ruby.txt` on the user's hard drive.
'''


#

# Expected Outputs

If the wallet is empty, then the format `Wallet Address == 0` will be printed. An example is:
'''
Passphrase: ['inversa', 'precurse', 'autonomy']
Privatekey: 32b34f25a749f84438533ca93e8a5fc86e43af28a948b65c2e406d65d6780675
1Bopy7AVixCSupeXrKxbSFnaemavwALuNj  b'5JCcezYvd8CApZ7ebmZnTu6vk1q5XymfheW19TnXBW6CjCDSmDT'    == 0
Passphrase: ['prologue', 'watchout', 'sbatte']
Privatekey: e5ade198e5cb65d2af1d83b0cb2eeef2cb12319d45ee65098f83e8a33444b1b0
1DeovhdVX88XVmPS36DcPNiRzByNrKQGNS  b'5KZSRqTPUFvPkJfF1FLQmRt6AHpkVKEsG4Qw1tBcvoEfRxwZCTB'    == 0
Passphrase: ['tumife', 'irrigare', 'rehumiliation']
Privatekey: 8dc79408310189df37576a5733d8ae66b2fdc210072f9306f1e6cddadf36001c
1NBZAxdTUmgR6PDGpAexrYXyLV9ANbePdB  b'5Jtj9inJJ6XjukKuFUPeWx2uLBGGsTEVRqEudy6dR8qn9LausmP'    == 0
Passphrase: ['carcinemia', 'prebendate', 'flummox']
Privatekey: a0a3cec16c9bed19e673525c8c70ae936f0f329b05478c81496deca6f0a06c96
1Nc657MrTTJwN3TU9xoKjXA7ozJAoVzZUU  b'5K32upU4hHJZjAonwL4oCVPz12AP65LnxnsGs8dXrvXAMP4Nhxh'    == 0
Passphrase: ['chinawoman', 'hushedly', 'semiconvergent']
Privatekey: 00d67438ae39aec90eb1996ac5e7f8426ca7fa87134af14cfa3276d4ca8145cf
12D3LvzSrMoZiMbaujFzmExuXqwyf6Qtqf  b'5Hpeymzo8vhFwzM8hpwwwQQXLtC1KqYZ37j6nFpzxB8oWqQgrkB'    == 0
Passphrase: ['sgravare', 'wayworn', 'monophyleticism']
Privatekey: b09862ccf869d4239e2b79dada56c823a2a51904ef5ac77416e8d931c152b868
1K9sadcUnMVMCoSvHKKPDGXiWJLwTo9K97  b'5KA4UEWEPB3PqGRYXsK1zkCMnSAcBUSPhHJjVfjhWf28apYt3u4'    == 0
'''
 
However, if a balance is found, then the output will include all necessary information about the wallet. A copy of the output will also be saved in a text file titled `rudygen.txt` with all balances in Satoshi. An example is:

>address: 1JGM6sREUwt5paFEfHNuzvRy7nXtQdaamn<br>
>private key: 6694e2d40e786839d48b1b699ab9c318514dc0a0f27f2ccaf7f9f32224ead3a8<br>
>WIF private key: 5JbTtbihnAnNbBtqZKmkWbrDUeei1bCamqKPrHJ49vQx1CT8oUQ<br>
>public key: 04475C43E9E58637630E10DB01F2FF38C64430E07E272E4C82C877653B8AF15720E4F98F66B49BB4E91B36D4C08FC4F2E13F0A5079DFCEB1821FA05A9F9F30F361<br>
>balance: 10000000

#

# Warnings

If you are receiving: 

>HTTP Error Code: (number)<br/>
>Retrying in 5 seconds

Or

>Unable to connect to API after several attempts<br>
>Retrying in 30 seconds

This program queries Block Explorer API for wallet balances making a HTTP request necessary for complete operation. If connection to the API is found to be unresponsive (failing to return a 200 HTTP status) the program will pause for 5 seconds and attempt to continue.

If you are receiving a lot of errors, visit <a href="https://bitcoinlegacy.blockexplorer.com/">Blockexplorer.com</a> to see if their API might be down.

This program also responds to 429 HTTP responses because of the high frequency of server requests. When a 429 is encountered, the program will print the error `HTTP Error Code: 429`, but will not pause. However, if several 429's are received consecutively, the user will get the result `Unable to connect to API after several attempts` and will be forced to wait 30 seconds until the program continues again.

#

# Efficiency

This program is able to handle, generate, and query a private key in 0.5 seconds. However, because this program uses the internet for balance requests, a slower internet connection may impact time efficiency.

#

```
If u find this program to be usefull please,
Donate to the author of this program: 1GmQaG9R5NPs3ZzR6XPMD9jZk17F9MuoWn
```

#
