x = [("Вокин", "Сергей", "Михайлович"),
     ("Трапезникова", "Анастасия", "Олеговна"),
     ("Марцех", "Вячеслав", "Александрович")]


#ef length(name):
    #return len(" ".join(name))


#name_lengths = [length(name) for name in x]
#print(name_lengths)

x.sort(key=lambda name: len(" ".join(name)))
print(x)
