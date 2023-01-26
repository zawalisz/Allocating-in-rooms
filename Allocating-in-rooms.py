import tkinter as tk

# Funkcja do dodawania nowych osób
def add_person():
  # otwieramy plik w trybie dopisywania
  person = person_entry.get()
  gender = gender_var.get()
  person_entry.delete(0, tk.END)
  with open("Lista_osob.txt", "a") as plik:
      # pobieramy dane od użytkownika
      plik.write(gender + person + "\n")

# Funkcja do dodawania nowych pokoi
def add_room():
  # otwieramy plik w trybie dopisywania
  room = room_entry.get()
  room_entry.delete(0, tk.END)
  room_quantity = room_quantity_entry.get()
  room_quantity_entry.delete(0, tk.END)
  with open("Lista_pokoi.txt", "a") as plik:
      # pobieramy dane od użytkownika
      plik.write(room + "--" + room_quantity + "\n")
  

# Funkcja do wczytywania osób z listy
def load_people():
  # Usunięcie tylko elementów dynamicznie tworzonych
  for widget in app.grid_slaves():
    global counter
    counter = 0
    if widget not in keep_widgets:
      widget.grid_forget()

  with open("Lista_osob.txt", "r") as plik:
    people_list = plik.read().splitlines()
    for person in people_list:
      person = person[1:]
      counter += 1

      # Funkcja do usuwania osoby
      def delete_person(current_row):
        with open("Lista_osob.txt", "r") as plik:
          people_list = plik.read().splitlines()
        del people_list[current_row-4]
        with open("Lista_osob.txt", "w") as plik:
          for person in people_list:
            plik.write(person + "\n")
        for widget in app.grid_slaves():
          if int(widget.grid_info()["row"]) == current_row:
            widget.grid_forget()
      
      # Funkcja przydzielania pokoju do osoby
      def allocate(current_row1):
        no_room = no_room_entry.get()
        no_room_label = tk.Label(text=f"{no_room}")
        no_room_label.grid(row = current_row1, column = 2, padx = 1, pady = 1)
        
      # Stworzenie nowego labela Lp
      Lp1_label = tk.Label(text=f"{counter}.")
      Lp1_label.grid(row = counter+3, column = 0, padx = 1, pady = 1)

      # Stworzenie nowego labela uczestnika
      person_label = tk.Label(text=f"{person}")
      person_label.grid(row = counter+3, column = 1, padx = 1, pady = 1)

      # Stworzenie nowego labela do przydzielenia pokoju
      no_room_label = tk.Label(text=f"{0}")
      no_room_label.grid(row = counter+3, column = 2, padx = 1, pady = 1)

      # Stworzenie nowego entry do przydzielenia pokoju
      no_room_entry = tk.Entry()
      no_room_entry.grid(row = counter+3, column = 3, padx = 1, pady = 1)

      # Stworzenie nowego przycisku Dodania nr pomieszczenia
      current_row1 = counter + 3
      room_button = tk.Button(text="Przydziel pom.", command=lambda current_row1=current_row1: allocate(current_row1))
      room_button.grid(row = counter+3, column = 4, padx = 1, pady = 1)

      # Stworzenie nowego przycisku Usuń
      current_row = counter + 3
      delete_button = tk.Button(text="Usuń", command=lambda current_row=current_row: delete_person(current_row))
      delete_button.grid(row = counter+3, column = 5, padx = 1, pady = 1)

# Funkcja do wczytywania pokoi z listy
def load_rooms():
  # Usunięcie tylko elementów dynamicznie tworzonych
  for widget in app.grid_slaves():
    global counter
    counter = 0
    if widget not in keep_widgets:
      widget.grid_forget()

  with open("Lista_pokoi.txt", "r") as plik:
    rooms_list = plik.read().splitlines()
    for room in rooms_list:
      room_name = room.split("--")[0]
      room_quantity = room.split("--")[1]
      counter += 1

      # Funkcja do usuwania pokoju
      def delete_room(current_row):
        with open("Lista_pokoi.txt", "r") as plik:
          rooms_list = plik.read().splitlines()
        del rooms_list[current_row-4]
        with open("Lista_pokoi.txt", "w") as plik:
          for room in rooms_list:
            plik.write(room + "\n")
        for widget in app.grid_slaves():
          if int(widget.grid_info()["row"]) == current_row:
            widget.grid_forget()
            
      # Stworzenie nowego labela Lp
      Lp2_label = tk.Label(text=f"{counter}.")
      Lp2_label.grid(row = counter+3, column = 7, padx = 1, pady = 1)

      # Stworzenie nowego labela nazwy pokoju
      room_label = tk.Label(text=f"{room_name}")
      room_label.grid(row = counter+3, column = 8, padx = 1, pady = 1)

      # Stworzenie nowego labela pojemności pokoju
      room_quantity_label = tk.Label(text=f"{room_quantity}")
      room_quantity_label.grid(row = counter+3, column = 9, padx = 1, pady = 1)

      # Stworzenie nowego przycisku Usuń
      current_row = counter + 3
      delete_room_button = tk.Button(text="Usuń", command=lambda current_row=current_row: delete_room(current_row))
      delete_room_button.grid(row = counter+3, column = 10, padx = 1, pady = 1)

