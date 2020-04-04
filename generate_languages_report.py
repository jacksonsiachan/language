#! /usr/bin/env Python3

import csv
import sys
import os
import datetime

languages = {'en':'English', 'ru':'Russian', 'zh':'Chinese', 'ko':'Korean', 'es':'Spanish', 'pt':'Portuguese', 
             'ja':'Japanese', 'jp':'Japanese', 'pl':'Polish', 'de':'German', 'it':'Italian', 'tr':'Turkish',
             'fr':'French', 'th':'Thai', 'vi':'Vietnamese', 'nl':'Dutch', 'cs':'Czech', 'el':'Greek', 'ar':'Arabic',
             'hu':'Hungarian', 'sv':'Slovenian', 'uk':'Ukrainian', 'ro':'Romanian', 'sk':'Slovak', 'bg':'Bulgarian', 
             'da':'Danish', 'id':'Indonesian', 'fi':'Finnish', 'nb':'Norwegian Bokmål', 'sl':'Slovene', 'et':'Estonian',
             'be':'Belarusian', 'ca':'Catalan', 'he':'Hebrew', 'hi':'Hindi', 'jv':'Javanese', 'lv':'Latvian', 'ta':'Tamil',
             'hr':'Croatian', 'fa':'Persian', 'sr':'Serbian', 'lt':'Lithuanian', 'sa':'Sanskrit', 'sm':'Samoan', 'ka':'Georgian', 'az':'Azerbaijani'}


def create_list(source_file):

   with open(source_file) as process_list:  
        reader = csv.reader(process_list)
        first_list = []
        for row in reader:
            first_list.append(row)
        second_list = []
        for line in first_list[1:]:
            second_list.append(line)
        return second_list                 


def process(second_list):

    dict = {}    
    for items in second_list:
        language, view = items
        if language not in dict:
             dict[language] = int(view)    
        else:
             dict[language] += int(view) 

    dic={}
    for key, value in dict.items():
        if key[0:2] not in dic:
             dic[key[0:2]] = value
        else:
             dic[key[0:2]] += value     
    return dic  

def rename_key(languages,dic):

    converted = {languages.get(lang_code, lang_code):count for lang_code, count in dic.items()}  # Dictonary comprehension
    return converted

def final_report(converted):  

    list = sorted(converted.items(), key=lambda kv:(kv[1], kv[0]), reverse=True)
    header = ["Languages", "Users"]
    now = datetime.datetime.now() 
    path = os.path.expanduser('~') + '/Desktop/' + str(now) + ' languages.csv'  
    with open(path, 'w') as language:
         writer = csv.writer(language)
         writer.writerow(header)
         for line in list:
             writer.writerow(line)       

if __name__ == "__main__":
  
    source_file = sys.argv[1]
    second_list = create_list(source_file)
    dic = process(second_list)  
    converted = rename_key(languages,dic)
    final_report(converted)   
    
    
    
    
                     

    

        
