CSV_TYPE_CASH = 0
CSV_TYPE_DEBT = 1
CSV_TYPE_PROFIT = 2
CSV_TYPE_MAX = 3

cash_table_dict = {
    '经营活动现金流入小计(万元)':'business_activity_cash_income',
    '经营活动现金流出小计(万元)':'business_activity_cash_outcome',
    '经营活动产生的现金流量净额(万元)':'business_activity_cash_total',
    '投资活动现金流入小计(万元)':'investment_activity_cash_income',
    '投资活动现金流出小计(万元)':'investment_activity_cash_outcome',
    '投资活动产生的现金流量净额(万元)':'investment_activity_cash_total',
    '筹资活动现金流入小计(万元)':'fundraising_activity_cash_income',
    '筹资活动现金流出小计(万元)':'fundraising_activity_cash_outcome',
    '筹资活动产生的现金流量净额(万元)':'fundraising_activity_cash_total'
}

debt_table_dict = {
    '应收票据(万元)':'bill_checkin',
    '应收账款(万元)':'funds_checkin',
    '存货(万元)':'inventory',
    '固定资产(万元)':'fixed_asserts',
    '流动资产合计(万元)':'flowable_asserts_total',
    '非流动资产合计(万元)':'non_flowable_asserts_total',
    '资产总计(万元)':'asserts_total',
    '应付票据(万元)':'bill_checkout',
    '应付账款(万元)':'funds_checkout',
    '流动负债合计(万元)':'flowable_debt_total',
    '非流动负债合计(万元)':'non_flowable_debt_total',
    '负债合计(万元)':'total_debt'
}

profit_table_dict = {
    '营业总收入(万元)':'trading_income_total',
    '营业总成本(万元)':'trading_cost_total',
    '营业利润(万元)':'trading_profit',
    '营业外收入(万元)':'trading_outside_income',
    '营业外支出(万元)':'trading_outside_cost',
    '利润总额(万元)':'total_profit',
    '净利润(万元)':'pure_profit'
}

TABLE_LIST = [cash_table_dict, debt_table_dict, profit_table_dict]
CSV_DIR_LOCATION = [
    '/home/greetlist/extract_company_data/xjllb_csvs/',
    '/home/greetlist/extract_company_data/zcfzb_csvs/',
    '/home/greetlist/extract_company_data/lrb_csvs/',
]
