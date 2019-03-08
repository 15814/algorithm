
def bubble_sort(elements: list) -> list:
  length = len(elements)
  for i in range(length):
    swap = False
    for j in range(i+1,length):
      if elements[i] > elements[j]:
        elements[i], elements[j] = elements[j], elements[i]
        swap = True
    if not swap:
      break
  return elements


  
