---
DateStarted: 2024-03-17
DateToFinish: 2024-09-01
sr-due: 2024-05-28
sr-interval: 56
sr-ease: 286
---
For this period I'll follow the  General, specific and operative objectives strategy. I'll divide the period in two. From march to July (une included as there are a few exams taking place in those dates) and July to September (the summer season). To keep track of the set objectives the [dailyNote](../99%20-%20Meta/1.%20Templates/dailyNote.md) template will be updated with all the task extracted in the operative objectives. 
This note will be reviewed periodically to modify any objectives and check that the chosen strategy is working. #review 
# General objectives: 
## 1. Use of RRSS and online learning resources
With a great use of social media comes great responsibility. I can really easily go towards a misusage of it all. I want to focus on using it for longer content. I recently discovered during the t3chfest that all CS media is on twitter. If I start using twitter or instagram I would like it to be focused on the content I have chosen to see. 
- [ ] DONE?
## 2. Sleep / Wake up in time
Sleeping has always troubled me. Now with the afternoon uni courses it has all gotten even worse. This is one of the main objectives I want to work on, controlling and learning about sleep so that I can use it as a power instead of it controlling me. 
- [ ] DONE?
## 3.Scouts: 
During this period there are three main focuses. Camps, Documentation and the  MTL course. Working on more courses would be a nice thing to do. However It doesn't seem realistic. 
- [ ] DONE?
## 4.Uni & Learning: 
I've been struggling with university since I started with it. I think it's mostly because of a lack of effort from my part. At the start of this year I noticed a big change when I  focused on going to all clases. Even more with the friendships  and connections I started to create. What I'm lacking is success, seeing my efforts create something I'm proud of. 
- [ ] DONE?

# Specific&Operative (March - June)

The main focus for this time is to create a routine. All objectives are mostly based on things to do daily or every week. This is because I haven't been following this methods and I still need to build up this routine. Once the routine is build everything goes detrás. 

---
## 1.1 Use Instagram and Twitter as learning spaces

### 1.1.1 Using the search tab to search (content just to fill some gap time)(even then better to just read)
- [ ] 
### 1.1.2 Read 30 min per day
I'm not using reading as a whole general objective because even though I think it is of vital importance in my life. Right now learning h0w to manage the resources I have to learn also contains managing RRSS and others. 
- [ ] 


## 1.2 Control the time usage of RRSS

### 1.2.1 Maintain daily RRSS usage under 1h 

- [ ] 


## 1.3 Control the situational usage of RRSS
### 1.3.1 Tener un propósito antes de entrar en RRSS
Keeping the time at the home tab as a previous objective reflects already helps. However there are many times when I don't choose to take out my phone. I just do it by instinct.  By thinking of what to use the RRSS before actually opening this stops. Another good thought to have at this moment is how long am I going to stay with the RRSS. Many times I won't be able to stop and time flies by. 
- [ ] 

---
## 2.1 State the reasons for sleeping schedule
It's really hard to do anything just with pure willforce. By stating why I should go to sleep or wake up earlier and really thinking about the benefits I can have a better reason then to awake up.
Reading about sleep and learning all of the reasons I will really benefit is useful, however I don't think I will have time for it during this semester. 
### 2.1.1 Plan the next day before going to bed. 
Enfasis on planing the next morning and objectives that will be checked out by waking up at that time. 
- [ ] 


## 2.2 Create a routine around sleep. 
### 2.2.1 Do 30 min of daily sport/movement
- [ ] 
### 2.2.3 Don't use RRSS after bedtime - read
- [ ] 
--- 

## 3.1 Mantener responsabilidades dentro de secretaría
### 3.1.1 Pasar las cuotas mensualmente 
- [ ] 
### 3.1.2 Recoger documentación de Madrid cada dos semanas
- [ ] 
## 3.2 Aumentar responsabilidades de secretaría antes de campamentos y acampadas. 
### 3.2.1 Darle la tabarra a pi para que me vaya contando cositas e ir pudiendo enterarme de las cosas
- [ ] 
---
## 4.1 Create a sense of community inside the university. Be there. 
### 4.1.1 Go to university all days during class hours
Even if I'm not in class, this means I'm near the community, I interact with them and create a sense of community. 
- [ ] 
### 4.1.2 Do at least two nights out with the uni group 
- [ ] 
## 4.2 Obtain an average higher than 6
Better to achieve it with a higher notes than not being able to because I asked to much of myself
### 4.2.1 Daily use of active recall (space repetition) in obsidian
- [ ] 

## 4.3 Focus on first year courses
### 4.3.1 On busy weeks, prioritise Calculus, Discrete and Logic
# Objective tracking:

```dataview
TABLE WITHOUT ID 
key as Tasks, 
length(rows) AS Total,
length(filter(rows.tasks, (r) => r.completed)) AS Completed


FROM "01.Areas/0.DailyNote"
FLATTEN file.tasks as tasks 
GROUP BY tasks.text
SORT length(rows) DESC

