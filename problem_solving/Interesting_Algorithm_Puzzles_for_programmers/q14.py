
def q14(countries:list):
  for i in range(len(countries)):
    countries[i] = countries[i].lower()
  # print(countries)
  maxcount = -1

  dictionary = {}
  for i in range(ord('a'),ord('z')+1):
    key = chr(i)
    dictionary[key] = []
  for country in countries:
    dictionary[country[0]].append(country)

  # print(dictionary)

  for country in countries:
    results = []
    history = []
    history.append(country)
    jielong(country,dictionary,history, results)
    if results:
      print('results: ',results)

    results.sort()
    if results and results[-1] > maxcount:
      maxcount = results[-1]

  print('maxcount: ',maxcount)
  return maxcount

def jielong(start_country, dictionary, history, results):

  key = start_country[-1]
  lst = dictionary[key]
  if not lst:
    results.append(len(history))
    if history:
      print('history: ',history)
    return
  for next_country in lst:
    if not history or next_country not in history:
      history.append(next_country)
      jielong(next_country,dictionary,history,results)
      del history[-1]
  return











if __name__ == '__main__':
  countries = [ "Australia", "Iran", "Japan", "South Korea", "Algeria", "Cameroon", "Ghana", "Ivory Coast", "Nigeria", "Costa Rica", "Honduras", "Mexico", "United States", "Argentina", "Brazil", "Chile", "Colombia", "Ecuador", "Uruguay", "Belgium", "Bosnia and Herzegovina", "Croatia", "England", "France", "Germany", "Greece", "Italy", "Netherlands", "Portugal", "Russia", "Spain", "Switzerland"]
  countries2 = ["Brazil","Cameroon","Chile","Greece","Uruguay","Italy","France", "Bosnia and Herzegovina", "Germany", "USA", "Russia", "Croatia", "Spain", "Australia", "Cote d'lvoire", "Costa Rica", "Switzerland", "Honduras", "Iran", "Portugal", "Belgium", "Korea Republic", "Mexico", "Netherlands", "Colombia", "Japan", "England", "Ecuador", "Argentina", "Nigeria", "Ghana", "Algeria"]
  print(len(countries2))
  q14(countries2)
