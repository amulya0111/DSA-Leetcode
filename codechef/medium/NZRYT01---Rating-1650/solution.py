def calculate_max_profit(stockPrices):
    buy1=buy2=-float('inf')
    sell1=sell2=0
    for Price in stockPrices:
        b1=buy1
        b2=buy2
        s1=sell1
        s2=sell2
        buy1=max(buy1,-Price)
        sell1=max(sell1,buy1+Price)
        buy2=max(buy2,sell1-Price)
        sell2=max(sell2,buy2+Price)
    return sell2