likes_and_dislikes= """

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


import re
likes,dislikes = [],[]
pairs = re.split("\+-*\+-*\+\n?",likes_and_dislikes)[2:-1] #Drop the header and the tail
for p in pairs:
  like,dislike = [],[]
  for l in p.split('\n'):
    pair = l.split('|')
    if len(pair) > 1:
      # Not a blank line
      like.append(unicode(pair[1].strip(),'utf-8'))
      dislike.append(unicode(pair[2].strip(),'utf-8'))
  if len(like) > 0:
    likes.append(" ".join(like))
  if len(dislike) > 0:
    dislikes.append(" ".join(dislike))

  likeDislike = zip(likes,dislikes)
  

  # print type(u'Meritocracy')

  # print(type(likeDislike))
# return zip(likes,dislikes)
# from pprint import pprint
# print("Likes:")
# pprint(likes,indent=4)
# print ("Dislikes:")
# pprint(dislikes,indent=4)
# print ("A set of paired likes and dislikes")

# print ("A set of paired likes and dislikes")
# pprint(zip(likes,dislikes),indent=4)
print(zip(likes,dislikes))