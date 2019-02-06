def list_ifname_ip():
  fin = open("")
  list1 = []
  list2 = []
  list3 = []
  list4 = []
  list5 = []
  list6 = []
  list7 = []
  dict = {}
  line = fin.readline()
  words = line.strip()
  for word in words:
    list1.append(word)
  for i in range (len(list1)):
    if list1[i] == "interface":
      list2.append(list1[i+1])
    elif list1[i] == "if_name" or (list1[i+1] == "if_name" and list1[i] == "no":
      if list1[i] == "no" and list[i+1]:
        list3.append("no_name")
        list4.append("no_vlan")
        list5.append("no_ipadd")
        list5.append("no_netmask")
        elif list1[i-1] == "no" and list1[i] == "if_name":
          list3.append(list[i+1])
          list5.append(list[i+6])
          list6.append(list[i+7])
          if list1[i-1] == "management_only":
            list4.append("no_vlan")
          else:
            list4.append(list1[i-1]+list1[i-2])
  for i in range (len(list2):
    list7 = append.(list3[i])
    list7 = append.(list4[i])
    list7 = append.(list5[i])
    list7 = append.(list6[i])
    dict[list2[i]]=list7
  return dict
