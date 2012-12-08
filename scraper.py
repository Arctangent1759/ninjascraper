import urllib2, urllib

ways = ["","%20(solution)","%20solution"] 
tests = ['Midterm','Midterm%201','Midterm%202', 'Midterm%203','Final']
semesters = ["Fall", "Spring", "Summer"]
years = [str(n) for n in range(1990, 2013)]

def scrape_ninja(course, department, abv, prof):
    base_url = "http://media.ninjacourses.com/var/exams/1/{0}/{1}%20{2}%20-%20{3}%20{4}%20-%20{5}%20-%20{6}{7}.pdf"
    exists = {}
    combinations = [[way, test, semester, year] for way in ways for test in tests
                    for semester in semesters for year in years]
    for comb in combinations:
        way, test, sem, year = comb
        # print department, abv, course, sem, year, prof, test, way
        try:
            url = base_url.format(department,abv,course,sem,year,prof,test,way)
            # print(url)
            urllib2.urlopen(url)
            info = '-'.join([abv + course, sem, year, prof, test]) + way
            info = info.replace('%20', '-')
            exists[info] = url
        except Exception as e:
            pass
    if exists != {}:
        for info,url in exists.iteritems():
            print url
            urllib.urlretrieve(url, info+ '.pdf')
    else:
        print('Not found!')


defaults = {'Course Number': '61A',
            'Department': 'COMPSCI',
            'Abbreviation': 'CS'}
professors = ["Harvey","Denero"]
while True:
    for key, value in defaults.items():
        val = raw_input(key + ' (default ' + value + ') : ')
        if val != '':
            defaults[key] = val

    val = raw_input('Enter a list of professor names (default '
                + str(professors) + ') : ')
    if val != '':
        val = eval(val)
        assert type(val) is list, 'Must enter a list!'
        professors = val
    
    for prof in professors:
        scrape_ninja(defaults['Course Number'], defaults['Department'],
                     defaults['Abbreviation'], prof)
