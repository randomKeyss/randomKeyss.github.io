import os

b = os.path.dirname(os.path.abspath(__file__))
monthList = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

print("update main page? (y/n)")
update_main_page = input().upper() == "Y"
print("update archives? (y/n)")
update_archives = input().upper() == "Y"
if (update_archives):
    print("which year? 'a' for all")
    year = input()
    if (year.upper() == 'A'):
        year = -1
    year = int(year)
    print("which month? 'a' for all")
    month = input()
    if (month.upper() == 'A'):
        month = -1
    month = int(month)
    print("which day? 'a' for all")
    day = input()
    if (day.upper() == 'A'):
        day = -1
    day = int(day)
print("updating...")
num_files_updated = 0

if (update_archives):
    years = [name for name in os.listdir(b + '/../stories/') if name.isdigit()] if year == -1 else [str(year)]
    months = [str(i) for i in range(1,13)] if month == -1 else [str(month)]
    days = [str(day)]
    if day == -1:
        days = []
        for i in range(31):
            day = str(i)
            if i < 10:
                day = "0" + day
            days.append(day)
    folders_to_update = []
    for i in years:
        for j in months:
            for k in days:
                path = b + '/../stories/' + str(i) + '/' + str(j) + '/' + str(k) + '/'
                if (os.path.isdir(path)):
                    stories = [name for name in os.listdir(path)]
                    for story in stories:
                        folders_to_update.append(path + story + '/')
    for folder in folders_to_update:
        story_index = open(folder + "index.html", "w", encoding = "utf-8")
        story_template = open(b + "/story_template.html", "r", encoding = "utf-8")
        story = open(folder + "story.txt","r", encoding = "utf-8")
        story_split = story.read().split("\n")
        story_template_split = story_template.read().split("<!>")
        out = ""
        for i in range(4):
            out += story_template_split[i]
            out += story_split[i]
        i += 1
        while (i < len(story_split)):
            out += "\n<br><br>\n" + story_split[i]
            i += 1
        out += story_template_split[4]
        story_index.write(out)
        num_files_updated += 1

