@echo off

REM Définit la page de code UTF-8
chcp 65001

REM Vérifier si les dépendances sont déjà installées
python -c "import pkgutil" || (
    echo Installation des dépendances...
    python -m pip install -r requirements.txt --user
    echo Installation terminée.
)

REM Exécuter le script Flask
echo Démarrage de l'application...
python main.py


pause