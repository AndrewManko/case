"""Case-study #5
Developer: Manko A.

"""

import urllib.request

with open('input.txt', 'r') as f_in:
    links = f_in.readlines()
with open('output.txt', 'w') as f_out:
    for url in links:
        f = urllib.request.urlopen(url)
        text = str(f.read())
        part_name = text.find("player-name")
        name = text[text.find('>',part_name)+1:text.find('&',part_name)]
        start = text.find('TOTAL')
        res = text[text.find('<td>', start)+5:text.find('</tr>', start)]
        lst = ['<td>', r'\n',r'\t']
        for i in lst:
            res = res.replace(i, '')
        res = res.replace(r'</td>', ' ').split()
        f_out.write('{:20}{:7}{:7}{:10}{:7}{:7}{:7}\n'.format(name, res[0], res[1], res[3], res[5], res[6], res[9]))
