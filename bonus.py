import statistics as stats

values = [2000001, 2002001,2004001,2006001,2008001,2010001,2014001,2014001,2016001,2018001,2020001,2022001,2024001,2026001,2028001,2030001,2032001,2034001,2036001,2038001,2040001,2042001,2044001,2046001,2048001,2050001,2052001,2054001,2056001,2058001,2060001,2062001,2064001,2066001,2068001,2070001,2072001,2074001,2076001,2078001,2080001,2082001,2084001,2086001,2088001,2090001,2092001,2094001,2096001,2098001,2100001,2102001,2104001,2106001,2108001,2110001,2112001,2114001,2116001,2118001,2120001,2122001,2124001,2126001,2128001,2130001,2132001,2134001,2136001,2138001,2140001,2142001,2144001,2146001,2148001,2150001,2152001,2154001,2156001,2158001,2160001,2162001,2164001,2166001,2168001,2170001,2172001,2174001,2176001,2178001,2180001,2182001,2184001,2186001,2188001,2190001,2192001,2194001,2196001,2198001,2200001,2202001,2204001,2206001,2208001,2210001,2212001,2214001,2216001,2218001,2220001,2222001,2224001,2226001,2228001,2230001,2232001,2234001,2236001,2238001,2240001,2242001,2244001,2246001,2248001]

count = (len(values))
print (count)

sum = (sum(values))
print (sum)

mean = (stats.mean(values))
print(mean)
median = (stats.median(values))
print(median)
mode = (stats.mode(values))   
print (mode)

print ("The total claims count was",(count),"with an average loss of",(mean),";the total severity was",(sum), "with and median of",(median),"and mode",(mode),"!")
