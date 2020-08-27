li=[
    43,
    44,
    45,
    46,
    50,
    51,
    52,
    53,
    54,
    61,
    62,
    63,
    64,
    65
]
for i in li:
    s='spark.read.parquet("/user/zh2_huawei_yybxyuser/obc/tods_location_detail_h/hour=2020082620/prov={0}/*").createOrReplaceTempView("tb1")'.format(i)
    print(s)
    print('sql("select length(lacid) lac_len,length(cellid) as len_cell,count(*) as cnt from tb1 a group by length(lacid),length(cellid) order by 3 desc").show(100)')
    print()