#creation d'un serveur utilisant les thread pour ne pas attendre que le second client reponde pour renvoyer message
#definition de l'adresse ip et du port d'ecoute du systeme hote
HOST = '192.168.0.39'
PORT = 42000
 
import socket, sys, threading
 
class ThreadClient(threading.Thread):
    '''creation d'un objet thread pour que le client communique a travers le reseau''' # documentation de la classe
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.connexion = conn
 
    def run(self):
        # Dialogue avec le client :
        nom = self.getName()        # Chaque thread possède un nom
        while 1:
            msgClient = self.connexion.recv(2048) #codage 2048 octets pour gerer des message de plus grande taille
            if msgClient.upper() == "STOP" or msgClient =="": #Si le client envoie STOP ou un espace la discussion prend fin
                break
            message = "%s> %s" % (nom, msgClient)
            print (message)#nous pouvons voir la discussion sur le serveur
            # Envoie du message à tous les autres clients :
            for cle in conn_client:
#                if cle != nom:      # ne pas le renvoyer à l'émetteur
                conn_client[cle].send(message)
 
        # Fermeture de la connexion :
        self.connexion.close()      # Couper la connexion côté serveur
        del conn_client[nom]        # Supprimer son entrée dans le dictionnaire
        print (u"Client %s déconnecté." % nom)
          
# Fermeture du thread
# programme principale (main), lancement des sockets
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


try:
    mySocket.bind((HOST, PORT))
except socket.error:
    print ("La liaison du socket à l'adresse choisie a échoué.")
    sys.exit()

print ("Serveur prêt, en attente de requêtes ...")
mySocket.listen(2)#possibilité de communiquer entre 2 personnes sur cryptochat

# Attente et prise en charge des clients :
conn_client = {}                # dictionnaire des connexions clients
while 1:    
    connexion, adresse = mySocket.accept()
    # Créer un nouvel objet thread pour gérer la connexion :
    th = ThreadClient(connexion)
    th.start()
    # Mémoriser la connexion dans le dictionnaire : 
    it = th.getName()        # identifiant du thread
    conn_client[it] = connexion
    print ("Client %s connecté, adresse IP %s, port %s." %\
           (it, adresse[0], adresse[1]))
    # Dialogue avec le client :
    connexion.send("Vous êtes connecté. Envoyez vos messages.")
