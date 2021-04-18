import math
import re

def splitSpecial(word):
    return [char for char in word] 
 
def intToHexWith0(n):
    
    binTemp = bin(int(n, 16))
    binTemp = int(binTemp,2)
    binTemp =  format(binTemp, '#016b')
    binTemp = binTemp[2:]     
    
    return binTemp

def binaryStringToHex(hexa):  
    binary_string = hexa
    
    return '%0*X' % ((len(binary_string) + 3) // 4, int(binary_string, 2))
 
def isMultipleof16(n):
    while ( n > 0 ):
        n = n - 16
    if ( n == 0 ):
        return 1
    return 0 

def toBin(x):
    return toBin(x//2) + [x%2] if x > 1 else [x]

def checkIpv4Format(ip, maskOrIp):
    
    splittedIP = ip.split(".")
    count = len(splittedIP)
    
    errorMessage = "IP erroné"
    if(maskOrIp == "masque"):
        errorMessage = "Masque erroné"
    if(count != 4):
        raise Exception(errorMessage)
    for i in range(len(splittedIP)):
        
        try:
            splittedIPToInt = int(splittedIP[i])
        except:
            raise Exception(errorMessage)
        finally:
            if splittedIPToInt < 0 or splittedIPToInt > 255:
                raise Exception(errorMessage)    

def checkPrefix(prefix, type):
    prefixInt = 0
    try:
        prefixInt = int(prefix)
    except:
        raise Exception("Prefixe erroné")
    finally:
        if type == "IPv4":
            if prefixInt < 1 or prefixInt > 32:
                raise Exception("Prefixe erroné")
        else:
            if prefixInt < 1 or prefixInt > 128:
                raise Exception("Prefixe erroné")
        
def getNetworkClass(ip):

    splittedIP = ip.split(".")
    splittedIPToInt = int(splittedIP[0])
    if  1 <= splittedIPToInt < 127:
        return "A"
    if 128 <= splittedIPToInt < 192:
        return "B"
    if 192 <= splittedIPToInt < 224:
        return "C"
    else:
        raise Exception("Undefined IP Adress")    


def getNetworkMask(ip):
    
    classeA = "255.0.0.0"
    classeB = "255.255.0.0"
    classeC = "255.255.255.0"

    if(getNetworkClass(ip) == "A"):
        return classeA
    if(getNetworkClass(ip) == "B"):
        return classeB
    if(getNetworkClass(ip) == "C"):
        return classeC        

def getNetworkAddress(ip, mask):
    
    response = ""
    splitted_IP = ip.split(".")
    splitted_mask = mask.split(".")
    for i in range(len(splitted_IP)):
        splittedIPInt = int(splitted_IP[i])
        maskSplitInt = int(splitted_mask[i])
        
        if(i == 0):
            response = str(splittedIPInt & maskSplitInt)
        else:
            response = response + "." + str(splittedIPInt & maskSplitInt)
    return response

def onesComplement(n):
    if(n == 0):
        return 255
    nombreBits = (int)(math.floor(math.log(n)/math.log(2)))+1
    return ((1 << nombreBits) - 1)^n

def getBroadcatAddress(ip, mask):   
    broadcast = ""
    splittedIP = ip.split(".")
    maskSplit = mask.split(".")
    
    for i in range(len(splittedIP)):
        if i == 0:
            broadcast = str(onesComplement(int(maskSplit[i])) |  int(splittedIP[i]))
        else:
            broadcast = broadcast + "." + str(onesComplement(int(maskSplit[i])) |  int(splittedIP[i]))
        
    return broadcast

def getLastOrder(ip, mask):
    lastOrder = str(int(getBroadcatAddress(ip, mask).split(".")[0])) + "." + str(int(getBroadcatAddress(ip, mask).split(".")[1])) + "." + str(int(getBroadcatAddress(ip, mask).split(".")[2])) + "." + str(int(getBroadcatAddress(ip, mask).split(".")[3])-1)
    return lastOrder

def getFirstOrder(ip, mask):  
    firstOrder = str(int(getNetworkAddress(ip, mask).split(".")[0])) + "." + str(int(getNetworkAddress(ip, mask).split(".")[1])) + "." + str(int(getNetworkAddress(ip, mask).split(".")[2])) + "." + str(int(getNetworkAddress(ip, mask).split(".")[3]) + 1)
    return firstOrder

def getHostPartIndex(ip):
    if(getNetworkClass(ip) == 'A'):
        return 1
    if(getNetworkClass(ip) == 'B'):
        return 2
    if(getNetworkClass(ip) == 'C'):
        return 3

def hostBit(ip):
    return (4-getHostPartIndex(ip))*8

def getAddressNumber(ip):    
    numberOf = pow(2,hostBit(ip))-2
    return numberOf
 
def decimalToSubnet(n):
    if n == 1:
        return 128 
    if n == 2:
        return 192
    if n == 3:
        return 224
    if n == 4:
        return 240
    if n == 5:
        return 248
    if n == 6:
        return 252
    if n == 7:
        return 254
    if n == 8:
        return 255                      

def getNetworkMaskSpecial(prefix):
    
    if prefix < 8:
        return decimalToSubnet(prefix)+".0.0.0"
    
    subnetMask = ""
    i = 0
    while(prefix >= 8):
        prefix = prefix - 8
        i = i + 1
        
    for index in range(i):
        initial = "255"
        if(index == 0):
            subnetMask = initial
        else:
            subnetMask = subnetMask +  "." + initial
    
    subnetMask = subnetMask + "." + str(decimalToSubnet(prefix))  
      
    while(len(subnetMask.split("."))!=4):
        subnetMask = subnetMask + ".0"

    return subnetMask

def hostBitSpecial(prefix):
    return 32-prefix

def getAddressNumberSpecial(prefix):
    numberOf = pow(2, hostBitSpecial(prefix))-2
    return numberOf

def checkIpv6Format(ip):
    
    splittedIP = ip.split(":")
    count = len(splittedIP)
    
    if(count != 8):
        raise Exception("IP erroné")
    for i in range(count):
        try:
            hex(int("0x"+(splittedIP[i]), 16))
        except:
            raise Exception("IP erroné")    
        finally:
            if(len(splitSpecial(splittedIP[i]))!=4):
                raise Exception("IP erroné") 

def getIPv6Compressed(ip):
    
    noZero = ip.replace("0000","*");
    noZero = re.sub(":0+",":",noZero)
    noZero = re.sub(":\\*:\\*(:\\*)+:","::",noZero)
    noZero = re.sub("::\\*","::",noZero)
    noZero = noZero.replace("*", "0")
    return noZero
 
def mergeSplitHex(hex): 
    ipv6  = ""
    for i in range(len(hex)):
        if( (isMultipleof16(i+1) == 1) and i != (len(hex)-1) ):
            ipv6 = ipv6 + hex[i] + ":" 
        else:
            ipv6 = ipv6 + hex[i]      
            
    return ipv6

def binaryStringToHexSpecial(hexa): 
    hexaSplit = hexa.split(":")
    hexadecimal = ""
    
    for i in range(len(hexaSplit)):
        if(i == 0):
            hexadecimal = binaryStringToHex(hexaSplit[i])
        else:
            hexadecimal = hexadecimal + ":" + binaryStringToHex(hexaSplit[i])
              
    return hexadecimal

def networkAddress(ip, prefix):
    
    splittedIP = ip.split(":")
    binaryIp = ""
    binaryPrefixWithoutDelimiter = ""
    networkAddress = ""
    
    for i in range(len(splittedIP)):
        binTemp = intToHexWith0(splittedIP[i])
        
        binTemp = binTemp.zfill(16) 
        if(i == 0):
            binaryIp = binTemp
        else:
            binaryIp = binaryIp + binTemp
            
    binarySplit = splitSpecial(binaryIp)
    
    for j in range(len(binarySplit)):
        if(j > (prefix-1)):
            binarySplit[j] = '0'
    networkAddress = binaryStringToHexSpecial(mergeSplitHex(binarySplit))
    networkAddress = getIPv6Compressed(networkAddress)
    return networkAddress