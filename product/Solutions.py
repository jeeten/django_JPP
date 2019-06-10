"""


    greater_than_avg(): Use a list comprehension to return all the numbers in a list that are greater than the average of all numbers in the list.

    sort_fruit(): Sort the passed in list of dicts by the count key.

    reverse_dict(): Return a reversed dictionary so that the values are the keys and the keys are the values.

    week_start_end(): Given a datetime object, return a tuple of (start, end) where start is the Monday at 00:00:00:000000 and end is Sunday at 23:59:59:999999.

    month_last_day(): Given a datetime object, return the day of the last day in that month.

    string_parse(): Look at the text in the test. Parse the passed in text and return a list of tuples of the likes and dislikes as seen in the test. Note that I don't want the top entry since that is a header.

    palindrome_test_function(): Return a function that I can use that will accurately determine whether or not a string is a palindrome. https://en.wikipedia.org/wiki/Palindrome

    get_dynamic_classes(): For a given list of names, return a list of classes created dynamically that are named the same as the names passed in (assume names will always be valid class names). Each class should have a method on it called is_the_one() that I can call which should only return True if the class name is "Neo".


"""

class Solutions(object):

    def greater_than_avg(self, nums):
        return [x for x in nums if x > sum(nums)/len(nums)]

    def sort_fruit(self, fruit):
        import  operator
        fruit.sort(key=operator.itemgetter('count'))
        return fruit
        

    def reverse_dict(self, d):
        return {v: k for k, v in d.iteritems()}
        # pass

    def week_start_end(self, dt):
        from datetime import timedelta,datetime
        curDay = dt.weekday()
        lstDay = 6 - curDay

        fDay = dt - timedelta(days=curDay)
        lDay = dt + timedelta(days=lstDay)
        # print("=>",dt.strptime(fDay.strftime('%Y, %m, %d, 0, 0, 0, 0'),'%Y, %m, %d, %H, 0, 0, 0'))
        # print (fDay.strftime('%Y, %m, %d, 0, 0, 0, 0'),lDay.strftime('%Y, %m, %d, 23, 59, 59, 999999'))
        # print("last date {}".format(lDay))
        fdw = datetime(fDay.year, fDay.month, fDay.day, 0,0,0,0)
        ldw = datetime(lDay.year, lDay.month, lDay.day, 23,59,59,999999)

        dayT = (fdw,ldw)
        return dayT

    def month_last_day(self, dt):
        from datetime import datetime,timedelta
        next_month = datetime(year=dt.year, month=dt.month+1, day=1)
        last_day = next_month - timedelta(days=1)
        return last_day.day

        # fDay = dt - timedelta(days=curDay)
        # lDay = dt + timedelta(days=lstDay)
        # nfdt = datetime.__new__(fDay,fDay.year,month=fDay.month,day=fDay.days ,hour=0, minute=0, second=0,microsecond=0)
        # print("hey ",nfdt)
        # print lDayi

        
        #print (fDay.strftime('%Y, %m, %d, 0, 0, 0, 0'),lDay.strftime('%Y, %m, %d, 23, 59, 59, 999999'))
        #dayT = (fDay.strftime('%Y, %m, %d, 0, 0, 0, 0'),lDay.strftime('%Y, %m, %d, 23, 59, 59, 999999'))
        #return dayT


        # pass

    def string_parse(self, text):
        import re
        likes,dislikes = [],[]
        pairs = re.split("\+-*\+-*\+\n?",text)[2:-1] #Drop the header and the tail
        for p in pairs:
            like,dislike = [],[]
            for l in p.split('\n'):
                pair = l.split('|')
                if len(pair) > 1:
                    # Not a blank line
                    # arv = str("{}".format(pair[1].strip()))
                    # print("len => %s of the str %s" %(len(arv),arv))
                    
                    # like.append(re.sub(' +', '',pair[1].strip()))
                    like.append(unicode(pair[1].strip()))
                    dislike.append(unicode(pair[2].strip()))
            if len(like) > 0:
                likes.append(" ".join(like).strip())
            if len(dislike) > 0:
                dislikes.append(" ".join(dislike).strip())

        likeDislike = zip(likes,dislikes)
        
        # print(type(likeDislike))
        # print zip(likes,dislikes)[0]
        return zip(likes,dislikes)



    def palindrome_test_function(self):
        def checkString(text):
            import re
            text = re.sub('[^A-Za-z0-9]+', '', text).lower()
            if text == text[::-1]: 
                return True
            else:
                return False
        return checkString
        

    def get_dynamic_classes(self, names):
        return [type('cls', (object,),{"name":cls,"is_the_one":lambda self : self.name == "Neo"}) for cls in names]
        #pass
            

    
