# We can easily show multiple lines in one line chart
# it's as simple as calling multiple plot() functions before show()

import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
air_fryers = [100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650] # upward trend
toasters = [650, 600, 550, 500, 450, 400, 350, 300, 250, 200, 150, 100] # downward trend
blenders = [300, 320, 310, 330, 290, 350, 370, 360, 340, 380, 390, 410] # mixed bag

plt.plot(months, air_fryers, label="air fryers")
plt.plot(months, toasters, label="toasters")
plt.plot(months, blenders, label="blenders")
plt.legend(bbox_to_anchor=(1, 0))
plt.show()