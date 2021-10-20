sampleDict = { 
   "class":{ 
      "student":{ 
         "name":"Mike",
         "marks":{ 
            "physics":70,
            "history":80
         }
      }
   }
}
print(sampleDict["class"]['student']['marks']['history'])




'''x=sampleDict.get("class")
y=x.get("student")
z=y.get("marks")
a=z.get("history")
print(a)'''