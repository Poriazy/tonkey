import httpx


def market_raw():
    url = 'http://www.tsetmc.com/tsev2/data/MarketWatchPlus.aspx'
    content = httpx.get(url).content.decode('utf-8')
    return content.split('@')[2].split(';')


def market():
    inst_price = market_raw()
    market = {}
    for item in inst_price:
        item = item.split(',')
        symbol = item[2]
        market[symbol] = dict(
            id=item[0],
            code=item[1],
            symbol=item[2],
            name=item[3],
            first_price=item[5],
            close_price=item[6],
            last_price=item[7],
            count=item[8],
            volume=item[9],
            value=item[10],
            min_traded_price=item[11],
            max_treaded_price=item[12],
            yesterday_price=item[13],
            eps=item[14],
            base_volume=item[15],
            c2=item[16],
            table_id=item[17],
            group_id=item[18],
            max_allowed_price=item[19],
            min_allowed_price=item[20],
            type_of_symbol=item[22],
            all_count_of_symbol=item[21]
        )
    return market


def market_list():
    inst_price = market_raw()
    market = []
    for item in inst_price:
        item = item.split(',')
        market.append(dict(
            id=item[0],
            code=item[1],
            symbol=item[2],
            name=item[3],
            first_price=item[5],
            close_price=item[6],
            last_price=item[7],
            count=item[8],
            volume=item[9],
            value=item[10],
            min_traded_price=item[11],
            max_treaded_price=item[12],
            yesterday_price=item[13],
            eps=item[14],
            base_volume=item[15],
            c2=item[16],
            table_id=item[17],
            group_id=item[18],
            max_allowed_price=item[19],
            min_allowed_price=item[20],
            type_of_symbol=item[22],
            all_count_of_symbol=item[21]
        ))
    return market


def get_dayprice(id):
    id = int(id)
    url = 'http://www.tsetmc.com/tsev2/chart/data/IntraDayPrice.aspx?i=%i' % id
    dayprice = []
    content = httpx.get(url).content.decode('utf-8').split(';')
    for item in content:
        item = item.split(',')
        try:
            dayprice.append(dict(
                time=item[0],
                high_price=item[1],
                low_price=item[2],
                open_price=item[3],
                close_price=item[4],
                volume=item[5]
            ))
        except BaseException:
            pass
    return dayprice


def get_day_general_info(id):
    id = int(id)
    url = 'http://www.tsetmc.com/tsev2/data/instinfodata.aspx?i=%i&c=' % id
    content = httpx.get(url).content.decode('utf-8').split(';')
    general_info = content[0]
    infodata = []
    item = general_info.split(',')
    try:
        if len(item) == 13:
            infodata = (dict(
                last_tarde_time=item[0],
                last_price=item[1],
                close_price=item[2],
                first_price=item[3],
                yesterday_price=item[4],
                max_traded_price=item[5],
                min_traded_price=item[6],
                count=item[7],
                volume=item[8],
                value=item[9],
                c1=item[10],
                c2date=item[11],  # georgian numeric date
                c3=item[12]  # numeric time
            ))
        if len(item) == 14:
            infodata = (dict(
                last_tarde_time=item[0],
                last_price=item[2],
                close_price=item[3],
                first_price=item[4],
                yesterday_price=item[5],
                max_traded_price=item[6],
                min_traded_price=item[7],
                count=item[8],
                volume=item[9],
                value=item[10],
                c1=item[11],
                c2date=item[12],  # georgian numeric date
                c3=item[13]  # numeric time
            ))
    except BaseException:
        pass
    return infodata


def get_dayinfo(id):
    id = int(id)
    info = []
    url = 'http://www.tsetmc.com/tsev2/data/instinfodata.aspx?i=%i&c=74+' % id
    content = httpx.get(url).content.decode('utf-8').split(';')
    con1 = content[0]  # genral info
    infodata = []
    item = con1.split(',')
    try:
        if len(item) == 13:
            infodata.append(dict(
                last_tarde_time=item[0],
                last_price=item[1],
                close_price=item[2],
                first_price=item[3],
                yesterday_price=item[4],
                max_traded_price=item[5],
                min_traded_price=item[6],
                count=item[7],
                volume=item[8],
                value=item[9],
                c1=item[10],
                c2date=item[11],  # georgian numeric date
                c3=item[12]  # numeric time
            ))
        if len(item) == 14:
            infodata.append(dict(
                last_tarde_time=item[0],
                last_price=item[2],
                close_price=item[3],
                first_price=item[4],
                yesterday_price=item[5],
                max_traded_price=item[6],
                min_traded_price=item[7],
                count=item[8],
                volume=item[9],
                value=item[10],
                c1=item[11],
                c2date=item[12],  # georgian numeric date
                c3=item[13]  # numeric time
            ))
    except BaseException:
        pass
    try:
        item = content[4].split(',')  # client_typpe_info
        print(len(item))
        infodata.append(dict(
            haghighi_buy_volume=item[0],
            hoghughi_buy_volume=item[1],
            haghighi_sell_volume=item[3],
            hoghughi_sell_volume=item[4],
            haghighi_buy_count=item[5],
            hoghughi_buy_count=item[6],
            haghighi_sell_count=item[8],
            hoghughi_sell_count=item[9]
        ))
    except BaseException:
        pass
    con1 = content[2]  # book (tablo)
    try:
        info = [{**infodata[0], **infodata[1]}]
    except BaseException:
        info.append(infodata[0])
        pass
    ite = con1.split(',')
    for it in ite:
        try:
            i = it.split('@')
            info.append(dict(
                buy_count=i[0],
                buy_volume=i[1],
                buy_price=i[2],
                sell_price=i[3],
                sell_volume=i[4],
                sell_count=i[5]
            ))
        except BaseException:
            pass
    return info


def get_history(id):
    id = int(id)
    base_url = 'http://members.tsetmc.com/tsev2/data/InstTradeHistory.aspx'
    url = '%s?i=%i&Top=99999&A=0' % (base_url, id)
    content = httpx.get(url).content.decode('utf-8').split(';')
    history = []
    for item in content:
        item = item.split('@')
        try:
            history.append(dict(
                date=item[0],
                max_price=item[1],
                min_price=item[2],
                close_price=item[3],
                last_price=item[4],
                first_price=item[5],
                yesterday_price=item[6],
                value=item[7],
                volume=item[8],
                count=item[9]
            ))
        except BaseException:
            pass
    return history


def get_clienttype_history(id):
    id = int(id)
    url = 'http://www.tsetmc.com/tsev2/data/clienttype.aspx?i=%i' % id
    content = httpx.get(url).content.decode('utf-8').split(";")
    clienttype = []
    for item in content:
        item = item.split(',')
        try:
            clienttype.append(dict(
                date=item[0],
                haghighi_buy_count=item[1],
                hoghughi_buy_count=item[2],
                haghighi_sell_count=item[3],
                hoghughi_sell_count=item[4],
                haghighi_buy_volume=item[5],
                hoghughi_buy_volume=item[6],
                haghighi_sell_volume=item[7],
                hoghughi_sell_volume=item[8],
                haghighi_buy_value=item[9],
                hoghughi_buy_value=item[10],
                haghighi_sell_value=item[11],
                hoghughi_sell_value=item[12]
            ))
        except BaseException:
            pass
    return clienttype
