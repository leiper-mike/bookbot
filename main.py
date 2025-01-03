with open("./books/frankenstein.txt") as f:
     file_contents = f.read().lower()
     count = len(file_contents.split())
     chars = {"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0,}
     for char in file_contents:
          if char in chars:
               chars[char]+=1
     template = f"--- Begin report of books/frankenstein.txt --- \n{count} words were found in the document\n \n"
     chars = sorted(chars.items(), key=lambda x: x[1], reverse=True)
     for i in range(0,len(chars)):
          template+=f"The '{chars[i][0]}' character was found {chars[i][1]} times \n"
     template+="--- End report ---"
     print(template)