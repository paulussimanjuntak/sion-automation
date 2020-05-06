import mechanize
from typing import List
from bs4 import BeautifulSoup

class AutomationSion:
    def __init__(self,nim: str, password: str,harapan: List):
        self.nim = nim
        self.password = password
        self.harapan = harapan

    def automated(self) -> int:
        url = "http://sion.stikom-bali.ac.id"
        br = mechanize.Browser()
        br.open(url)
        # login to sion
        br.select_form(id="htmlForm")
        br.form['uname'] = self.nim
        br.form['passwd'] = self.password
        br.submit()
        # access kuesioner
        try:
            br.open(url + '/reg/KuesionerPBM/')
            soup = BeautifulSoup(br.response().read(),"html.parser")
            # get all mata kuliah
            raw_mata_kuliah = soup.find_all("a")[1:]
            mata_kuliah = [x['href'] for x in raw_mata_kuliah]

            # fill up all kuesioner
            for link in mata_kuliah:
                br.open(link)
                br.select_form(id="bootstrapSelectForm")

                soup = BeautifulSoup(br.response().read(),"html.parser")
                raw_harapan = soup.find_all("input",attrs={'type':'radio'})
                harapan = [x['name'] for x in raw_harapan]

                br.form['komentar'] = 'automated by python'
                br.form['komentar2'] = 'automated by python'

                for radio in harapan:
                    br.form[radio] = self.harapan

                br.submit()

            return 200
        except Exception:
            return 400
