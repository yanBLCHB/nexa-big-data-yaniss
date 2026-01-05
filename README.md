#Arborescence du projet

 nexa-big-data-yaniss/
├── script/
│   └── getapi.py
├── data/
│   └── raw/ 
        └── meteo_20260105_150408.json
├── README.md



# Commandes – Lancer le script getapi.py

## 1. Cloner le dépôt
```bash
git clone https://github.com/yanBLCHB/nexa-big-data-yaniss.git
```

## 2. Se placer dans le dossier du projet
```bash
cd nexa-big-data-yaniss
```

## 3. Aller dans le dossier du script
```bash
cd script
```

## 4. Installer les dépendances Python
```bash
pip install requests
```

ou

```bash
pip3 install requests
```

## 5. Lancer le script getapi.py
```bash
python getapi.py
```

ou

```bash
python3 getapi.py
```

## 6. Vérifier les fichiers générés
```bash
cd ..
ls data/raw
```

