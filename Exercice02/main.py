students = {
    'Alice': {
         'Mathematiques': 90,
         'Francais': 80,
         'Histoire': 95
    },
    'Bob': {
         'Mathematiques': 75,
         'Francais': 85,
         'Histoire': 70
    },
     'Charlie': {
         'Mathematiques': 88,
         'Francais': 92,
         'Histoire': 78
     }
}

student = input("Entrez le nom de l’étudiant : ")

print(f"Nom de l'étudiant: {student}")

try:
     total_grade = 0
     nb_grade = 0
     for subject, grade in students[student].items():
          print (f"{subject}: {grade}")
          total_grade = total_grade + grade
          nb_grade = nb_grade +1

     avg = total_grade/nb_grade

     print(f"La moyenne des notes de {student} est : {avg:.2f}")


except KeyError:
     print(f"L'étudiant {student} n'existe pas dans la liste.")

