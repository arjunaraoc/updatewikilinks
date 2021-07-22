# update wiki links
# When localising English wiki pages, the target wiki links are to be updated
# This program is used to update the wikilinks  stored in csv file, with find, replace
# as header and english text, target wiki  as mapped values
# inputs
#   enwiki source file
#   mapping file csv with ilinks,page_titleTE as header :: get this with wd query (example:https://w.wiki/3S6s)
# outputs
#   target wikifile


import csv

def upd_wiki_links():
    file = 'enwiki.txt'
    file_open = open(file, 'r')
    file_read = file_open.read()

    links_list=[]
    map_file = 'wikilinksmap.csv'
    with open(map_file, mode='r') as csv_file:
        dict_replace = csv.DictReader(csv_file)
        for row in dict_replace:
            links_list.append( ("[["+row['ilinks'], "[["+row['page_titleTE']))
    new_content = replace_content(links_list, file_read)
    new_file = 'tewiki.txt'
    new_file_open = open(new_file, 'w')
    new_file_open.write(new_content)
    new_file_open.close()

def replace_content(map_changes, target):
    """Based on dict, replaces key with the value on the target."""
    for  check, replacer in map_changes:
        #target = sub(check, replacer, target)
        target = target.replace(check, replacer)
    return target

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    upd_wiki_links()


