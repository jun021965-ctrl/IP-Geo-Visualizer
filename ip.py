import requests
import folium

ip = input("请输入要查询的 IP 地址： ")

# 使用国内可访问的 API
url = f"http://ip-api.com/json/{ip}?lang=zh-CN"

data = requests.get(url).json()

print("\n===== IP 地理信息 =====")
print("IP 地址:", ip)
print("国家:", data.get("country"))
print("城市:", data.get("city"))
print("经度:", data.get("lon"))
print("纬度:", data.get("lat"))
print("运营商:", data.get("isp"))

lat = data.get("lat")
lon = data.get("lon")

m = folium.Map(location=[lat, lon], zoom_start=10)

folium.Marker(
    [lat, lon],
    popup=f"{data.get('city')}, {data.get('country')}",
    tooltip="点击查看"
).add_to(m)

m.save("ip_location_map.html")

print("\n地图已生成：ip_location_map.html")
