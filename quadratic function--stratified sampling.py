
print('\t\t\tLet\'s go to the \"world of math\"!')
import math

user_name = input('please input user name:')
if user_name == 'xwm64':
    print('\tHello xwm64!')
    print('Welcome to this program!')
    print('Now you can select 2 programs\n\tfirst progame is \'quadratic function\'\n\tsecond programe is \'stratified sampling\'')
    progame = input('please input the kind of progame:')
    if progame == 'first progame':
        print('\ta**2 + b + c = 0_this is the quadratic functions\n\tplease input a,b,c:') # 这是一个二次函数
        a = float(input('a = '))
        b = float(input('b = '))
        c = float(input('c = '))
        function_1 = (-b + math.sqrt(b ** 2 - 4 * a * c))/(2 * a)
        function_2 = (-b - math.sqrt(b ** 2 - 4 * a * c))/(2 * a)
        print(f'\n\tthe result of function is {function_1} and {function_2}')
        print()
    elif progame == 'second progame':
        print('\tNext way is stratified sampling') # 分层抽样
        print('\tNow,you can select 2 ways\n\tfirst way is stratified sampling of average\n\tsecond way is stratified sampling of variance')
        a = input('please input the kind of way:')
        if a == 'first way':
            print('\tplease input two samples of each average and each sample size:')
            numder_average_1 = float(input('first sample average= '))
            numder_average_2 = float(input('second sample average= '))
            numder_sample_size_1 = float(input('first sample size = '))
            numder_sample_size_2 = float(input('second sample size = '))
            stratified_sampling_of_average = ((numder_average_1 * numder_sample_size_1)) + ((numder_average_2 * numder_sample_size_2)) / (numder_sample_size_1 + numder_sample_size_2)
            print(f'\tthe result of stratified sampling of average is' + str(stratified_sampling_of_average))
        elif a == 'second way':
            print('\tplease input two samples of each variance , each sample size and each average:')
            numder_variance_1 = float(input('first sample variance= '))
            numder_variance_2 = float(input('second sample variance= '))
            numder_sample_size_1 = float(input('first sample size = '))
            numder_sample_size_2 = float(input('second sample size = '))
            numder_average_1 = float(input('first sample average= '))
            numder_average_2 = float(input('second sample average= '))
            stratified_sampling_of_average = ((numder_average_1 * numder_sample_size_1)) + ((numder_average_2 * numder_sample_size_2)) / (numder_sample_size_1 + numder_sample_size_2)
            stratified_sampling_of_variance = (numder_sample_size_1 * (numder_variance_1 ** 2 + (numder_average_1 - stratified_sampling_of_average) ** 2) + numder_sample_size_2 * (numder_variance_2 ** 2 + (numder_average_2 - stratified_sampling_of_average) ** 2)) / (numder_sample_size_1 + numder_sample_size_2)
            print(f'\tthe result of stratified sampling of variance is' + str(stratified_sampling_of_variance))
        elif a != 'first way' or 'second way':
            print('\tPlease input the right way')
    else:
        print('\tPlease input the right progame')
else:
    print('\tPlease input the right user name')        
print("\tThank you for using the program!")