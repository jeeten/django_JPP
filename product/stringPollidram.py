import Solutions


obj = Solutions.Solutions()
# obj.palindrome_test_function()

test_function = obj.palindrome_test_function()
res = test_function('HYH')
names = ['TheOracle', 'Neo', 'Trinity', 'Morpheous']
dynamic_classes = obj.get_dynamic_classes(names)
klasses = {}
for idx, name in enumerate(names):
    klasses[name] = dynamic_classes[idx]()

# print(klasses['TheOracle'].is_the_one())
# print(klasses['Neo'].is_the_one())
# print(klasses['Trinity'].is_the_one())
# print(klasses['Morpheous'].is_the_one())

def test_month_last_day():
        from datetime import datetime

        
        print(obj.month_last_day(datetime(2013, 8, 4))) #31)
        print(obj.month_last_day(datetime(2012, 2, 1))) #29)
        print(obj.month_last_day(datetime(2013, 2, 1))) #28)
        print(obj.month_last_day(datetime(2013, 10, 1))) #31)

# test_month_last_day()

def test_week_start_end():
    from datetime import datetime
    answer = obj.week_start_end(datetime(2013, 8, 15, 12, 0, 0))
    print(answer, (datetime(2013, 8, 12, 0, 0, 0, 0), datetime(2013, 8, 18, 23, 59, 59, 999999)))
    answer = obj.week_start_end(datetime(2013, 8, 5, 12, 0, 0))
    # print(answer, (datetime(2013, 8, 5, 0, 0, 0, 0), datetime(2013, 8, 11, 23, 59, 59, 999999)))

# test_month_last_day()
def test_string_parse():
        developer_likes_and_dislikes = """

+------------------------------------+-----------------------------------+
| likes                              | dislikes                          |
+------------------------------------+-----------------------------------+
| Meritocracy                        | Favoritism, ass-kissing, politics |
+------------------------------------+-----------------------------------+
| Healthy debates and collaboration  | Ego-driven rhetoric, drama and FUD|
|                                    | to get one's way                  |
+------------------------------------+-----------------------------------+
| Autonomy given by confident leaders| Micro-management by insecure      |
| capable of attracting top-tier     | managers compensating for a weak, |
| talent                             | immature team                     |
+------------------------------------+-----------------------------------+
| Fluid communication, brief, ad-hoc | Formal meetings, endless debate   |
| discussions, white-boarding, and   |                                   |
| quick but informed decisions       |                                   |
+------------------------------------+-----------------------------------+
| Where else can I help out?         | I'm blocked by..., I only know how|
|                                    | to...                             |
+------------------------------------+-----------------------------------+
| Getting things done.               | Contrived company culture         |
+------------------------------------+-----------------------------------+
| Clever and disruptive business     |                                   |
| ideas that solve real and immediate|                                   |
| needs in a marketplace             |                                   |
+------------------------------------+-----------------------------------+
| Software and system abstractions   | Hard-coding, brute-force          |
+------------------------------------+-----------------------------------+
| Frameworks and best-practices      | Hermetic code-base                |
+------------------------------------+-----------------------------------+
| Best tool for the job              | One size fits all                 |
+------------------------------------+-----------------------------------+
| Simple design                      | Over-engineering                  |
+------------------------------------+-----------------------------------+
| Leveraging open-source             | Re-inventing the wheel            |
+------------------------------------+-----------------------------------+
| Practical solutions to business    | Let's do this or use that because |
| core competency                    | it's new and cool                 |
+------------------------------------+-----------------------------------+
| Building solutions to current      | Over-emphasizing "nice-to-haves"  |
| business needs and customer demand | and conjecture                    |
+------------------------------------+-----------------------------------+

"""
        answer = obj.string_parse(developer_likes_and_dislikes)
        print answer
        
        chkAnswer = [(u'Meritocracy', u'Favoritism, ass-kissing, politics'),]
        print chkAnswer

test_string_parse()
