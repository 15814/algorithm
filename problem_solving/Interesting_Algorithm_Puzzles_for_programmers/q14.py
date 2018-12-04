
def q14(countries:list):
  for i in range(len(countries)):
    countries[i] = countries[i].lower()
  print(countries)
  maxcount = -1

  dictionary = {}
  for i in range(ord('a'),ord('z')+1):
    key = chr(i)
    dictionary[key] = []
  for country in countries:
    dictionary[country[0]].append(country)

  for country in countries:
    count = []
    history = []
    jielong(country,dictionary,history=history, results=count)
    count.sort()
    if count and count[-1] > maxcount:
      maxcount = count

  return maxcount

def jielong(start_country, dictionary, count=0, history=[], results = []):

  key = start_country[-1]

  if key not in dictionary:
    results.append(count)
    return
  for next_country in dictionary[key]:
    if next_country not in history:
      jielong(next_country,dictionary,count+1,history.append(next_country),results)

  return











if __name__ == '__main__':
  countries = [ "Australia", "Iran", "Japan", "South Korea", "Algeria", "Cameroon", "Ghana", "Ivory Coast", "Nigeria", "Costa Rica", "Honduras", "Mexico", "United States", "Argentina", "Brazil", "Chile", "Colombia", "Ecuador", "Uruguay", "Belgium", "Bosnia and Herzegovina", "Croatia", "England", "France", "Germany", "Greece", "Italy", "Netherlands", "Portugal", "Russia", "Spain", "Switzerland"]
  countries2 = ["Brazil","Cameroon","Chile","Greece","Uruguay","Italy","France", "Bosnia and Herzegovina", "Germany", "USA", "Russia", "Croatia", "Spain", "Australia", "Cote d'lvoire", "Costa Rica", "Switzerland", "Honduras", "Iran", "Portugal", "Belgium", "Korea Republic", "Mexico", "Netherlands", "Colombia", "Japan", "England", "Ecuador", "Argentina", "Nigeria", "Ghana", "Algeria"]
  print(len(countries2))
  q14(countries2)
