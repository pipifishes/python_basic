import urllib.request
import json
'''
调用高德地图的天气API接口
https://restapi.amap.com/v3/weather/weatherInfo?city=110101&key=f3f5c21c63094d5b05d259d73fe43893&extensions=all
citykey = "110101"
'''


def get_weather_data():
    citykey = input("请输入要查询的城市代码，（例如北京是110101）：")
    url1 = "https://restapi.amap.com/v3/weather/weatherInfo?city="+f"{citykey}"+"&key=f3f5c21c63094d5b05d259d73fe43893&extensions=all"

    # 读取网页数据
    weather = urllib.request.urlopen(url1)
    weather_read = str(weather.read(),'utf-8')  #会得到二进制数据则由bytes类型表示,然后转成中文
    #print(weather_read)
    weather_dict = json.loads(weather_read)  #将json数据转换为dict数据
    #print(weather_dict)
    #print(type(weather_dict))

    # 获取了接口的forecasts值
    weather_list = weather_dict.get('forecasts')
    #print("城市信息情况: ",weather_list)     #打印出来，发现是字典格式里有列表
    print("province: ",weather_list[0].get('province'))
    print("city: ", weather_list[0].get('city'))
    print("reporttime: ", weather_list[0].get('reporttime'))

    print("dayweather: ", weather_list[0].get('casts')[0].get('dayweather'))
    print("nightweather: ", weather_list[0].get('casts')[0].get('nightweather'))
    print("daytemp: ", weather_list[0].get('casts')[0].get('daytemp')+'°C')
    print("nighttemp: ", weather_list[0].get('casts')[0].get('nighttemp')+'°C')
    print('*' * 50)

    weather_forecast = input("是否需要查看未来几天的天气情况： y/n：")
    if weather_forecast == 'y':
        for i in range(1,4):
            print("date: ", weather_list[0].get('casts')[i].get('date'))
            print("dayweather: ", weather_list[0].get('casts')[i].get('dayweather'))
            print("daytemp: ", weather_list[0].get('casts')[i].get('daytemp')+'°C')
            print("daytemp: ", weather_list[0].get('casts')[i].get('nighttemp')+'°C')
            print('*' * 50)
    else:
        print('*'*80)


get_weather_data()
