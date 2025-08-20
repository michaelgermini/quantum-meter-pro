# QuantumMeter Pro - Documentation

Ce dossier contient la documentation pour GitHub Pages du projet QuantumMeter Pro.

## 📁 Structure des fichiers

```
docs/
├── index.html              # Page d'accueil HTML
├── index.md                # Documentation principale
├── presentation.md         # Page de présentation
├── home.md                 # Page d'accueil alternative
├── _config.yml            # Configuration Jekyll
├── Gemfile                # Dépendances Ruby/Jekyll
├── assets/
│   └── README.md          # Documentation des assets
└── README.md              # Ce fichier
```

## 🚀 Déploiement

Le site GitHub Pages est automatiquement déployé via GitHub Actions à chaque push sur la branche `main`.

### URL du site
- **Production**: https://michaelgermini.github.io/quantum-meter-pro
- **Repository**: https://github.com/michaelgermini/quantum-meter-pro

## 🔧 Configuration

### Jekyll
- **Thème**: Cayman
- **Plugins**: SEO Tag, Sitemap
- **Base URL**: `/quantum-meter-pro`

### GitHub Actions
Le workflow `.github/workflows/pages.yml` gère automatiquement :
- Build Jekyll
- Déploiement sur GitHub Pages
- Mise à jour automatique

## 📝 Contenu

### Pages disponibles
1. **index.html** - Page d'accueil avec design moderne
2. **index.md** - Documentation complète du projet
3. **presentation.md** - Présentation détaillée en français
4. **home.md** - Page d'accueil alternative

### Assets
- **Logo**: `../QuantumMeter_Pro.png`
- **Favicon**: Même image que le logo
- **Styles**: CSS intégré dans index.html

## 🛠️ Développement local

Pour tester localement :

```bash
cd docs
bundle install
bundle exec jekyll serve
```

Puis ouvrir http://localhost:4000/quantum-meter-pro/

## 📊 SEO

Le site est optimisé pour le référencement avec :
- Meta tags appropriés
- Sitemap automatique
- Structure HTML sémantique
- Mots-clés pertinents

## 🔗 Liens utiles

- [GitHub Repository](https://github.com/michaelgermini/quantum-meter-pro)
- [Issues](https://github.com/michaelgermini/quantum-meter-pro/issues)
- [Documentation](https://github.com/michaelgermini/quantum-meter-pro/blob/main/README.md)
- [Email](mailto:michael@germini.info)
