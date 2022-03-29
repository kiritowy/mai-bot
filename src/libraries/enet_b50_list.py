import  requests,json
import pymysql

def searchRank(userId):
    url = 'http://youraquaurl/Maimai2Servlet/Maimai2Servlet/GetUserRatingApi'
    data1 = {'userId':userId}
    datajs = json.dumps(data1)
    # logger.info(datajs)
    req = requests.post(url,data=datajs,headers={"Content-Type":"application/json"},verify = False)
    result = req.text
    return result

def searchMusic(userId):
    url = 'http://youraquaurl/Maimai2Servlet/Maimai2Servlet/GetUserMusicApi'
    data1 = {'userId':userId,'nextIndex':0, 'maxCount':9999}
    datajs = json.dumps(data1)
    # logger.info(datajs)
    req = requests.post(url,data=datajs,headers={"Content-Type":"application/json"},verify = False)
    result = req.text
    return result
def getb50list(userId):
    rankout = json.loads((searchRank(userId)))
    musicout = json.loads((searchMusic(userId)))
    # oldlist = []
    # oldlistlevel = []
    # newlist = []
    # newlistlevel = []
    # # print(len(rankout['userRating']['ratingList']))
    # for i in range(0, len(rankout['userRating']['ratingList'])):
    #     musicid = rankout['userRating']['ratingList'][i]['musicId']
    #     musiclevel = rankout['userRating']['ratingList'][i]['level']
    #     oldlist.append(musicid)
    #     oldlistlevel.append(musiclevel)
    # for o in range(0, len(rankout['userRating']['newRatingList'])):
    #     musicid = (rankout['userRating']['newRatingList'][o]['musicId'])
    #     musiclevel = (rankout['userRating']['newRatingList'][o]['level'])
    #     newlist.append(musicid)
    #     newlistlevel.append(musiclevel)


    # print(oldlist)
    # print(oldlistlevel)
    # print(newlist)
    # print(newlistlevel)
    # print(searchMusic(45601466))


    charts = []
    sd = []
    dx = []
    scoreRank = 'd c b bb bbb a aa aaa s sp ss ssp sss sssp'.split(' ')
    fclist = ['', 'fc', 'fcp', 'ap', 'app']
    # print(musicout['userMusicList'][0]['userMusicDetailList'])
    for i in range(0, len(rankout['userRating']['ratingList'])):
        musicid = rankout['userRating']['ratingList'][i]['musicId']
        musiclevel = rankout['userRating']['ratingList'][i]['level']
        achi = rankout['userRating']['ratingList'][i]['achievement']
        conn = pymysql.connect(host='localhost',user = "root",password = "pw",db = "music")
        cursor=conn.cursor()
        cursor.execute(f"select title,ds,level from music where id = '{str(musicid)}';")
        while 1:
            res=cursor.fetchone()
            if res is None:
                #表示已经取完结果集
                break
            # print (res)
            title = res[0]
            dsall = res[1]
            levelall = res[2]
        cursor.close()
        conn.commit()
        conn.close()
        ds = json.loads(dsall)[musiclevel]
        level = json.loads(levelall)[musiclevel]
        # print(title)
        # print(ds)
        # print(level)
        # print(musicid)
        # print(musiclevel)
        # print(f"i={i}")
        for a in range(0, len(musicout['userMusicList'][0]['userMusicDetailList'])):
            # print(f"a={a}")
            if musicid == musicout['userMusicList'][0]['userMusicDetailList'][a]['musicId'] and musiclevel == musicout['userMusicList'][0]['userMusicDetailList'][a]['level']:
                scoreRank1 = musicout['userMusicList'][0]['userMusicDetailList'][a]['scoreRank']
                # tests2 = musicout['userMusicList'][0]['userMusicDetailList'][0]['achievement']
                combo = musicout['userMusicList'][0]['userMusicDetailList'][a]['comboStatus']
                # print(musicid)
                # print(musiclevel)
                sd.append({"song_id":str(musicid),"level_index":int(musiclevel), "type":"SD","rate":scoreRank[scoreRank1], 'fc':fclist[int(combo)],'achievements':float(achi/10000),'title':title,'ds':ds,'level':level})

    for o in range(0, len(rankout['userRating']['newRatingList'])):
        musicid = rankout['userRating']['newRatingList'][o]['musicId']
        musiclevel = rankout['userRating']['newRatingList'][o]['level']
        achi = rankout['userRating']['newRatingList'][o]['achievement']
        conn = pymysql.connect(host='localhost',user = "root",password = "pw",db = "music")
        cursor=conn.cursor()
        cursor.execute(f"select title,ds,level from music where id = '{str(musicid)}';")
        while 1:
            res=cursor.fetchone()
            if res is None:
                #表示已经取完结果集
                break
            # print (res)
            title = res[0]
            dsall = res[1]
            levelall = res[2]
        cursor.close()
        conn.commit()
        conn.close()
        ds = json.loads(dsall)[musiclevel]
        level = json.loads(levelall)[musiclevel]
        # print(title)
        # print(ds)
        # print(level)
        # print(musicid)
        # print(musiclevel)
        # print(f"i={i}")
        for a in range(0, len(musicout['userMusicList'][0]['userMusicDetailList'])):
            # print(f"a={a}")
            if musicid == musicout['userMusicList'][0]['userMusicDetailList'][a]['musicId'] and musiclevel == musicout['userMusicList'][0]['userMusicDetailList'][a]['level']:
                scoreRank1 = musicout['userMusicList'][0]['userMusicDetailList'][a]['scoreRank']
                # tests2 = musicout['userMusicList'][0]['userMusicDetailList'][0]['achievement']
                combo = musicout['userMusicList'][0]['userMusicDetailList'][a]['comboStatus']
                # print(musicid)
                # print(musiclevel)
                dx.append({"song_id":str(musicid),"level_index":int(musiclevel), "type":"DX","rate":scoreRank[scoreRank1], 'fc':fclist[int(combo)],'achievements':float(achi/10000),'title':title,'ds':ds,'level':level})
    
    def searchMaiInfo(Userid:str):
        url = 'http://youraquaurl/Maimai2Servlet/Maimai2Servlet/GetUserPreviewApi'
        data1 = {'userId':Userid, 'segaIdAuthKey': ""}
        datajs = json.dumps(data1)
        req = requests.post(url,data=datajs,headers={"Content-Type":"application/json"},verify = False)
        result = req.text
        req1 = json.loads(result)
        return req1
    user = searchMaiInfo(userId)
    username = user['userName']
    charts.append({"nickname":username,"dx":dx,"sd":sd})
    fin = json.dumps(charts)
    return fin
    