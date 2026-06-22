# Select_and_Copy
English version of README below

Une application légère en Python permettant de copier automatiquement des fichiers sélectionnés à partir d’un fichier CSV.

Développée avec **Tkinter**, cette application a été créée pour simplifier la gestion de photos sans utiliser Lightroom ou d’autres logiciels de gestion d’images.

---

## Objectif

Ce projet a été conçu pour résoudre un problème concret : trier manuellement de grandes quantités de photos (500+) afin de retrouver les fichiers sélectionnés par un client et les copier dans un dossier séparé.

Avant de découvrir des outils comme Lightroom, ce script servait de solution personnelle pour accélérer l’organisation des fichiers.

---

## Fonctionnalités

- Chargement d’un fichier CSV contenant les noms de fichiers sélectionnés
- Choix du dossier source (images originales)
- Choix du dossier de destination
- Correspondance automatique des noms de fichiers (sans extension)
- Copie des fichiers correspondants vers le dossier cible
- Interface graphique simple avec Tkinter

---

## Fonctionnement

1. L’utilisateur sélectionne :
   - Le dossier source
   - Le fichier CSV
   - Le dossier de destination

2. Le programme :
   - Lit le CSV et extrait les noms dans la colonne `Name`
   - Analyse le dossier source
   - Compare les noms de fichiers (sans extension)
   - Copie les fichiers correspondants dans le dossier de destination

---

## Technologies utilisées

- Python
- Tkinter (interface graphique)
- Module csv
- shutil
- os

---

## Remarque

Ce projet a été développé avant le début de ma formation technique et reflète une première approche de l’automatisation de tâches répétitives de gestion de fichiers.


ENGLISH VERSION
# Select_and_Copy

A lightweight Python desktop application that automatically copies selected image files based on CSV input.

Built with **Tkinter**, this tool was created to simplify photo selection workflows without using Lightroom or other photo management software.

---

## Purpose

This application was created to solve a practical workflow issue: manually sorting through large photo sets (500+ images) to find client-selected filenames and copy them into a separate folder.

Before discovering tools like Lightroom, this script was designed as a personal solution for faster file organization.

---

## Features

- Load a CSV file containing selected filenames
- Choose a source folder (original images)
- Choose a destination folder (output)
- Automatically matches filenames (ignoring file extensions)
- Copies matching files to the destination folder
- Simple graphical interface using Tkinter

---

## How it works

1. The user selects:
   - Source directory
   - CSV file
   - Destination directory

2. The program:
   - Reads the CSV and extracts filenames from the `Name` column
   - Scans the source folder
   - Matches filenames (without extensions)
   - Copies matching files into the destination folder

---

## Tech Stack

- Python
- Tkinter (GUI)
- csv module
- shutil
- os

---

## Notes

This project was developed before starting formal technical studies and reflects an early attempt at automating repetitive file management tasks.
