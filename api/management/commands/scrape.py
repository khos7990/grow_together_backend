from django.core.management.base import BaseCommand;
from bs4 import BeautifulSoup;
from api.models import Plant
import requests
import re



imageUrl = "http://www.tropicopia.com/house-plant/thumbnails/"
baseURL = "http://www.tropicopia.com/house-plant/detail.np/detail-"
     
class Command(BaseCommand):
    def handle(self, *args, **options):
       for num in range (1,356):
        newNum = str(num)
        if len(newNum) == 1:
            newNum = ("0" + newNum)
            url = baseURL + newNum + ".html" 
            result = requests.get(url)
            doc = BeautifulSoup(result.text, "html.parser")
            info = doc.find_all('p')
            image = doc.find_all('img')[12]
            image = (image['src'].split('/')[2])
            image = imageUrl + image
            name = info[10].text.strip()
            common = info[15].text.strip()
            light = info[34].text.strip()
            light = light.split('(')
            light = light[0]
            water = info[38].text.strip()
            water = water.split('&')
            water = water[0]
            insects = info[40].text.strip()
            disease = info[42].text.strip()
            if common == 'Common name :':
                newCommon = info[16].text.strip()
                newLight = info[35].text.strip()
                newLight = newLight.split('(')
                newLight = newLight[0]
                newWater = info[39].text.strip()
                newWater = newWater.split('&')
                newWater = newWater[0]
                newInsects = info[41].text.strip()
                newDisease = info[43].text.strip()
                if Plant.objects.filter(scientific_name = name):
                    continue
                else:
                    Plant.objects.create(
                        scientific_name = name,
                        common_name = newCommon, 
                        water_use = newWater,
                        light = newLight,
                        insects = newInsects,
                        disease = newDisease,
                        image = image
                    )
            elif light == 'Light tolered :':
                otherLight = info[33].text.strip()
                otherLight = otherLight.split('(')
                otherLight = otherLight[0]
                otherWater = info[37].text.strip()
                otherWater = otherWater.split('&')
                otherWater = otherWater[0]
                otherInsects = info[39].text.strip()
                otherDisease = info[41].text.strip()
                if Plant.objects.filter(scientific_name = name):
                    continue
                else:
                    Plant.objects.create(
                        scientific_name = name,
                        common_name = common, 
                        water_use = otherWater,
                        light = otherLight,
                        insects = otherInsects,
                        disease = otherDisease,
                        image = image
                    )
            elif common == 'Common name (fr.) :':
                unknownCommon = 'N/A'
                unknownCommonlight = info[32].text.strip()
                unknownCommonlight = unknownCommonlight.split('(')
                unknownCommonlight = unknownCommonlight[0]
                unknownCommonWater = info[36].text.strip()
                unknownCommonWater = unknownCommonWater.split('&')
                unknownCommonWater = unknownCommonWater[0]
                unknownCommonInsects = info[38].text.strip()
                unknownCommonDisease = info[40].text.strip()
                if Plant.objects.filter(scientific_name = name):
                    continue
                else:
                    Plant.objects.create(
                        scientific_name = name,
                        common_name = unknownCommon, 
                        water_use = unknownCommonWater,
                        light = unknownCommonlight,
                        insects = unknownCommonInsects,
                        disease = unknownCommonDisease,
                        image = image
                    )
            elif water == 'Insects :':
                altWater = info[37].text.strip()
                altWater = altWater.split('&')
                altWater = altWater[0]
                altInsects = info[39].text.strip()
                altDisease = info[41].text.strip()
                if Plant.objects.filter(scientific_name = name):
                    continue
                else:
                    Plant.objects.create(
                        scientific_name = name,
                        common_name = common, 
                        water_use = altWater,
                        light = light,
                        insects = altInsects,
                        disease = altDisease,
                        image = image
                    )
            else:
                 if Plant.objects.filter(scientific_name = name):
                    continue
                 else:
                    Plant.objects.create(
                    scientific_name = name,
                    common_name = common, 
                    water_use = water,
                    light = light,
                    insects = insects,
                    disease = disease,
                    image = image
                )
            self.stdout.write('job complete')
        else:
            url = baseURL + newNum + ".html" 
            result = requests.get(url)
            doc = BeautifulSoup(result.text, "html.parser")
            info = doc.find_all('p')
            image = doc.find_all('img')[12]
            image = (image['src'].split('/')[2])
            image = imageUrl + image
            name = info[10].text.strip()
            common = info[15].text.strip()
            light = info[34].text.strip()
            light = light.split('(')
            light = light[0]
            water = info[38].text.strip()
            water = water.split('&')
            water = water[0]
            insects = info[40].text.strip()
            disease = info[42].text.strip()
            if common == 'Common name :':
                newCommon = info[16].text.strip()
                newLight = info[35].text.strip()
                newLight = newLight.split('(')
                newLight = newLight[0]
                newWater = info[39].text.strip()
                newWater = newWater.split('&')
                newWater = newWater[0]
                newInsects = info[41].text.strip()
                newDisease = info[43].text.strip()
                if Plant.objects.filter(scientific_name = name):
                    continue
                else:
                    Plant.objects.create(
                        scientific_name = name,
                        common_name = newCommon, 
                        water_use = newWater,
                        light = newLight,
                        insects = newInsects,
                        disease = newDisease,
                        image = image
                    )
            elif light == 'Light tolered :':
                otherLight = info[33].text.strip()
                otherLight = otherLight.split('(')
                otherLight = otherLight[0]
                otherWater = info[37].text.strip()
                otherWater = otherWater.split('&')
                otherWater = otherWater[0]
                otherInsects = info[39].text.strip()
                otherDisease = info[41].text.strip()
                if Plant.objects.filter(scientific_name = name):
                    continue
                else:
                    Plant.objects.create(
                        scientific_name = name,
                        common_name = common, 
                        water_use = otherWater,
                        light = otherLight,
                        insects = otherInsects,
                        disease = otherDisease,
                        image = image
                    )
            elif common == 'Common name (fr.) :':
                unknownCommon = 'N/A'
                unknownCommonlight = info[32].text.strip()
                unknownCommonlight = unknownCommonlight.split('(')
                unknownCommonlight = unknownCommonlight[0]
                unknownCommonWater = info[36].text.strip()
                unknownCommonWater = unknownCommonWater.split('&')
                unknownCommonWater = unknownCommonWater[0]
                unknownCommonInsects = info[38].text.strip()
                unknownCommonDisease = info[40].text.strip()
                if Plant.objects.filter(scientific_name = name):
                    continue
                else:
                    Plant.objects.create(
                        scientific_name = name,
                        common_name = unknownCommon, 
                        water_use = unknownCommonWater,
                        light = unknownCommonlight,
                        insects = unknownCommonInsects,
                        disease = unknownCommonDisease,
                        image = image
                    )
            elif water == 'Insects :':
                altWater = info[37].text.strip()
                altWater = altWater.split('&')
                altWater = altWater[0]
                altInsects = info[39].text.strip()
                altDisease = info[41].text.strip()
                if Plant.objects.filter(scientific_name = name):
                    continue
                else:
                    Plant.objects.create(
                        scientific_name = name,
                        common_name = common, 
                        water_use = altWater,
                        light = light,
                        insects = altInsects,
                        disease = altDisease,
                        image = image
                    )
            else:
                if Plant.objects.filter(scientific_name = name):
                    continue
                else:
                    Plant.objects.create(
                    scientific_name = name,
                    common_name = common, 
                    water_use = water,
                    light = light,
                    insects = insects,
                    disease = disease,
                    image = image
                )
            self.stdout.write('job complete')
                



          
