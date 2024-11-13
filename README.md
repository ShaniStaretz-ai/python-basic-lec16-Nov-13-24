# python-basic-lec16-Nov-13-24

## subjects learned:

* lambda functions- anonymous functions - continue:
    * to random numbers from the exist list numbers:
      ```
      print("2 digits", list(filter(lambda x: random.choice([True,False], numbers)))
      ```
    * you can send a regular function name to the filter,map function (like in js)
    * you can send multiple parameters to lambda:
      ```
      sum_a_b_lm=lambda a,b:a+b
      ```
    * function sorted():
        * the default of the function is by the start of the str by 'abc'
        * you can send, to the function sorted, **the way** to sort the list:

          ```
          print("by len", sorted(words,key=lambda w:len(w))) #sort by the length of the word
          ```
        * you can add keys separated by ',':
          ```
          print("by len,abc of the word", sorted(words,key=lambda w:(len(w),w))) #sort by the length of the word and then by abc w
          ```

        * sort by even and then odd: lambda x:x%2- because the even is always 0 and then odd(always 1)-so it's always
          first 0 and then 1
        * sort by palindrom first: lambda not w:==w[::-1]- because all condition returns True(1)/False(0)=True(1)=first then False(0)
        * sort nested list by second value [["moshe",89]]: lambda name_grade:name_grade[1]
    * dictionary(hash-map): {key:value}- 
      * init:
      ```
        grades_d:dict[str,int]=dict()
        grades_d:dict[str,int]={'moshe':89,'danny':94}
        thisdict = dict(name = "John", age = 36, country = "Norway")
        ```
      * access: 
      ```
      print(grades_d['moshe'])
      print(grades_d.get('moshe'))- return  None if not exist
      print(grades_d.get('moshe',-1))- return -1 if not exist
      ```
      * add to dict: if exist will override , else will add new
        ```
        dict[key]=value
        dict['moshe']=99 
        dict.update({"color": "red"})
        dict.update({"color": "red","shani":87})
        ```
      * delete items:
        * by key
          ```
          del  dict['moshe']
          dict.pop('moshe']- returns the value
          ```
        * last item:
          ```
           last= dict.popitem()= return as tuple: (key,value)
          ```
    
## extra subjects: