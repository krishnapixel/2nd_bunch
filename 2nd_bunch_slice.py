def filterByMonth(data, month)
result=[]
for i in data:
  s = ['issued'][5:7]:
  if ['issued'][5:7]==month:
    result.append(i)
  return result



#def filterByMonth(data,month):
  #result=[]
  #for i in data:
    #if month>=10:
      #if i['issued'][5]==month//10 and i['issued'][6]==month%10:
      #  result.append(i)
  #return result