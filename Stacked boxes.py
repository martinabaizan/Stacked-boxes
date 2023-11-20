#Implement a script that, given 2 integers (box_size and grid_size), displays on screen a grid of boxes using ASCII characters

box_size = 5
grid_size = 6

if box_size % 2 != 0:
  print(("+" + "-" * (box_size - 2))* grid_size + "+")
  for x in range(grid_size):
    a = 0
    b = box_size - 4
    c = int((box_size / 2) - 2)
    d = 1
    e = int((box_size / 2)-1)
    if box_size == 3:
      print(("|" + "X") * grid_size + "|")
      print(("+" + "-" * (box_size - 2)) * grid_size + "+")

    else:
      while a <= int((box_size / 2) -2) and b >= 0:
        print(("|" + (" " * a) + "\\" + (" "*b) + "/" + (" " * a)) * grid_size + "|")
        a += 1
        b -= 2

      print(("|" + " "*e + "X" + " "*e) * grid_size + "|")

      while c >= 0 and d <= int(box_size/2):
        print(("|" + (" " * c) + "/" + (" "*d) + "\\" + (" " * c)) * grid_size + "|")
        c -= 1
        d += 2
      print(("+" + "-" * (box_size - 2))* grid_size + "+")
else:
  print(("+" + "-" * (box_size - 2)) * grid_size + "+")
  for x in range(grid_size):
    a = 0
    b = box_size - 4
    c = int((box_size / 2) - 2)
    d = 0
    while a <= int((box_size / 2) - 2) and b >= 0:
      print(("|" + (" " * a) + "\\" + (" " * b) + "/" + (" " * a)) * grid_size + "|")
      a += 1
      b -= 2
    while c >= 0 and d <= int(box_size / 2):
      print(("|" + (" " * c) + "/" + (" " * d) + "\\" + (" " * c)) * grid_size + "|")
      c -= 1
      d += 2
    print(("+" + "-" * (box_size - 2)) * grid_size + "+")
