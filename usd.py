from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt

getPage = requests.get('https://www.bookmyforex.com/blog/1-usd-to-inr-in-1947-2018/')

pageText = getPage.text

soup = BeautifulSoup(pageText, 'lxml')

table = soup.find('table')
tableRows = table.find_all('tr')
usdData = []
for row in tableRows:
    rowData = []
    for data in row.find_all('td'):
        rowData.append(data.text)
    try:
        data1 = (int(rowData[0]),float(rowData[1]))
        data2 = (int(rowData[2]), float(rowData[3]))
        usdData.append(data1)
        usdData.append(data2)
    except:
        continue

usdData = sorted(usdData, key=lambda x: x[0])

xAxis = [x[0] for x in usdData]
yAxis = [x[1] for x in usdData]
# print(xAxis)
# print(yAxis)

plt.title('1 USD vs INR')
plt.plot(xAxis, yAxis)
plt.xlabel('Year')
plt.ylabel('1 USD in Indian Rupees')
# plt.legend()
plt.show()
