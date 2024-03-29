from genericpath import isdir
import os

b = os.path.dirname(os.path.abspath(__file__))
monthList = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

print("update main page? (y/n)")
update_main_page = input().upper() == "Y"
print("update pages? (y/n)")
update_pages = input().upper() == "Y"
print("update archives? (y/n)")
update_archives = input().upper() == "Y"
print("updating...")
num_files_updated = 0

MONTHSLIST = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
def story_to_card(story_path, isPage = False):
    story_html = ""
    this_story = open(story_path + "/story.txt","r", encoding = "utf-8")
    card_template = open(b + "/card_template.html", "r", encoding = "utf-8")
    card_template_split = card_template.read().split("<!>")
    story = this_story.read().split("\n")
    for j in range(4):
        if j == 2 and story[j] == "":
            story_html += MONTHSLIST[int(story_path.split("/")[-4])-1] + " " + str(int(story_path.split("/")[-3])) + ", " + str(int(story_path.split("/")[-5]))
        story_html += card_template_split[j]
        if j == 0:
            if isPage:
                story_html += "<a href = '../../" + "/".join(story_path.split("/")[-6:]) + "index.html" + "'>" + story[j] + "</a>"
            else:
                story_html += "<a href = '" + "/".join(story_path.split("/")[-6:]) + "index.html" + "'>" + story[j] + "</a>"
        else:
            story_html += story[j]
    j += 1
    while(j < len(story)):
        story_html += "\n<br><br>\n" + story[j]
        j += 1
    story_html += card_template_split[4]
    return story_html
def get_all_pages():
    all_pages_in_order = []
    years = [int(name) for name in os.listdir(b + '/../stories/') if name.isdigit()]
    years.sort()
    for year in years:
        months = [int(name) for name in os.listdir(b + '/../stories/' + str(year) + '/') if name.isdigit()]
        months.sort()
        for month in months:
            days = [int(name) for name in os.listdir(b + '/../stories/' + str(year) + '/' + str(month) + '/') if name.isdigit()]
            days.sort()
            for day in days:
                if (day < 10):
                    day = "0" + str(day)
                stories = [name for name in os.listdir(b + '/../stories/' + str(year) + '/' + str(month) + '/' + str(day) + '/')]
                stories.sort(reverse=True)
                for story in stories:
                    story_folder_link = b + '/../stories/' + str(year) + '/' + str(month) + '/' + str(day) + '/' + story + '/'
                    readable_day = str(int(day))
                    href_link = 'stories/' + str(year) + '/' + str(month) + '/' + str(day) + '/' + story + '/' + 'index.html'
                    story_file = open(story_folder_link + "story.txt","r", encoding = "utf-8")
                    story_data = story_file.read().split("\n")
                    title = story_data[0]
                    date = story_data[1]
                    if (date == ""):
                        date = monthList[month-1] + " " + readable_day + ", " + str(year)
                    author = story_data[2]
                    contents = story_data[3:]
                    story_card = story_to_card(story_folder_link)
                    page_story_card = story_to_card(story_folder_link, True)
                    out = [(href_link, story_folder_link),
                            (title, date, author),
                            contents,
                            story_card,
                            page_story_card]
                    all_pages_in_order.append(out)
                    story_file.close()
    return all_pages_in_order
ALL_PAGES = get_all_pages() #[(href_link, story_folder_link),
                            #(title, date, author),
                            #contents,
                            #story_card,
                            #page_story_card]




if (update_archives):
    story_template = open(b + "/story_template.html", "r", encoding = "utf-8")
    story_template_split = story_template.read().split("<!>")
    for i,page in enumerate(ALL_PAGES):
        links, metadata, contents, story_card, page_card = page
        title, date, author = metadata
        story_index = open(links[1] + "index.html", "w", encoding = "utf-8")
        out = story_template_split[0] + title + story_template_split[1] + date + story_template_split[2] + author + story_template_split[3]
        for j in range(len(contents)):
            paragraph = contents[j]
            beginning = "" if j == 0 else "\n<br><br>\n"
            out += beginning + paragraph
        out += story_template_split[4]
        out += ALL_PAGES[0][0][0]
        out += story_template_split[5]
        out += ALL_PAGES[max(i-1,0)][0][0]
        out += story_template_split[6]
        out += ALL_PAGES[min(len(ALL_PAGES)-1,i+1)][0][0]
        out += story_template_split[7]
        out += ALL_PAGES[-1][0][0]
        out += story_template_split[8]
        story_index.write(out)
        num_files_updated += 1
