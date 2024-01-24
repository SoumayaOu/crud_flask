Gestion des partenaires : 
 
- L’objectif principal de ce projet réside dans la gestion des partenaires de Cash plus en utilisant FLASK et l’ORM SqlAlchemy. Pour cela, nous avons procédé par l ‘implémentation d’une application CRUD qui mène à  créer, afficher, modifier et supprimer un ou plusieurs partenaires. Chaque partenaire possède un ensemble de caractéristiques qui le décrivent à savoir :

*  Son type ( Marchands, Facturiers, MTO).
*  Son code.
*  Son nom.
*  Son contact.
*  Son logo.
*  Son icone. 

- Un partenaire est défini et spécifié par un couple (type, code) unique, ou ces deux champs sont immutable.

- Les champs type, code, contact et logo sont obligatoires lors de la création d’une nouvelle instance. Quand au champ icône, il  est facultatif et en cas d’ absence une copie du logo lui sera affectée.

- Lors de la saisie des logos et des icônes, des contraintes ont été effectuées notamment l’extension de l’image qui doit être « .png » ainsi la taille qui doit être supérieure ou égale à 100x100 pixels.

- Une fois que le nouveau partenaire a été créé avec succès, un ensemble d’images en miniatures avec des tailles de 16, 24, 32, 64 pixels  sont générées pour chaque type d’image (icône, logo) pour nous servir pour la suite dans la version mobile.

- Afin d’optimiser et minimiser le transfert des requêtes http et gagner en temps de chargement des pages web, nous avons penser à implémenter des sprites qui servent à regrouper des images dans une seule image. Pour chaque type d’image et pour chaque taille une sprite a été créée avec son fichier CSS  permettant ainsi un  accès plus rapide aux images générées préalablement .

- Enfin, nous avons établie l’authentification avec l’extension Flask-Login pour la gestion de la session des utilisateurs.







