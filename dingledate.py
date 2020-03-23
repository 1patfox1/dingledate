

#!/usr/bin/python

"""convert the date to an encoded date using common words"""

import datetime

adjs="""lonely
big
old
wise
boring
scary
cloned
dynamic
hot
spicy
stable
good
robust
focused
stinky
bitter
wide
friendly
fit
ugly
tall
clean
posh
tiny
slow
nice
cute
curious
great
enhanced
cold
lucky
mild
weak
mad
fast
"""

colors="""coral
green
olive
maroon
fuscia
indigo
turquoise
puce
wheat
silver
red
purple
ivory
orange
azure
gray
crimson
white
khaki
violet
aquamarine
lime
mauv
goldenrod
teal
yellow
magenta
pink
black
blue
cyan
"""
animals="""gecko
wolf
cow
dog
otter
owl
crab
fox
llama
hyena
lion
mouse
seal
bear
bat
cat
pig
puma
rabbit
huron
dove
hare
gull
ox
duck
whale
rat
tiger
eagle
moose
deer
"""
nouns="""lot
party
mother
home
house
cola
money
country
problem
name
kind
room
idea
member
education
car
girl
community
reason
system
teacher
man
woman
game
thing
study
number
book
state
case
law
eye
child
part
air
issue
change
time
research
way
area
company
president
morning
family
group
question
hand
history
level
force
story
end
school
fact
beer
city
government
student
people
point
water
door
war
parent
result
fence
face
person
power
body
guy
kid
work
business
program
information
place
line
health
art
back
others
world
side
moment
life
job
word
service
hour
father
friend
right
head
week
team
minute
office
night
"""
def codeyear(year):
    ycount=0
    ymap = {}
    for i in nouns.splitlines():
        if ycount >=1 and ycount <=9:
            istr="0"+str(ycount)
        else:
            istr=str(ycount)
        ymap[istr]=i
        ycount=ycount+1
    return ymap[year]

def codedaya(month):
    ycount=1
    ymap = {}
    for i in animals.splitlines():
        if ycount >=1 and ycount <=9:
            istr="0"+str(ycount)
        else:
            istr=str(ycount)
        ymap[istr]=i
        ycount=ycount+1
    return ymap[month]

def codedayc(month):
    ycount=1
    ymap = {}
    for i in colors.splitlines():
        if ycount >=1 and ycount <=9:
            istr="0"+str(ycount)
        else:
            istr=str(ycount)
        ymap[istr]=i
        ycount=ycount+1
    return ymap[month]

def codemonth(zmonth,zoption=1):
    icount=1
    mmap = {}
    for i in adjs.splitlines():
        if icount >=1 and icount <=9:
            istr="0"+str(icount)
        else:
            istr=str(icount)
        mmap[istr]=i
        icount=icount+1
    returnpointer=(int(zoption)-1)*12+int(zmonth)
    if returnpointer >=1 and returnpointer <=9:
        rstr="0"+str(returnpointer)
    else:
        rstr=str(returnpointer)
    return mmap[rstr]

def dingledate(thedate):
    theyear=thedate.strftime("%y")
    themonth=thedate.strftime("%m")
    theday=thedate.strftime("%d")
    dinglemonth1=codemonth(themonth)
    dinglemonth2=codemonth(themonth,zoption=2)
    dinglemonth3=codemonth(themonth,zoption=3)
    dingleyear=codeyear(theyear)
    dingledaya = codedaya(theday)
    dingledayc = codedayc(theday)
    dingle={'year': dingleyear, 'month':dinglemonth1, 'day': dingledaya, 'month2': dinglemonth2, 'month3': dinglemonth3, 'day2': dingledayc}
    return(dingle)

DDEBUG = False
def main():

  if DDEBUG: print("dingledate:\n")
  mydate=datetime.date.today()
  dingle = dingledate(mydate)
  if DDEBUG: print(dingle)
  print("%s-%s-%s" % (dingle['year'],dingle['month'],dingle['day']))
  olddate=datetime.datetime(2020,1,30)
  dingle = dingledate(olddate)
  if DDEBUG: print(dingle)
  if DDEBUG: print("%s-%s-%s" % (dingle['year'],dingle['month'],dingle['day']))
  olderdate=datetime.datetime(2019,12,31)
  dingle = dingledate(olderdate)
  if DDEBUG: print(dingle)
  if DDEBUG: print("%s-%s-%s" % (dingle['year'],dingle['month'],dingle['day']))
  futuredate=datetime.datetime(2040,7,20)
  dingle = dingledate(futuredate)
  if DDEBUG: print(dingle)
  if DDEBUG: print("%s-%s-%s" % (dingle['year'],dingle['month'],dingle['day']))

if __name__== "__main__":
  main()

