elevesNote = {
    "Nikki": 10,
    "Aurélien": 17,
    "Toni": 15,
    "Corentin": 14,
    "Maryline": 18
}

meilleurEleve = max(elevesNote, key=elevesNote.get)
print("L'élève avec la meilleure note est", meilleurEleve, "avec une note de", elevesNote[meilleurEleve])