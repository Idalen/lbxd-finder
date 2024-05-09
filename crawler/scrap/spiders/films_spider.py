import scrapy
from pathlib import Path
from bs4 import BeautifulSoup
import pandas as pd


class UserCatalog(scrapy.Spider):
    
    name = "films"
    
    def start_requests(self):
        user = "idalen"
        
        urls = [
            f"https://letterboxd.com/{user}/films/page/1",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-1]
        user = response.url.split("/")[-4]
        
        filename = f"{user}-films-{page}.html"
        
        html_content = response.body
        soup = BeautifulSoup(html_content, 'html.parser')
        
        posters = soup.findAll("li", class_="poster-container")
        
        for poster in posters:
            if poster:
                data_div = poster.find('div')
                
                film_slug = data_div.get('data-film-slug')
                # film id
                # rating
                


                # Print the extracted film slug
                print(film_slug)
            else:
                print("Container element not found")
        
        
        
        
        
        
        #Path(filename).write_bytes(response.body)
        #self.log(f"Saved file {filename}")