# Zmienna do przechowywania liczby dodanych labeli
counter = 0

# Stworzenie okna aplikacji
app = tk.Tk()
app.title("Rozmieszczanie w pokojach")


# FIRST ROW

# Stworzenie labela imię i nazwizko
person_label = tk.Label(text="Imię i nazwisko:")
person_label.grid(row = 0, column = 1, padx = 1, pady = 1)

# Stworzenie labela płeć
gender_label = tk.Label(text="Płeć:")
gender_label.grid(row = 0, column = 2, columnspan = 2, padx = 1, pady = 1)

# Stworzenie labela separatora
separate1_label = tk.Label(text="|")
separate1_label.grid(row = 0, column = 6, padx = 1, pady = 1)

# Stworzenie labela numer pokoju
room_label = tk.Label(text="Numer pokoju:")
room_label.grid(row = 0, column = 8, padx = 1, pady = 1)

# Stworzenie labela pojemności pokoju
room_quantity_label = tk.Label(text="Ilość miejsc:")
room_quantity_label.grid(row = 0, column = 9, padx = 1, pady = 1)

# SECOND ROW

# ADDING PEOPLE

# Stworzenie przycisku do wczytania listy osób
wgraj_button = tk.Button(text="Wczytaj osoby", command=load_people)
wgraj_button.grid(row = 1, column = 0, padx = 1, pady = 1)

# Stworzenie pola do wprowadzania imienia i nazwiska
person_entry = tk.Entry()
person_entry.grid(row = 1, column = 1, padx = 1, pady = 1)

gender_var = tk.StringVar(value='K')

# Stworzenie radiobutton male/female
person_radiobutton_k = tk.Radiobutton(value="K", text="K", variable=gender_var)
person_radiobutton_k.grid(row = 1, column = 2, padx = 1, pady = 1)

# Stworzenie radiobutton male/female
person_radiobutton_m = tk.Radiobutton(value="M", text="M", variable=gender_var)
person_radiobutton_m.grid(row = 1, column = 3, padx = 1, pady = 1)

# Stworzenie przycisku do dodania osoby
dodaj_button = tk.Button(text="Dodaj osobę", command=add_person)
dodaj_button.grid(row = 1, column = 4, padx = 1, pady = 1)


# Stworzenie labela separatora
separate2_label = tk.Label(text="|")
separate2_label.grid(row = 1, column = 6, padx = 1, pady = 1)

# ADIING ROOMS

# Stworzenie przycisku do wczytania listy pokoi
load_rooms_button = tk.Button(text="Wczytaj pokoje", command=load_rooms)
load_rooms_button.grid(row = 1, column = 7, padx = 1, pady = 1)

# Stworzenie pola do wprowadzania nazwy pokoju
room_entry = tk.Entry()
room_entry.grid(row = 1, column = 8, padx = 1, pady = 1)

# Stworzenie pola do wprowadzania pojemnosci pokoju
room_quantity_entry = tk.Entry()
room_quantity_entry.grid(row = 1, column = 9, padx = 1, pady = 1)

# Stworzenie przycisku do dodania pokoju
add_room_button = tk.Button(text="Dodaj pokój", command=add_room)
add_room_button.grid(row = 1, column = 10, padx = 1, pady = 1)


# THIRD ROW

# Stworzenie przerwy
separate3_label = tk.Label(text="---------------------------------------------------------------------------------------")
separate3_label.grid(row = 2, column = 0, columnspan = 5, padx = 1, pady = 1)

# Stworzenie separatora
separate4_label = tk.Label(text="|")
separate4_label.grid(row = 2, column = 6, padx = 1, pady = 1)

# Stworzenie przerwy
separate5_label = tk.Label(text="---------------------------------------------------------------------------------------")
separate5_label.grid(row = 2, column = 7, columnspan = 5, padx = 1, pady = 1)


# FOURTH ROW

# Stworzenie nagłówka tabeli
tabel1_label = tk.Label(text="Lp")
tabel1_label.grid(row = 3, column = 0, padx = 1, pady = 1)
tabel2_label = tk.Label(text="Imię i nazwisko")
tabel2_label.grid(row = 3, column = 1, padx = 1, pady = 1)
tabel3_label = tk.Label(text="Przydzielony pokój")
tabel3_label.grid(row = 3, column = 2, padx = 1, pady = 1)

tabel4_label = tk.Label(text="Lp")
tabel4_label.grid(row = 3, column = 7, padx = 1, pady = 1)
tabel5_label = tk.Label(text="Numer pokoju")
tabel5_label.grid(row = 3, column = 8, padx = 1, pady = 1)
tabel6_label = tk.Label(text="Liczba miejsc")
tabel6_label.grid(row = 3, column = 9, padx = 1, pady = 1)

keep_widgets = [person_label, gender_label, room_label, room_quantity_label, wgraj_button, person_entry, dodaj_button, separate1_label, separate2_label, separate3_label, separate4_label, separate5_label, person_radiobutton_k, person_radiobutton_m, load_rooms_button, room_entry, room_quantity_entry, add_room_button, tabel1_label, tabel2_label, tabel3_label, tabel4_label, tabel5_label, tabel6_label]

# Uruchomienie pętli aplikacji
app.mainloop()