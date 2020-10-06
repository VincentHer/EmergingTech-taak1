# Importing Modules 
from urllib.request import urlopen
from xml.etree.ElementTree import parse
import urllib.parse
import requests

# API & Key 
main_api = "https://www.goodreads.com/search/index.xml?"
key = input('Please insert your key: ')


while True:
    # Asking input from the customer
    input_klant = input('Which book do you want to search [quit/exit]? ')

    # Counter to show the firt 5 results (8000 in total)
    counter = 1
    
    # Let the customer quit without KeyboardInterrupt
    if input_klant == 'q' or input_klant == 'quit' or input_klant == 'exit':
        break

    # Making the URL
    url = main_api + urllib.parse.urlencode({'key':key, 'q':input_klant})
    frase1 = 'URL: ' + url
    print(len(frase1) * '-')
    print(frase1)
    

    # Parsing the URL
    var_url  = urlopen(url)
    xmldoc = parse(var_url)

    # Making preperation for controlling the status code
    response = requests.get(url)
    
    # Request | status code control        
    if response.status_code == 200:
        frase2 = 'Succes! You will see the first 5 results.'
        print(frase2)
        print(len(frase2) * '-')

        # Retrieving important data
        for item in xmldoc.iterfind('search/results/work'):
            rating = item.findtext('average_rating')
            year = item.findtext('original_publication_year')
            
            for item2 in xmldoc.iterfind('search/results/work/best_book'):
                title = item2.findtext('title')
                image = item2.findtext('image_url')

                for item3 in xmldoc.iterfind('search/results/work/best_book/author'):
                    autheur = item3.findtext('name')
                    frase3 = str(counter) + '. ' + title + ' - ' + autheur + ' (' + str(year) + ') - [' + rating + '/5.00]'

            # Printing the first 5 search results
                if counter != 6:
                    print(frase3)
                    print('Book image: ' + image)
                    print('-' * len(frase3))
                    print(' ')
                    counter +=1
                else:
                    break                     
    else:
        print('Error! Search failed, try again.')
        print('-'*30)
        break   


        



    
            
            
        
        





    

    







