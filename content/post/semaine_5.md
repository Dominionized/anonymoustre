+++
date = "2016-02-17T10:41:25-05:00"
description = "Traitement des informations et présentation des données"
title = "Semaine 5"

+++

Nous avons principalement fait de la recherche d'informations sur les DNSBL/RBL (Realtime blacklists) afin d'avoir des filtres de *spam* pour les adresses IP. Il existe plusieurs services en ligne qui font l'aggrégation de *blacklists*, tels que [URLVoid](http://www.urlvoid.com/) (IPVoid) et [MxToolBox](http://mxtoolbox.com/). Il reste à vérifier que les résultats retournés par ces services sont fiables.

Il existe aussi [SORBS](http://www.sorbs.net/), [ASPEWS](http://www.aspews.org/) et [Spamhaus ZEN](https://www.spamhaus.org/) qui sont des DNSBL populaires et gratuites. Spamhaus est une liste intéressante, puisqu'elle est aussi actualisée avec les adresses IP de *malwares*. Ces listes sont toutefois légèrement plus difficiles à accéder via Python, puisqu'elle demandent d'être intérogées via une requête DNS.

L'utilitaire `dig` inclus dans la suite d'outils [BIND](https://www.isc.org/downloads/bind/) permet de faire une telle requête.

Exemple (en ligne de commande) : 
```shell
dig +short 156.142.77.110.spam.dnsbl.sorbs.net
// 127.0.0.6
```

Le résultat `127.0.0.6` indique que l'adresse IP `110.77.142.156` dont les octets ont été renversés dans la requête à l'adresse `156.142.77.110.spam.dnsbl.sorbs.net` est considéré comme étant liée à un hôte qui envoie du *spam*. 

Également, nous avons étendu notre programme de filtrage d'adresses IP avec un module qui se connecte à l'API de [Shodan.IO](https://www.shodan.io). Cela nous permet de faire la collecte de métadonnées sur des adresses IP (géolocalisation, fournisseur d'accès à internet, WHOIS, etc.) et des données plus techniques, telles que les services offerts et les ports ouverts sur le point d'accès. Nous allons donc délaisser plusieurs options que nous avons exploré auparavant, puisque Shodan est programmable, gratuit et qu'il donne un rapport assez complet d'une point d'accès.

Nous vérifions aussi les dates d'expiration des certificats SSL pour les services offerts par une adresse IP avec l'API de Shodan.IO. Bien sûr, cette vérification est encore trop minimale pour réellement vérifier la validité d'un certificat SSL. Plusieurs autres facteurs pourraient être vérifiés :

* les authorités de certification;
* le *Common Name*;
* la function de hashage utilisée;
* la taille de la paire de clés RSA (2048 bits ou plus).

Dans le cadre de ce projet, nous n'aurons toutefois pas le temps d'ajouter ces facteurs de sécurité. Nous n'aurons également pas le temps d'ajouter BurpSuite en tant qu'outil de vérification de sécurité Web à notre système.

Dans l'espoir d'avoir accès à une plateforme qui fait l'aggrégation de *blacklists* de serveur mail, nous avons contacté un Chad James, un représentant chez MxToolBox, en espérant obtenir un accès à leur interface de programmation. C'est un succès ! Nous pouvons maintenant intégrer leur plateforme à notre projet. Le nombre de requêtes par jour est toutefois limité à 10.

[Cliquer ici pour voir la conversation.](/anonymoustre/files/MXToolBox_Email.pdf)

Nous avons maintenant un service web afin de présenter visuellement notre outil. Des scores pour les catégories *malware*, *phishing*, *unwanted* et *unsecure (SSL)* sont disponibles. Nous avons donc décider de laisser Maltego de côté.

![Anonymoustre platform](/anonymoustre/files/anon_web.png)

*La première adresse IP a plusieurs services disponibles, qui ont tous un certificat SSL expiré.*

Il reste donc à ajouter les *blacklists* à l'algorithme de calcul de réputation de notre outil, pour obtenir des résultats plus précis au niveau du phishing et d'une catégorie qui serait le *spam*. 

Après cela, il faudra penser à finaliser le projet de recherche et préparer un média de présentation. 

Après une discussion avec François mercredi passé, nous avons décidé d'ajouter du contenu à notre présentation qui n'est pas lié à notre sujet de recherche. Nous parlerons de Shodan.IO comme engin de recherche pour les [caméras de sécurité non-sécurisées](http://globalnews.ca/news/2478442/shodan-search-engine-browses-vulnerable-baby-monitors-webcams/).