if (update_main_page):
    most_recent_stories = []
    years = [int(name) for name in os.listdir(b + '/../stories/') if name.isdigit()]
    
    year = max(years)
    years.remove(year)
    months = [int(name) for name in os.listdir(b + '/../stories/' + str(year) + '/') if name.isdigit()]
    month = max(months)
    months.remove(month)
    days = [int(name) for name in os.listdir(b + '/../stories/' + str(year) + '/' + str(month) + '/') if name.isdigit()]
    day = max(days)
    days.remove(day)
    if (day < 10):
            day = "0" + str(day)
    stories = [name for name in os.listdir(b + '/../stories/' + str(year) + '/' + str(month) + '/' + str(day) + '/')]
    story = stories.pop()
    most_recent_stories.append(b + '/../stories/' + str(year) + '/' + str(month) + '/' + str(day) + '/' + story + '/')
    while(len(most_recent_stories) < 7):
        if (len(stories) == 0):
            if (len(days) == 0):
                if (len(months == 0)):
                    if (len(years) == 0):
                        print("not enough stories to fill main page")
                        break
                    year = max(years)
                    years.remove(year)
                    months = [int(name) for name in os.listdir(b + '/../stories/' + str(year) + '/') if name.isdigit()]
                    month = max(months)
                    months.remove(month)
                month = max(months)
                months.remove(month)
                days = [int(name) for name in os.listdir(b + '/../stories/' + str(year) + '/' + str(month) + '/') if name.isdigit()]
            day = max(days)
            days.remove(day)
            if (day < 10):
                day = "0" + str(day)
            stories = [name for name in os.listdir(b + '/../stories/' + str(year) + '/' + str(month) + '/' + str(day) + '/')]
        story = stories.pop()
        most_recent_stories.append(b + '/../stories/' + str(year) + '/' + str(month) + '/' + str(day) + '/' + story + '/')
    

    main_page = open(b + "/../index.html", "w", encoding = "utf-8")
    main_page_template = open(b + "/main_page_template.html", "r", encoding = "utf-8")
    card_template = open(b + "/card_template.html", "r", encoding = "utf-8")
    card_template_split = card_template.read().split("<!>")
    main_story = open(most_recent_stories[0] + "/story.txt","r", encoding = "utf-8")
    story = main_story.read().split("\n")
    main_page_template_split = main_page_template.read().split("<!>")
    out = ""
    for i in range(4):
        if i == 2 and story[i] == "":
                out += monthList[int(most_recent_stories[0].split("/")[-4])-1] + " " + str(int(most_recent_stories[0].split("/")[-3])) + ", " + str(int(most_recent_stories[0].split("/")[-5]))
        if i == 0:
            out += main_page_template_split[i] + "<a href = '" + "/".join(most_recent_stories[0].split("/")[-6:]) + "index.html" + "'>" + story[i] + "</a>"
        else:
            out += main_page_template_split[i] + story[i]
    i += 1
    while(i < len(story)):
        out += "\n<br><br>\n" + story[i]
        i += 1
    out += main_page_template_split[4]


    monthList = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    years = [int(name) for name in os.listdir(b + '/../stories/') if name.isdigit()]
    years.sort(reverse = True)
    for year in years:
        months = [int(name) for name in os.listdir(b + '/../stories/' + str(year) + '/') if name.isdigit()]
        months.sort(reverse = True)
        for month in months:
            out += '<li><a href="archive.html#' + monthList[month-1] + str(year) + '">' + monthList[month-1] + ' ' + str(year) + '</a></li>'
    out += main_page_template_split[5]



    cols = ["",""]
    for i in range(1, len(most_recent_stories)):
        story_html = ""
        this_story = open(most_recent_stories[i] + "/story.txt","r", encoding = "utf-8")
        story = this_story.read().split("\n")
        for j in range(4):
            if j == 2 and story[j] == "":
                story_html += monthList[int(most_recent_stories[i].split("/")[-4])-1] + " " + str(int(most_recent_stories[i].split("/")[-3])) + ", " + str(int(most_recent_stories[i].split("/")[-5]))
            story_html += card_template_split[j]
            if j == 0:
                story_html += "<a href = '" + "/".join(most_recent_stories[i].split("/")[-6:]) + "index.html" + "'>" + story[j] + "</a>"
            else:
                story_html += story[j]
        j += 1
        while(j < len(story)):
            story_html += "\n<br><br>\n" + story[j]
            j += 1
        story_html += card_template_split[4]
        colInd = (i-1)%2
        cols[colInd] += story_html
    out += cols[0]
    out += main_page_template_split[6]
    out += cols[1]
    out += main_page_template_split[7]
    main_page.write(out)
    num_files_updated += 1



    



    archive_page = open(b + "/../archive.html", "w", encoding = "utf-8")
    archive_page_template = open(b + "/archive_template.html", "r", encoding = "utf-8")
    archive_page_template_split = archive_page_template.read().split("<!>")
    monthList = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    years = [int(name) for name in os.listdir(b + '/../stories/') if name.isdigit()]
    years.sort(reverse = True)
    o1 = ""
    o2 = ""
    for year in years:
        months = [int(name) for name in os.listdir(b + '/../stories/' + str(year) + '/') if name.isdigit()]
        months.sort(reverse = True)
        for month in months:
            o1 += '<h1 name="' + monthList[month-1] + str(year) +'">' + monthList[month-1] + ' ' + str(year) + '</h1>\n<br>'
            o2 += '<a href="#' + monthList[month-1] + str(year) + '">' + monthList[month-1] + ' ' + str(year) + '</a>'
            days = [name for name in os.listdir(b + '/../stories/' + str(year) + '/' + str(month) + '/') if name.isdigit()]
            days.reverse()
            for day in days:
                stories = [name for name in os.listdir(b + '/../stories/' + str(year) + '/' + str(month) + '/' + str(day) + '/')]
                for story in stories:
                    link = b + '/../stories/' + str(year) + '/' + str(month) + '/' + str(day) + '/' + story + '/'
                    txt_file = open(link + "story.txt", "r", encoding = "utf-8")
                    title = txt_file.read().split("\n")[0]
                    o1 += '<ul><a href="../nightly_illini/stories/' + str(year) + '/' + str(month) + '/' + str(day) + '/' + story + '/index.html">' + title + '</a></ul>'
    out = archive_page_template_split[0] + o1 + archive_page_template_split[1] + o2 + archive_page_template_split[2]
    archive_page.write(out)
    num_files_updated += 1

print("updated " + str(num_files_updated) + " file" + ("" if num_files_updated == 1 else "s"))