if (update_pages):
    page_template = open(b + "/old_page_template.html", "r", encoding = "utf-8")
    page_template_split = page_template.read().split("<!>")
    card_template = open(b + "/card_template.html", "r", encoding = "utf-8")
    card_template_split = card_template.read().split("<!>")
    for i in range(0,len(ALL_PAGES)-14,7):
        if(i+1 >= len(ALL_PAGES) - 2):
            break
        page_num = i//7 + 1
        page_path = b + "/../page/" + str(page_num) + "/"
        if (not os.path.isdir(page_path)):
            os.mkdir(page_path)
        page_index = open(page_path + "/index.html", "w", encoding = "utf-8")
        out = page_template_split[0] + "../../index.css" + page_template_split[1]
        single_col = ""
        cols = ["",""]
        for j in range(6,-1,-1):
            story_html = ALL_PAGES[i + j][4]
            colInd = j % 2
            cols[colInd] += story_html
            single_col += story_html
        out += single_col
        out += page_template_split[2]
        out += cols[0]
        out += page_template_split[3]
        out += cols[1]
        out += page_template_split[4]
        out += str(max(page_num - 1,1))
        out += page_template_split[5]
        if page_num >= len(ALL_PAGES)//7 - 1:
            out += ".."
        else:
            out += str(page_num + 1)
        out += page_template_split[6]
        page_index.write(out)
        num_files_updated += 1
    all_pages = open(b + "/../all_stories.html", "w", encoding = "utf-8")
    out = page_template_split[0] + "index.css" + page_template_split[1]
    single_col = ""
    cols = ["",""]
    for i in range(len(ALL_PAGES)-1,-1,-1):
        story_html = ALL_PAGES[i][3]
        colInd = i % 2
        cols[colInd] += story_html
        single_col += story_html
    out += single_col
    out += page_template_split[2]
    out += cols[1]
    out += page_template_split[3]
    out += cols[0]
    out += page_template_split[4]
    out += str(max(page_num - 1,1))
    out += page_template_split[5]
    if page_num >= len(ALL_PAGES)//7 - 1:
        out += ".."
    else:
        out += str(page_num + 1)
    out += page_template_split[6]
    all_pages.write(out)
    num_files_updated += 1


        
if (update_main_page):
    main_page = open(b + "/../index.html", "w", encoding = "utf-8")
    main_page_template = open(b + "/main_page_template.html", "r", encoding = "utf-8")
    main_page_template_split = main_page_template.read().split("<!>")
    card_template = open(b + "/card_template.html", "r", encoding = "utf-8")
    card_template_split = card_template.read().split("<!>")
    
    links, metadata, contents, story_card, page_card = ALL_PAGES[-1]
    title, date, author = metadata
    out = ""
    out += main_page_template_split[0] + "<a href = '" + links[0] + "'>" + title + "</a>"
    out += main_page_template_split[1] + date
    out += main_page_template_split[2] + author
    out += main_page_template_split[3] + contents[0]
    for i in range(1,len(contents)):
        out += "\n<br><br>\n" + contents[i]
    out += main_page_template_split[4]

    years = [int(name) for name in os.listdir(b + '/../stories/') if name.isdigit()]
    years.sort(reverse = True)
    for year in years:
        months = [int(name) for name in os.listdir(b + '/../stories/' + str(year) + '/') if name.isdigit()]
        months.sort(reverse = True)
        for month in months:
            out += '<li><a href="archive.html#' + MONTHSLIST[month-1] + str(year) + '">' + MONTHSLIST[month-1] + ' ' + str(year) + '</a></li>'
    out += main_page_template_split[5]

    

    single_col = ""
    cols = ["",""]
    front_page_stories = ALL_PAGES[-1*(len(ALL_PAGES)%7 + 7):-1]
    front_page_stories.reverse()
    for i,page in enumerate(front_page_stories):
        story_html = page[3]
        colInd = i%2
        cols[colInd] += story_html
        single_col += story_html
    out += single_col
    out += main_page_template_split[6]
    out += cols[0]
    out += main_page_template_split[7]
    out += cols[1]
    out += main_page_template_split[8]
    out += str(max([int(x) for x in os.listdir(b + "/../page") if x.isdigit()]))
    out += main_page_template_split[9]
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
            o1 += '<h1 id="' + monthList[month-1] + str(year) +'">' + monthList[month-1] + ' ' + str(year) + '</h1>\n<br>'
            o2 += '<a href="#' + monthList[month-1] + str(year) + '">' + monthList[month-1] + ' ' + str(year) + '</a>'
            days = [name for name in os.listdir(b + '/../stories/' + str(year) + '/' + str(month) + '/') if name.isdigit()]
            days.sort()
            days.reverse()
            for day in days:
                stories = [name for name in os.listdir(b + '/../stories/' + str(year) + '/' + str(month) + '/' + str(day) + '/')]
                for story in stories:
                    link = b + '/../stories/' + str(year) + '/' + str(month) + '/' + str(day) + '/' + story + '/'
                    txt_file = open(link + "story.txt", "r", encoding = "utf-8")
                    title = txt_file.read().split("\n")[0]
                    o1 += '<ul><a href="stories/' + str(year) + '/' + str(month) + '/' + str(day) + '/' + story + '/index.html">' + title + '</a></ul>'
    out = archive_page_template_split[0] + o2 + archive_page_template_split[1] + o1 + archive_page_template_split[2]
    archive_page.write(out)
    num_files_updated += 1

print("updated " + str(num_files_updated) + " file" + ("" if num_files_updated == 1 else "s"))