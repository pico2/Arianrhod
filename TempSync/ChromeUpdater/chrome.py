from ml import *
import asyncio

stable = r'''<?xml version='1.0' encoding='UTF-8'?><request protocol='3.0' ismachine='0'><app appid='{4DC8B4CA-1BDA-483E-B5FA-D3C12E15B62D}' ap='-multi-chrome'><updatecheck/></app></request>'''
beta = r'''<?xml version='1.0' encoding='UTF-8'?><request protocol='3.0' ismachine='0'><app appid='{4DC8B4CA-1BDA-483E-B5FA-D3C12E15B62D}' ap='1.1-beta'><updatecheck/></app></request>'''
dev = r'''<?xml version='1.0' encoding='UTF-8'?><request protocol='3.0' ismachine='0'><app appid='{4DC8B4CA-1BDA-483E-B5FA-D3C12E15B62D}' ap='2.0-dev'><updatecheck/></app></request>'''

stable = r'''<?xml version="1.0" encoding="UTF-8"?>
<request protocol="3.0" version="1.3.29.1" shell_version="1.3.29.1" ismachine="1" sessionid="{19A1B502-10BF-484F-8A0D-D67E94D1B62E}" installsource="taggedmi" requestid="{E6B71FEB-CC00-49F6-89A2-70DE65A2083A}" dedup="cr">
    <!-- <hw physmemory="6" sse="1" sse2="1" sse3="1" ssse3="1" sse41="1" sse42="1" avx="1"/> -->
    <os platform="win" version="10.0" sp="" arch="x86"/>
    <app appid="{8A69D345-D564-463C-AFF1-A69D9E530F96}" version="" nextversion="" lang="en" brand="" client="" installage="-1" installdate="-1" iid="{12066EC4-352D-45CF-A793-465E1E7EA180}">
        <updatecheck/>
    </app>
</request>'''

async def query_chrome(ver):
    req = network.AsyncHttp()
    # req.SetProxy('localhost', 6789)
    ret = await req.request('post', 'https://tools.google.com/service/update2', data = ver)

    info = ET.fromstring(ret.text())
    app = info.find('app')
    updatecheck = app.find('updatecheck')
    urls = updatecheck.find('urls')
    manifest = updatecheck.find('manifest')

    name = manifest.find('packages')[0].attrib['name']
    dllist = [(x.attrib['codebase'] + name) for x in urls]

    for url in dllist:
        print(url.split('://', maxsplit = 1)[1])
    print()

    return dllist

@asynclib.main
async def run():
    dl = (await query_chrome(stable))[-1]

    req = network.AsyncHttp()
    open(os.path.join('D:\\Desktop\\', os.path.basename(dl)), 'wb').write((await req.request('get', dl)).content)

def main():
    run()
    console.pause('done')

if __name__ == '__main__':
    Try(main)
