⚠️ Avertissement À l'attention des personnes souhaitant évaluer mes compétences en programmation :

Ce logiciel a été réalisé en **2021**, durant l'année de Terminale de mon bac général. Il n'a subi **aucune évolution significative depuis**, à l'exception des modifications nécessaires à sa publication en tant que dépôt public (suppression d'informations privées et ajout de ce README).

Il n'est donc **plus représentatif de mon niveau actuel** en programmation.

Sa mise en public a uniquement pour objectif de **« servir la communauté »** et de permettre à d'autres personnes de consulter ou d'utiliser le projet.

Merci de vous référer à mes travaux **plus récents** pour évaluer mon niveau actuel.


⚠️ Avertissement

Ce script viole très probablement les conditions d’utilisation d’equideow.com.
Je décline toute responsabilité en cas de bannissement de votre compte.


🚀 Installation

Dans votre terminal, exécutez :

pip install -r requirements.txt


Renseignez ensuite le fichier privateInfo avec votre identifiant et votre mot de passe ainsi que le lien vers l’élevage que vous voulez automatiser et le lien d’un des chevaux de cet élevage.


🛠️ Création de l’exécutable

Pour générer un fichier exécutable, utilisez la commande suivante :

python -m PyInstaller --onefile --noconsole --icon=logo.ico main.py

🌐 Navigateur

Ce script fonctionne avec le navigateur Google Chrome.
Si vous ne souhaitez pas ou ne pouvez pas installer Chrome, modifiez les lignes 10, 11 et 13 afin d’utiliser un autre navigateur.

⚙️ Compatibilité serveur

Ce script est optimisé pour les serveurs Ouranos.
Il peut fonctionner sur d’autres serveurs, mais son comportement et ses performances ne sont pas garantis.

⏰ Exécution automatique

Une fois le script transformé en exécutable, il peut être lancé automatiquement :

chaque jour via le Planificateur de tâches sous Windows

via Cron sous Linux
