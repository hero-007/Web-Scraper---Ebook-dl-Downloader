from urllib import request as rq
import requests as rs
from bs4 import BeautifulSoup as bs



def information_extractor(book_name,book_item_link,book_number):
    """
    This function is used to extract the following information about the book:
        1: Book name
        2: Book Author
        3: Book Publisher
        4: File Format
        5: File Size
        6: Book Description

    """
    book_page = rs.get(book_item_link)
    b_soup = bs(book_page.text,'html.parser')

    page_detail_table = b_soup.find('div',{'class':'product-page'})
    book_table = page_detail_table.findAll('tr')

    book_author = book_table[0].find('td').text
    book_publisher = book_table[3].find('td').text
    book_file_size = book_table[6].find('td').text
    book_file_format = book_table[7].find('td').text

    # Book description extraction

    book_description_section = b_soup.find('p',{'class':'margin-reset'})
    book_description = book_description_section.text

    # Book download link
    book_download_link = "http://ebook-dl.com/downloadshort/"+book_number

    book_detail_tuple = tuple([book_name,book_author,book_publisher,book_file_size,book_file_format,book_description,book_download_link])
    return book_detail_tuple


def download_books(download_link):
    """
    Function takes a download link as an input and download the resource from that link
    :param download_link:
    :return:
    """

    local_filename,header = rq.urlretrieve(download_link)
    print('Your file saved by name :',local_filename)

    return
