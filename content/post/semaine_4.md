+++
date = "2016-02-11T16:45:38-05:00"
description = "Collecte d’informations, expérimentation et développer l’outil de présentation"
title = "Semaine 4"
+++

Au courant de la semaine, nous avons travaillé principalement avec l'API de Google Safe Browsing, qui nous donne accès à un filtre pour des domaines classés comme étant malveillants. Nous avons commencer à écrire un script en Python afin de tester cet outil. Nous espérons pouvoir affecter la métrique qui représente la réputation d'une adresse IP à partir du résultat que Google nous retourne (*phishing*, *malware* ou *unwanted*) Le code est disponible directement sur [GitHub](https://github.com/Dominionized/anonymoustre).

Il existe des APIs pour la géolocalisation d'adresses IP, tel que [freegeoip](http://freegeoip.net/) qui utilise la base de données [GeoLite2](http://dev.maxmind.com/geoip/geoip2/geolite2/) pour analyser les requêtes. Nous pensons éventuellement intégrer la géolocalisation dans le calcul de la métrique de sécurité.

Une liste de domaines bloqués pour spam dans les courriels est disponible sur le portail de [Wikimedia](https://meta.wikimedia.org/wiki/Spam_blacklist). La liste est formattée sous forme d'expressions régulières, ce qui pourrait aider pour filtrer des noms de domaine.

Une autre *blacklist* similaire, cette fois-ci sous forme textuelle est disponible sur [jwSpamSpy](http://www.joewein.de/sw/spam-bl-s.htm).

Des outils semblables sont disponibles sur le portail de [Select Real Security](http://www.selectrealsecurity.com/public-block-lists). Il faudra toutefois faire un tri de ces outils et vérifier qu'ils sont bel et bien fiables.

[BurpSuite](https://portswigger.net/burp/) pourrait être une système de test intéressant à utiliser, si nous trouvons le temps pour automatiser le logiciel. Il nous permettrait de rouler des tests sur des applications web pour trouver des failles potentielles. Si nous ne trouvons pas le temps de mettre en place un tel système, nous pourrions toujours tester la validité des certificats SSL pour les adresses IP. Cette option serait probablement plus rapide à implémenter et nous donnerais une autre métrique à prendre en compte dans le calcul de la réputation d'adresses IP.

Nous avons fait un essai du programme [Maltego](https://www.paterva.com/web6/) qui pourrait nous être utile pour faire de la collecte d'informations. Le logiciel, étant très visuel, pourrait également être utilisé comme outil de présentation (merci à François Gagnon pour la référence). 

Nous avons d'ailleurs envoyé un message à François Gagnon en date du 11 février 2016 pour demander s'il était possible d'avoir une banque d'adresses IP avec des métadonnées.

Pour terminer, nous sommes légèrement en retard par rapport au plan de travail que nous avons mis en place à la première semaine du projet de recherche. Il faudra porter attention à la progression générale du projet au cours des prochains jours et trouver un moyen de corriger la situation au besoin.

#### Modification (11 février 2016, à 22:24) :
Nous avons eu la réponse de François. Selon lui, chaque métrique dans le calcul de la réputation d'une adresse IP devrait avoir sa propre banque d'adresses. De cette manière, une ou plusieurs métriques seront associées pour chaque adresse IP. Initialement, nous n'avons pas approché le problème de cette manière, mais c'est un point de vue très intéressant. François nous a également fourni dans son message un [lien](https://zeltser.com/malicious-ip-blocklists/) vers plusieurs *blocklists* que nous pourrons utiliser au cours du projet. Il propose aussi de chercher pour des listes de sites de *phishing*. 
