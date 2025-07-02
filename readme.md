# Django E-Commerce Lernprojekt

Ein Django REST API Projekt für E-Commerce mit verschiedenen Apps für Warenkorb, Produktmanagement, Adressverwaltung und Shop-Funktionalitäten.

## 📋 Voraussetzungen

- Python 3.8 oder höher (bereits installiert)
- Git

## 📥 Download & Installation

### Option 1: Repository klonen
```bash
git clone [REPOSITORY_URL]
cd [REPOSITORY_NAME]
```

### Option 2: ZIP herunterladen
1. [Projekt als ZIP herunterladen]([DOWNLOAD_LINK])
2. ZIP-Datei entpacken
3. Terminal/CMD im Projektordner öffnen

## 🚀 Projekt einrichten (Schritt für Schritt)

### 1. Virtuelle Umgebung erstellen
```bash
python -m venv venv
```

### 2. Virtuelle Umgebung aktivieren
```bash
# Windows:
venv\Scripts\activate

# Mac/Linux:
source venv/bin/activate
```

**Wichtig**: Das Terminal sollte jetzt `(venv)` vor dem Pfad anzeigen.

### 3. Alle benötigten Pakete installieren
```bash
pip install django
pip install djangorestframework
pip install djoser
pip install drf-yasg
pip install django-cors-headers
pip install djangorestframework-simplejwt
```

### 4. Datenbank einrichten
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Admin-Benutzer erstellen
```bash
python manage.py createsuperuser
```
Folge den Anweisungen und merke dir Benutzername und Passwort!

### 6. Server starten
```bash
python manage.py runserver
```

## 🌐 Zugriff auf die Anwendung

Nach dem Start des Servers sind folgende URLs verfügbar:

- **Hauptanwendung**: http://127.0.0.1:8000/
- **Admin Interface**: http://127.0.0.1:8000/admin/
- **API Dokumentation (Swagger)**: http://127.0.0.1:8000/swagger/

## 📁 Projektstruktur

Das Projekt enthält folgende Django Apps:

- **shoppingcart** - Warenkorb-Funktionalität
- **adressmanager** - Adressverwaltung für Kunden
- **productmanager** - Verwaltung von Produkten
- **shop** - Shop-Frontend und -logik
- **cart** - Erweiterte Warenkorb-Features

## 🔧 API Testing mit Postman

### Postman installieren
1. [Postman herunterladen](https://www.postman.com/downloads/)
2. Account erstellen oder als Gast verwenden

### API-Endpunkte testen
Die wichtigsten Endpunkte für Tests:

**Authentifizierung:**
- `POST /auth/users/` - Benutzer registrieren
- `POST /auth/jwt/create/` - Login (JWT Token erhalten)
- `POST /auth/jwt/refresh/` - Token erneuern

**Allgemeine APIs:**
- `GET /api/products/` - Alle Produkte anzeigen
- `POST /api/products/` - Neues Produkt erstellen
- `GET /api/cart/` - Warenkorb anzeigen

### JWT Token in Postman verwenden
1. Login-Request senden und Token kopieren
2. In anderen Requests unter "Authorization" > "Bearer Token" einfügen

## 🛠️ Entwicklung

### Server neu starten
```bash
# Server stoppen: Ctrl+C
python manage.py runserver
```

### Neue Änderungen an Modellen
```bash
python manage.py makemigrations
python manage.py migrate
```

### Django Shell öffnen
```bash
python manage.py shell
```

### Virtuelle Umgebung deaktivieren
```bash
deactivate
```

## 🔐 Technologie-Stack

- **Django 5.0.2** - Web Framework
- **Django REST Framework** - API Framework
- **Djoser** - Benutzerauthentifizierung
- **drf-yasg** - Swagger API Dokumentation
- **django-cors-headers** - CORS Unterstützung für Frontend
- **djangorestframework-simplejwt** - JWT Token Authentifizierung
- **SQLite** - Datenbank

## ⚠️ Wichtige Hinweise

- Virtuelle Umgebung muss **immer** aktiviert sein beim Arbeiten
- Bei Fehlern: Server stoppen (Ctrl+C) und neu starten
- Admin Interface nutzen um Daten zu verwalten
- Swagger UI zeigt alle verfügbaren API-Endpunkte
- Für API-Tests Postman verwenden

## 🔧 Häufige Probleme & Lösungen

**"ModuleNotFoundError"**:
```bash
# Prüfen ob venv aktiviert ist (sollte (venv) anzeigen)
# Alle Pakete nochmal installieren:
pip install django djangorestframework djoser drf-yasg django-cors-headers djangorestframework-simplejwt
```

**"Port already in use"**:
```bash
python manage.py runserver 8001
```

**Datenbank-Probleme**:
```bash
python manage.py makemigrations
python manage.py migrate
```

**Server lädt nicht**:
- Terminal schließen, neues öffnen
- Virtuelle Umgebung neu aktivieren
- Server neu starten