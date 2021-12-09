import urllib.request
import json
# 调用高德地图的接口
# https://restapi.amap.com/v3/weather/weatherInfo?city=110101&key=f3f5c21c63094d5b05d259d73fe43893
# citykey = "110101"

def get_weather_data():
    citykey = input("请输入要查询的城市代码，（例如北京是110101）：")
    url1 = "https://restapi.amap.com/v3/weather/weatherInfo?city="+f"{citykey}"+"&key=f3f5c21c63094d5b05d259d73fe43893"

    # 读取网页数据
    weather = urllib.request.urlopen(url1)
    weather_read = str(weather.read(),'utf-8')  #会得到二进制数据则由bytes类型表示,然后转成中文
    #print(weather_read)
    weather_dict = json.loads(weather_read)  #将json数据转换为dict数据
    print(weather_dict)
    #print(type(weather_dict))

    # 获取了接口的lives值
    weather_list = weather_dict.get('lives')
    print("城市信息情况: ",weather_list)

get_weather_data()
