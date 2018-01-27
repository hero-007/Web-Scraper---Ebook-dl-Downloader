import requests as rs
from bs4 import BeautifulSoup as bsoup
import download_from_ebook_dl as ded


base_url = 'http://ebook-dl.com/Search/'
base_item_url = 'http://ebook-dl.com'

search_book = input("Enter the book that you would like to search : ")
search_book = search_book.strip(' ')
search_book = search_book.replace(' ','%20')

final_url = base_url + search_book

get_response = rs.get(final_url)

# print(get_response.status_code)

response = bsoup(get_response.text,'html.parser')

book_list = response.findAll('div',{'class':'four shop columns'})
book_details = []
for i in book_list:
    book_item = i.find('a')
    book_name_img = book_item.find('img')
    book_link = base_item_url+book_item['href']
    book_name = book_name_img['alt']
    book_number = book_item['href']
    book_number = book_number[6::]
    book_details.append(tuple([book_name,book_link,book_number]))

if len(book_details)!= 0:
    print('############# BOOK SEARCH RESULTS ################\n\n')
    i = 1
    for j in book_details:
        print(str(i)+':',j[0])
        print('\t URL :',j[1])
        print('\t Book NO:',j[2])
        print('\n\n')
        i+=1

    download_ans = input("\n\nWOULD YOU LIKE TO DOWNLOAD/CHECKOUT A BOOK ( y/n ) : ")

    if download_ans == 'y' or download_ans == 'n':
        book_download_num = int(input("\nENTER THE SERIAL NUMBER OF THE BOOK THAT YOU WOULD LIKE TO CHECKOUT/DOWNLOAD : "))
        if book_download_num < len(book_list) and book_download_num > 0:
            book = book_details[book_download_num-1]
            book_detail_tuple = ded.information_extractor(book[0],book[1],book[2])
            print("\n\n############## BOOK INFORMATION ###############\n\n")
            print('BOOK NAME        :',book_detail_tuple[0])
            print('BOOK AUTHOR      :',book_detail_tuple[1])
            print('BOOK PUBLISHER   :',book_detail_tuple[2])
            print('BOOK FILE SIZE   :',book_detail_tuple[3])
            print('BOOK FILE FORMAT :',book_detail_tuple[4])
            print('\n\nBOOK DESCRIPTION :',book_detail_tuple[5],'\n\n')

            book_down = input("WOULD YOU LIKE TO DOWNLOAD THIS BOOK (y/n) : ")

            if book_down == 'y' or book_down == 'Y':
                bd_link = book_detail_tuple[6]
                ded.download_books(bd_link)
                print('######### THANK YOU FOR DOWNLOADING THIS BOOK #########')

    input("\n\n ###### PRESS ANY KEY TO EXIT ######")
else:
    print("############# NO BOOK FOUND ################")


