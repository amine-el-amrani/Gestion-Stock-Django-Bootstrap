#!/bin/bash

# Fonction pour installer PostgreSQL et configurer la base de données
install_postgresql () {
    # Installe PostgreSQL (pour Ubuntu)
    sudo apt-get install -y postgresql postgresql-contrib libpq-dev || true

    # Démarre le service PostgreSQL
    sudo systemctl start postgresql.service 2>/dev/null || true
    sudo /etc/init.d/postgresql start 2>/dev/null || true

    echo "[+] Configuration de la base de données PostgreSQL"

    export POSTGRES_USER="efrei"
    export POSTGRES_PASSWORD="efrei"
    export POSTGRES_DB="efrei"

    # Créer la base de données
    echo "Création de la base de données $POSTGRES_DB"
    sudo -u postgres psql -c "CREATE USER $POSTGRES_USER WITH PASSWORD '$POSTGRES_PASSWORD';" || true
    sudo -u postgres psql -c "GRANT postgres TO $POSTGRES_USER;" || true
    sudo -u postgres psql -c "CREATE DATABASE $POSTGRES_DB;"
    sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE $POSTGRES_DB TO $POSTGRES_USER;"

    # Autoriser l'utilisateur à créer des bases de données (optionnel)
    sudo -u postgres psql -c "ALTER USER $USER CREATEDB;"
}

# Appeler la fonction d'installation de PostgreSQL
install_postgresql

# Attendre que PostgreSQL soit prêt
sleep 5

# Lancer le serveur Django
exec "$@"
