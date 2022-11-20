from speedtest import Speedtest

st = Speedtest(secure=True)

download = st.download() / 1024 / 1024
upload = st.upload() / 1024 / 1024
ping = st.results.ping

print(f'Download: {download:.2f}\nUpload: {upload:.2f}\nPing: {ping:.0f}')