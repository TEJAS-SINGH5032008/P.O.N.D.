import random
import ploty.figure_factory as ff
import satistics
import ploty.graph_objects as go

dice_result = []
for i in range(0,1000)
dice1 = random.randint(1,6)
dice2 = random.randint(1,6)
dice_result.append(dice1 + dice2)

mean = sum(dice_result) / len(dice_result)
std_deviation = statistics.stdev(dice_result)
median = statistics.median(dice_result)
mode = statistics.mode(dice_result)
first_std_deviation_start,first_std_deviation_end = mean -std_deviation, mean +std_deviation
second_std_deviation_start,second_std_deviation_end = mean -(2*std_deviation), mean +(2*std_deviation)
third_std_deviation_start,third_std_deviation_end = mean -(3*std_deviation), mean +(3*std_deviation)

fig = ff.create_distplot([dice_result], ["Result"], show_hist = False)
fig.add_trace(go.Scatter(x =[mean,mean], y = [0,0.17], mode = "lines" ,name = "MEAN"))
fig.add_trace(go.Scatter(x = [first_std_deviation_start,first_std_deviation_start], y = [0,0.17], mode =  "standard derivation 1"))
fig.add_trace(go.Scatter(x = [first_std_deviation_end,first_std_deviation_end], y = [0,0.17], mode =  "standard derivation 1"))
fig.add_trace(go.Scatter(x = [second_std_deviation_start,second_std_deviation_start], y = [0,0.17], mode =  "standard derivation 2"))
fig.add_trace(go.Scatter(x = [second_std_deviation_end,second_std_deviation_end], y = [0,0.17], mode =  "standard derivation 2"))
fig.show()

list_of_data_within_1_std_deviation = [result for result in dice_result if result > first_std_deviation_start and result <first_std_deviation_end]
list_of_data_within_2_std_deviation = [result for result in dice_result if result > second_std_deviation_start and result <second_std_deviation_end]
list_of_data_within_3_std_deviation = [result for result in dice_result if result > third_std_deviation_start and result <third_std_deviation_end]

print("mean of this data is {}".format(mean))
print("median of this data is {}".format(median))
print("mode of this data is {}".format(mode))
print("standard deviation of this data is {}"format(std_deviation))
print("{}% of data lies within 1 deviation".format(len(list_of_data_within_1_std_deviation)*100.0/len(dice_result)))
print("{}% of data lies within 2 deviation".format(len(list_of_data_within_2_std_deviation)*100.0/len(dice_result)))
print("{}% of data lies within 3 deviation".format(len(list_of_data_within_3_std_deviation)*100.0/len(dice_result)))