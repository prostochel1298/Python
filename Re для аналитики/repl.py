import re
text = ''''' 
1452319190
1452319489
1452490131
1452420146
1452520478
1452520574
1452520646
1452520671
2452520667
1452520691
1452520734
1452520933
1452621465
1452621450
1452621624
1452621655
1452621693
1452621765
1452621761
1452621843
1452621817
1452621867
1452722366
2452722435
2452796298
1452722669
3452707852
1452722723
1452722751
1452722862
1452792564
1452722953
2452823314
2453631055
1452823525
1453631072
1452807835
1453631078
2452823618
1452823644
1452823679
1452823710
1452823786
1452823837
1453631091
1452823955
1452823961
1452924521
1454138413
1453025290
1452924622
1452989303
1452924792
1452924828
1453025304
1453025352
1453025397
1453024604
1453084418
3453025352
1453025834
1453126171
1453126315
1453126194
1453126236
1453126260
1453631204
1453631219
3453126251
1453126368
1453126464
1453126511
1453126553
1453126568
1453126577
1453126604
1453126646
1453126688
1453126709
1453126732
1453227101
1453227093
1453631242
1453227324
1453227352
1453227387
1453631267
1453227531
1453227593
1453227582
3453227631
6453320574
1453327925
1453327959
1453327997
3453327970
1453328085
1453328190
3453320667
1453328264
1453328281
2453326236
1454239172
1453328326
1453328458
1453328455
1453328476
1453321867
1453631338
1453428871
1453428920
1453428931
1453428974
1453429010
1453426171
2453631375
1453631610
1453429077
1453631403
3453429098
1453429127
1453429133
2454848373
1453429278
1453429379
1453429390
1453631423
1453429478
1453429537
1453631431
1453529782
1453529800
1453529808
1453529879
1453529886
1453529906
1453631439
1453662967
1453527531
1454239201
2453530280
2453530307
3453530359
2453530388
2453530445
4453530558
2453630906
2453630910
2453631040
3453631503
1453631848
1453631693
1453631767
1453631812
3453732195
1453732216
1453732376
1453732396
2453732431
1453732728
1453732751
1453732801
1453732915
1453733019
1453733069
1454238905
2454340932
1454746977
1453733297
1453733301
3453733352
1453825201
1453834025
1453834107
1453834179
1454220667
1453834305
1453886778
3453834274
1453834473
2453834506
1453834521
1453889303
1453834548
1454747001
1453834578
1453834629
1453834767
1453935005
1454035848
1453935236
1454239048
1453935283
1454035855
1454035939
1454035946
1454239289
1454036115
1454036112
1454036114
1454036193
1454239304
2454036503
1454036484
1454207835
1454747050
1454036577
1454036625
1454036696
1454239377
2454239384
1454036918
1454747055
1454137293
1454137360
1454137479
1454239431
1454137519
1454137709
1454137733
1454137847
1454137987
1454138144
1454138131
1454138143
1454138227
1454138200
1454138389
1454239509
3454734277
1454239546
1454747092
1454747110
1454239610
1454239677
1454239697
1454340268
1454340431
1454340677
1454340701
1454340742
1454340780
1454340923
1454393832
1454340996
1454341101
1454442019
4454442075
2454442227
3454442664
1454442680
1454442745
1454521624
1454543361
1454543605
1454747372
1454543905
1454544083
1454544272
1454644891
1454645148
1454645238
1454645378
1454645387
1454645579
1454639546
1454645644
2454848109
1454623955
1454848630
2454848297
1454848468
1454848485
1454848661
1454848734
1454848768
2454849101
1454849114
1454949766
1454949887
1454950389
1454950388
1454950564
1454950764
1454950844
1452016557
1452622159
1454747658
1453631496
2453630990
1454238837
1454238911
1454238953
1454747009
1454035779
1454239323
2454036703
1454036908
1454137461
1454138128
1454747088
1454239528
1454239801
3454239948
1454340464
1454340559
1454340814
1454848451
2454744273
1454341421
1454441603
1454441648
1454441661
1454543511
1454442035
2454442311
2454543159
2454543325
1454543330
1454579147
1454848121
1454639948
1454746517
1454746551
2454949412
3454949742
1454949866
1454950428
'''
pattern = r"\d+"
repl = r"'\d+',"
print(re.findall(r"\d+",text))