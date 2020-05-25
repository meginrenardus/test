# UDPPingerServer.py 
# We will need the following module
from socket import * 
import time
import logging


logging.basicConfig(filename='PingerLog.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')


def ping():
    hostSocket = socket(AF_INET, SOCK_DGRAM)
    hostSocket.bind((gethostname(),22200))
    
    logging.info(" Socket is successfully open !!")
    
    hostname = gethostname()
 
    IPAddr = gethostbyname(hostname)
    subnet = IPAddr.split('.')
    
    serverSub= str(subnet[0]+"."+subnet[1]+"."+subnet[2]+"." )

    
    for i in range (1,11):
        serverName= serverSub+ str(i)
        
        if serverName == IPAddr:
            continue
        serverPort= 22200
        message = "Hallo"
        logging.info ("Sending ["+message+"] to "+serverName+" ....")
#    hostSocket.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)        # sending a broadcast
    
        hostSocket.sendto(message.encode(),(serverName, serverPort))
        logging.info ("message is sent :)")

    logging.info("\nTrying to receive some messages ..")
    recvMessage, address = hostSocket.recvfrom(1024)
#    recvMessage= "Received From "+ str(address)+" : " + str(message.decode())
    logging.info("Received From "+ str(address)+" : " + message)
    serverName, serverPort = address
    i = 1
    p = 0
    while serverName and serverPort:
        if str(recvMessage.decode()) == "Hallo":
            logging.info("111111111")
            message = "%Flag1%1111111111111111111111%Flag1%" # the message
        
        elif str("%Flag1%1111111111111111111111%Flag1%")  == str(recvMessage.decode()) and p == 0:
            logging.info("222222222222")
            message = "%Flag1%1111111111111111111111%Flag1%" 
        
        elif str(recvMessage.decode()) is not str("%Flag1%1111111111111111111111%Flag1%") or p > 0:
            logging.info("333333333333")
            p = p+1
            message = "%Flag2%22222222222222222222%Flag2%" 

        hostSocket.sendto(message.encode(), (serverName, serverPort))  # The message that will be sent to the server
        #logging.info(message)
        recvMessage, address = hostSocket.recvfrom(1024)  # Receive from server address 
        serverName1 , serverPort1 = address
        
        while serverName1 != serverName or serverPort1 != serverPort:

            message = "Welkom To Pinger"
            logging.warning(" Message Recieved from Unknown hostIP OR portNr " + str(address) +" : "+ str(recvMessage.decode()))  
            hostSocket.sendto(message.encode(), (serverName1, serverPort1))
            recvMessage, address = hostSocket.recvfrom(1024)
            serverName1 , serverPort1 = address
            continue


        logging.info("Receieved From " + str(address)+ " : ["+ recvMessage.decode()+ "] nr: "+str(i))
        time.sleep(3)
        i = i+1
    clientSocket.close()# To close the socket
        


ping()

#clientSocket.close()# To close the socket


