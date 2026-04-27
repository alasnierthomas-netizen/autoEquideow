def choix_du_concours(race_cheval):
    if race_cheval == "Arabe" or race_cheval == "Marwari" or race_cheval == "Mustang":
        return "first.top" #Barrel racing
    elif race_cheval == "Brumby" or race_cheval == "Highland Pony" or race_cheval == "Quarter Horse" or race_cheval == "Percheron":
        return "first.top.bottom" #Cross
    elif race_cheval == "Akhal-Téké" or race_cheval == "Anglo Arabe" or race_cheval == "Appaloosa" or race_cheval == "Fjord" or race_cheval == "Lipizzan" or race_cheval == "Paint Horse" or race_cheval == "Pur Sang Anglais" or race_cheval == "Selle Français":
        return "middle.top" #Course galop
    elif race_cheval == "Arabe d'Ouranos":
        return "last.top.bottom" #CSO
    elif race_cheval == "Arabe de Troie" or race_cheval == "Haflinger" or race_cheval == "Hunter Irlandais" or race_cheval == "Pottok" or race_cheval == "Pure Race Espagnole":
        return "first.top.bottom" #Cross
    elif race_cheval == "ANE" or race_cheval == "Barbe" or race_cheval == "Connemara" or race_cheval == "Dartmoor" or race_cheval == "Donskaya" or race_cheval == "Henson" or race_cheval == "KWPN" or race_cheval == "New Forest" or race_cheval == "Shagya" or race_cheval == "Tinker" or race_cheval == "Welsh":
        return "first.top.bottom" #Cross
    elif race_cheval == "Hanovrien" or race_cheval == "Morgan" or race_cheval == "Poney de Terre-Neuve" or race_cheval == "Shetland":
        return "last.top.bottom" #CSO
    elif race_cheval == "Curly" or race_cheval == "Hackney":
        return "last.top.bottom" #Western pleasure
    elif race_cheval == "Cheval Islandais" or race_cheval == "Drum Horse" or race_cheval == "Frison" or race_cheval == "Shire" or race_cheval == "Tennessee Walker":
        return "first.top.bottom" #Cross
    elif race_cheval == "Français de Selle" or race_cheval == "Holstein" or race_cheval == "Oldenbourg" or race_cheval == "Palomino" or race_cheval == "Poney de selle Belge":
        return "last.top.bottom" #CSO
    elif race_cheval == "Knabstrup" or race_cheval == "Nokota":
        return "last.top" #Trail class
    elif race_cheval == "Lusitanien":
        return "last.top" #Dressage
    elif race_cheval == "Cheval canadien" or race_cheval == "Trakehner":
        return "first.top.bottom" #Reining
    elif race_cheval == "Finlandais" or race_cheval == "Paso Péruvien" or race_cheval == "Trotteur Américain" or race_cheval == "Trotteur Français" or race_cheval == "Trotteur d'Orlov":
        return "first.top" #Course trot
    elif race_cheval == "Criollo Argentin" or race_cheval == "Kerry Bog" or race_cheval == "Mangalarga Marchador" or race_cheval == "Quarter Pony":
        return "middle.top" #Cutting
    elif race_cheval == "Camargue":
        return "middle.top" #Course galop
    elif race_cheval == "Konik Polski":
        return "first.top.bottom" #Cross
    elif race_cheval == "Divine":
        return "first.top.bottom" #Cross
    assert False, "la race de cheval n'ai pas reconnus par le programme"


if __name__ == "__main__":
    print(choix_du_concours("Tinker"))
